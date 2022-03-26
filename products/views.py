from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
from django.http import HttpRequest, JsonResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth import REDIRECT_FIELD_NAME, get_user_model
from django.urls import reverse
from django.contrib import messages

from products.models import Category, Product, Review
from products.forms import ProductForm, ReviewForm
from products.serializers import ProductSerializer


User = get_user_model()


class ProductListView(ListView):
    model = Product
    paginate_by = 9


def get_products(request):
    # select * from products_category where is_active = 1
    categories = Category.objects.filter(is_active=True).all()
    # select id, name, slug, is_active from products_product
    products = Product.objects.order_by("-created_at").all()

    try:
        page_no = int(request.GET.get("page", "1"))
    except ValueError:
        page_no = 1

    paginator = Paginator(products, per_page=9)
    page_obj = paginator.page(page_no)

    return render(
        request,
        "products/product_list.html",
        context={"categories": categories, "page_obj": page_obj},
    )


class ProductDetailView(DetailView):
    model = Product
    pk_url_kwarg = "id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["developer"] = "Gledi"
        return context


def get_product_details(request: HttpRequest, pk):
    product = Product.objects.select_related("user").get(pk=pk)

    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect_to_login(
                request.path,
                reverse("login"),
                REDIRECT_FIELD_NAME,
            )
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = Review(
                product=product,
                rating=form.cleaned_data["rating"],
                comment=form.cleaned_data["comment"],
            )
            review.save()
            return redirect("product_details", pk=product.pk)
    else:
        form = ReviewForm()

    reviews = Review.objects.filter(approved=True).filter(product=product).all()

    return render(
        request,
        "products/product_details.html",
        context={
            "product": product,
            "reviews": reviews,
            "form": form,
        },
    )


@permission_required("products.add_product")
def add_product(request: HttpRequest):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = Product(**form.cleaned_data)
            product.user = request.user
            product.save()
            messages.success(
                request,
                "Product successfully added",
                extra_tags="product-saved",
            )
            return redirect("product_details", pk=product.pk)
    else:
        form = ProductForm()
    return render(
        request,
        "products/product_form.html",
        context={"form": form},
    )


def get_user_products(request, username):
    product_user = User.objects.get(username=username)
    return render(
        request, "products/user_products.html", context={"product_user": product_user}
    )


def get_latest_offers(request):
    offers = Product.objects.filter(price__lt=100).order_by("-id")[:3]
    ps = ProductSerializer(offers, many=True)
    return JsonResponse(ps.data, safe=False)


@permission_required("products.offer_discount")
def discount_product(request, pk):
    if request.method == "POST":
        product = Product.objects.get(pk=pk)
        product.discount = 5
        product.save()
        return redirect("product_details", pk=product.pk)

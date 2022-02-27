from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.views.generic import ListView

from products.models import Category, Product, Review
from products.forms import ReviewForm


class ProductListView(ListView):
    model = Product
    paginate_by = 9


def get_products(request):
    # select * from products_category where is_active = 1
    categories = Category.objects.filter(is_active=True).all()
    # select id, name, slug, is_active from products_product
    products = Product.objects.order_by("-id").all()

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


def get_product_details(request, pk):
    product = Product.objects.get(pk=pk)

    if request.method == "POST":
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

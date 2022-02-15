from django.shortcuts import render
from django.core.paginator import Paginator

from products.models import Category, Product


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

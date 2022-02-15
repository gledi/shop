from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404
from django.core.paginator import Paginator

from blog.models import Post


def get_post_list(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.filter(published=True).all()

    try:
        page_no = int(request.GET.get("page", "1"))
    except ValueError:
        page_no = 1

    paginator = Paginator(posts, per_page=5)
    page_obj = paginator.page(page_no)

    return render(request, "blog/post_list.html", context={"page_obj": page_obj})


def get_post_details(request: HttpRequest, slug: str) -> HttpResponse:
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        raise Http404("Post not found")
    return render(request, "blog/post_details.html", context={"post": post})

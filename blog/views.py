from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, Http404
from django.core.paginator import Paginator

from blog.models import Post, Comment
from blog.forms import CommentForm


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

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                post=post,
                comment=form.cleaned_data["comment"],
            )
            comment.save()
            return redirect("blog:post_details", slug=post.slug)
    else:
        form = CommentForm()

    comments = Comment.objects.filter(post=post).filter(approved=True).all()
    return render(
        request,
        "blog/post_details.html",
        context={"post": post, "form": form, "comments": comments},
    )

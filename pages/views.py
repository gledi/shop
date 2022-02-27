from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import user_passes_test


def home(request: HttpRequest) -> HttpResponse:
    return render(request, "pages/home.html")


class HomeView(TemplateView):
    template_name = "pages/home.html"


class PageView(TemplateView):
    def get_template_names(self):
        page_name = self.kwargs.get("page_name", "home")
        template_name = page_name.lower().replace("-", "_").strip()
        return [f"pages/{template_name}.html"]


@user_passes_test(lambda user: user.is_superuser)
def super_secret(request):
    return render(request, "pages/secret.html")

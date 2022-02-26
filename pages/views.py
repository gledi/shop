from re import template
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


def home(request: HttpRequest) -> HttpResponse:
    return render(request, "pages/home.html")


class HomeView(TemplateView):
    template_name = "pages/home.html"


class PageView(TemplateView):
    def get_template_names(self):
        page_name = self.kwargs.get("page_name", "home")
        template_name = page_name.lower().replace("-", "_").strip()
        return [f"pages/{template_name}.html"]

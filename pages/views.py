from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import user_passes_test
from django.utils.translation import activate
from django.conf import settings

from pages.decorators import is_loggedin


def home(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated() and request.user.username.startswith("gl"):
        return render(request, "pages/home.html")
    return redirect("login")


@is_loggedin
def big_prize(request):
    return render(request, "pages/big_prize.html")


class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get(self, request, *args, **kwargs):
        visits = request.session.get("visits", 0)
        visits += 1
        request.session["visits"] = visits
        return super().get(request, *args, **kwargs)


class PageView(TemplateView):
    def get_template_names(self):
        page_name = self.kwargs.get("page_name", "home")
        template_name = page_name.lower().replace("-", "_").strip()
        return [f"pages/{template_name}.html"]


@user_passes_test(lambda user: user.is_superuser)
def super_secret(request):
    return render(request, "pages/secret.html")


def policy_agreement(request):
    request.session["user_agreed"] = True
    return redirect("page", page_name="privacy_policy")


def switch_language(request: HttpRequest, language):
    activate(language=language)
    response = redirect(request.META["HTTP_REFERER"])
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    return response

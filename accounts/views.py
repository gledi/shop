from django.shortcuts import render
from .decorators import manager_required

from accounts.models import Employee


@manager_required
def manager_view(request):
    return render(request, "accounts/manager_view.html")


def everyone_view(request):
    return render(request, "accounts/everyone_view.html")

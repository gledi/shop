from functools import wraps

from django.shortcuts import redirect
from django.contrib import messages


def is_loggedin(func):
    @wraps(func)
    def _inner(request, *args, **kwargs):
        if request.user.is_authenticated:
            return func(request, *args, **kwargs)
        messages.error(request, "You must sign in to win!")
        return redirect("login")

    return _inner

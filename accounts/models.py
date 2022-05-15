from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

from .managers import UserManager


class User(AbstractUser):
    username = None

    email = models.EmailField(_("email"), unique=True, null=False, blank=False)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name"]

    objects = UserManager()

    class Meta:
        db_table = "users"
        verbose_name = _("user")
        verbose_name_plural = _("users")


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name=_("user"),
        null=True,
        on_delete=models.SET_NULL,
    )
    fullname = models.CharField(_("fullname"), max_length=255, null=False, blank=False)
    photo = models.ImageField(_("photo"), null=True, blank=True, upload_to="profiles/")
    telno = models.CharField(_("telephone number"), max_length=32)
    bio = models.TextField(_("biography"), null=True, blank=True)
    created = models.DateTimeField(_("created"), default=timezone.now, editable=False)
    modified = models.DateTimeField(_("modified"), default=timezone.now, editable=False)

    class Meta:
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")

    def __str__(self) -> str:
        return self.user.get_full_name()

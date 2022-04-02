from django.db import models
from django.conf import settings


class Employee(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL
    )
    telno = models.CharField(max_length=32)
    is_manager = models.BooleanField(default=False)
    manager = models.ForeignKey(
        "self",
        null=True,
        on_delete=models.SET_NULL,
        limit_choices_to=models.Q(is_manager=True),
    )

    def __str__(self) -> str:
        return self.user.get_full_name()

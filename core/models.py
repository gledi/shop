from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django_hashids import HashidsField


class BaseModel(models.Model):
    hid = HashidsField(real_field_name="id")
    created_at = models.DateTimeField(
        _("created at"),
        default=timezone.now,
        editable=False,
    )
    updated_at = models.DateTimeField(
        _("updated at"),
        default=timezone.now,
        editable=False,
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

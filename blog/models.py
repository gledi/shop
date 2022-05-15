from django.db import models
from django.urls import reverse
from django.utils.text import Truncator, slugify
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel
from utils.renderers import markdown


class Post(BaseModel):
    title = models.CharField(_("title"), max_length=255, null=False)
    slug = models.SlugField(unique=True)
    content = models.TextField(_("content"), null=False)
    content_html = models.TextField(null=True, editable=False)
    published = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("post")
        verbose_name_plural = _("posts")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.content_html = markdown(self.content)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog:post_details", kwargs={"slug": self.slug})


class Comment(BaseModel):
    post = models.ForeignKey(
        Post,
        verbose_name=_("post"),
        null=True,
        on_delete=models.SET_NULL,
        related_name="comments",
    )
    comment = models.TextField(_("comment"), null=False, blank=False)
    approved = models.BooleanField(_("approved"), default=False)

    class Meta:
        db_table = "comments"
        verbose_name = _("comment")
        verbose_name_plural = _("comments")
        get_latest_by = ("-created_at",)

    def __str__(self) -> str:
        return self.short

    @property
    def short(self) -> str:
        truncator = Truncator(self.comment)
        return truncator.chars(32)

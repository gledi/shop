from django.db import models
from django.urls import reverse
from django.utils.text import Truncator
from django.utils.translation import gettext_lazy as _

from utils.renderers import markdown


class Post(models.Model):
    title = models.CharField(_("title"), max_length=255, null=False)
    slug = models.SlugField(unique=True)
    content = models.TextField(_("content"), null=False)
    content_html = models.TextField(null=True, editable=False)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("post")
        verbose_name_plural = _("posts")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.content_html = markdown(self.content)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog:post_details", kwargs={"slug": self.slug})


class Comment(models.Model):
    post = models.ForeignKey(Post, null=True, on_delete=models.SET_NULL)
    comment = models.TextField(null=False)
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "comment"
        verbose_name_plural = "comments"
        db_table = "comments"

    def __str__(self):
        return self.short

    @property
    def short(self):
        truncator = Truncator(self.comment)
        return truncator.chars(20)

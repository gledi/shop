from django.db import models
from django.urls import reverse

from utils.renderers import markdown


class Post(models.Model):
    title = models.CharField(max_length=255, null=False)
    slug = models.SlugField(unique=True)
    content = models.TextField(null=False)
    content_html = models.TextField(null=True, editable=False)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.content_html = markdown(self.content)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog:post_details", kwargs={"slug": self.slug})

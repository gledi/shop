from django.db import models
from django.conf import settings
from django.utils.text import slugify, Truncator
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel


class Product(BaseModel):
    name = models.CharField(_("name"), max_length=255, null=False)
    code = models.CharField(_(""), max_length=12, null=False)
    price = models.DecimalField(_("price"), max_digits=8, decimal_places=2)
    discount = models.IntegerField(_("discount"), default=0)
    description = models.TextField(_("description"), null=True)
    category = models.ForeignKey("Category", null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL,
    )

    class Meta:
        db_table = "products"
        verbose_name = _("product")
        verbose_name_plural = _("products")
        permissions = (("offer_discount", "Can offer product discount"),)

    def __str__(self):
        return self.name

    @property
    def picture(self):
        return self.pictures.filter(is_cover=True).first().picture


class Picture(BaseModel):
    product = models.ForeignKey(
        Product,
        verbose_name=_("product"),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="pictures",
    )
    picture = models.ImageField(_("picture"), upload_to="products/")
    caption = models.CharField(_("caption"), max_length=255, null=True, blank=True)
    is_cover = models.BooleanField(_("is cover"), default=False)

    class Meta:
        db_table = "pictures"
        verbose_name = _("picture")
        verbose_name_plural = _("pictures")


class Category(models.Model):
    name = models.CharField(_("name"), max_length=30, null=False, unique=True)
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(_("is active"), default=True)

    class Meta:
        db_table = "categories"
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Review(BaseModel):
    product = models.ForeignKey(
        Product,
        verbose_name=_("product"),
        null=True,
        on_delete=models.SET_NULL,
        related_name="reviews",
    )
    rating = models.PositiveSmallIntegerField(_("rating"))
    comment = models.TextField(_("comment"), null=True)
    is_approved = models.BooleanField(_("is approved"), default=False)

    class Meta:
        db_table = "reviews"
        verbose_name = _("review")
        verbose_name_plural = _("reviews")

    def __str__(self):
        return self.short_comment

    @property
    def short_comment(self):
        truncator = Truncator(self.comment)
        return truncator.chars(20)

from django.db import models
from django.utils.text import slugify, Truncator


class Product(models.Model):
    # name varchar(255) not null
    name = models.CharField(max_length=255, null=False)
    code = models.CharField(max_length=12, null=False)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(null=True)
    picture = models.ImageField(upload_to="products")
    category = models.ForeignKey("Category", null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"
        # db_table = "products"

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30, null=False, unique=True)
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.short_comment

    @property
    def short_comment(self):
        truncator = Truncator(self.comment)
        return truncator.chars(20)

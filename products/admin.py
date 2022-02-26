from django.contrib import admin

from products.models import Product, Category, Review


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "price")
    list_editable = ("price",)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "is_active")
    readonly_fields = ("slug",)
    list_editable = ("is_active",)


admin.site.register(Category, CategoryAdmin)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["short_comment", "approved"]
    list_editable = ["approved"]

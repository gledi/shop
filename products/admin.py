from django.contrib import admin

from products.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "price")
    list_editable = ("price",)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "is_active")
    readonly_fields = ("slug",)
    list_editable = ("is_active",)


admin.site.register(Category, CategoryAdmin)

from django.contrib import admin

from products.models import Product, Category, Review


class ReviewInline(admin.TabularInline):
    model = Review


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "price")
    list_editable = ("price",)
    inlines = [ReviewInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "is_active")
    readonly_fields = ("slug",)
    list_editable = ("is_active",)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["short_comment", "is_approved"]
    list_editable = ["is_approved"]

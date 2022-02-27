from django.contrib import admin

from blog.models import Post, Comment


class CommentInline(admin.StackedInline):
    model = Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "published")
    list_editable = ("published",)
    prepopulated_fields = {"slug": ("title",)}
    inlines = [CommentInline]

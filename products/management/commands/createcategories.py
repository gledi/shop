from django.core.management.base import BaseCommand
from django.utils.text import slugify

from products.models import Category


class Command(BaseCommand):
    help = "Create product categories"

    def handle(self, *args, **options):
        category_names = [
            "Videogames",
            "Electronics & Computers",
            "Hobby & Fun",
            "Toys",
        ]

        for name in category_names:
            slug = slugify(name)
            category, created = Category.objects.update_or_create(
                name=name,
                slug=slug,
                defaults={"is_active": True},
            )

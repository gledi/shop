import io
import random

from django.core.management.base import BaseCommand, CommandError
from django.core.files.images import ImageFile
from faker import Faker

from products.models import Category, Product


class Command(BaseCommand):
    help = "Create some fake products"

    def add_arguments(self, parser):
        parser.add_argument(
            'product_count',
            type=int,
            nargs='?',
            default=10
        )

    def handle(self, *args, **options):
        product_count = options.get('product_count', 10)

        fake = Faker()

        cats = [c for c in Category.objects.all()]

        products = []
        for i in range(product_count):
            product = Product()

            product.name = fake.bs().title()
            product.code = fake.numerify("######")
            product.price = fake.pydecimal(
                left_digits=4,
                right_digits=2,
                min_value=5,
                max_value=5000,
            )
            product.description = fake.paragraph()
            img = fake.image()
            filename = f'{product.name.replace(" ", "_")}.png'
            product.picture = ImageFile(io.BytesIO(img), name=filename)
            product.category = random.choice(cats)

            products.append(product)

        Product.objects.bulk_create(products)

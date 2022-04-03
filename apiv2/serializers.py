from django.contrib.auth import get_user_model
from rest_framework import serializers

from products.models import Product, Review


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email")


class ProductSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Product
        fields = ["id", "name", "price", "user"]

    def create(self, validated_data):
        product = super().create(validated_data)
        product.code = "DEFCODE"
        product.save()
        return product


class ProductSerializerAlt(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "code", "price"]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("id", "rating", "comment")


class ProdSerializer(serializers.ModelSerializer):
    review_set = ReviewSerializer(many=True)

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "code",
            "price",
            "discount",
            "description",
            "review_set",
        )

    def create(self, validated_data):
        from pprint import pp

        pp(validated_data)

        reviews_data = validated_data.pop("review_set", [])

        pp(reviews_data)
        pp(validated_data)

        product = super().create(validated_data)
        product.user = self.context["request"].user
        for review_data in reviews_data:
            product.review_set.create(**review_data)

        product.save()

        return product

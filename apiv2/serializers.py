from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "price"]

    def create(self, validated_data):
        product = super().create(validated_data)
        product.code = "DEFCODE"
        product.save()
        return product


class ProductSerializerAlt(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "code", "price"]

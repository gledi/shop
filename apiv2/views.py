from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from products.models import Product
from .serializers import ProductSerializer, ProductSerializerAlt


class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return ProductSerializerAlt
        return super().get_serializer_class()


class ProductDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

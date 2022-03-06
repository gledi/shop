from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from products.models import Product
from .serializers import ProductSerializer, ProductSerializerAlt


class ProductListView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return ProductSerializerAlt
        return super().get_serializer_class()

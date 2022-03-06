from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.exceptions import NotFound
from rest_framework import status
from rest_framework.views import APIView
from apiv1.pagination import ShopPagination

from products.models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


@api_view(("GET", "POST"))
def category_list(request: Request, format=None) -> Response:
    if request.method == "GET":
        cats = Category.objects.filter(is_active=True).all()
        serializer = CategorySerializer(cats, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(("GET", "PUT", "PATCH", "DELETE"))
def category_details(request: Request, pk: int, format=None) -> Response:
    try:
        category = Category.objects.filter(is_active=True).get(pk=pk)
    except Category.DoesNotExist:
        return Response(
            {"detail": "Category does not exist"},
            status=status.HTTP_404_NOT_FOUND,
        )

    serializer = CategorySerializer(category)

    if request.method == "GET":
        return Response(serializer.data)
    elif request.method == "PUT" or request.method == "PATCH":
        serializer.initial_data = request.data
        serializer.partial = request.method == "PATCH"
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductListView(APIView):
    def get(self, request, format=None):
        products = Product.objects.order_by("id").all()
        pagination = ShopPagination()
        results = pagination.paginate_queryset(products, request)
        serializer = ProductSerializer(results, many=True)
        return pagination.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductView(APIView):
    def get_object(self, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise NotFound("Product not found")
        return product

    def get_serializer(self, instance, data=None, partial=False):
        serializer = ProductSerializer(instance=instance)
        if data is not None:
            serializer.initial_data = data
        serializer.partial = partial
        return serializer

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = self.get_serializer(product)
        return Response(serializer.data)

    def _update(self, request, pk, partial=False):
        product = self.get_object(pk)
        serializer = self.get_serializer(product, request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        return self._update(request, pk)

    def patch(self, request, pk, format=None):
        return self._update(request, pk, partial=True)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

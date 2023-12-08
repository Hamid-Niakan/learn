from django.db.models.aggregates import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import status
from .models import Product, Collection, OrderItem, Review
from .serializers import ProductSerializer, CollectionSerializer, ReviewSerializer
from .filters import ProductFilter
from .pagination import DefaultPagination


# class ProductViewSet(ModelViewSet):
#     serializer_class = ProductSerializer

#     def get_queryset(self):
#         queryset = Product.objects.all()
#         collection_id = self.request.query_params.get('collection_id')
#         if collection_id is not None:
#             queryset = queryset.filter(collection_id=collection_id)

#         return queryset

#     def destroy(self, request, *args, **kwargs):
#         if OrderItem.objects.filter(product_id=kwargs['pk']).count() > 0:
#             return Response(
#                 {
#                     'error': 'there is an order item with this product'
#                 },
#                 status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         return super().destroy(request, *args, **kwargs)

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = ['collection_id']
    filterset_class = ProductFilter
    pagination_class = DefaultPagination
    search_fields = ['title', 'description']
    ordering_fields = ['unit_price', 'last_update']

    def destroy(self, request, *args, **kwargs):
        if OrderItem.objects.filter(product_id=kwargs['pk']).count() > 0:
            return Response(
                {
                    'error': 'there is an order item with this product'
                },
                status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(
        products_count=Count('products')).all()
    serializer_class = CollectionSerializer

    def destroy(self, request, *args, **kwargs):
        if Product.objects.filter(collection_id=kwargs['pk']).count() > 0:
            return Response(
                {
                    'error': 'collection has products and can not be deleted'
                },
                status=status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}

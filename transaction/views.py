from django.http import JsonResponse
from transaction.models import Transacions, Category
from transaction.serializers import TransacionsSerializer, CategorySerializer
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend



class TransacionsViewSet(viewsets.ModelViewSet):
   
    queryset = Transacions.objects.all()
    serializer_class = TransacionsSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [ 'due_date']

class CategoryViewSet(viewsets.ModelViewSet):
   
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

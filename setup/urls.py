
from django.contrib import admin
from django.urls import include, path
from transaction.views import TransacionsViewSet, CategoryViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'transactions', TransacionsViewSet, basename='Transactions')
router.register(r'categories', CategoryViewSet, basename='Categories')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

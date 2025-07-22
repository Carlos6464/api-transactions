
from django.contrib import admin
from django.urls import path
from transaction.views import transactions

urlpatterns = [
    path('admin/', admin.site.urls),
    path('transactions/', transactions),
]

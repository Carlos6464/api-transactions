from django.db import models
from django.conf import settings 
from django.utils import timezone



class Category(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank= True, null=True, related_name='categories')
    name = models.CharField(max_length=255, blank=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
    
class Transacions(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='transactions')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='transactions')

    NATURE = (
        (1, 'Credit'),
        (-1, 'Debit')
    )
    description = models.CharField(max_length=255, blank=False)
    value = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    due_date = models.DateField(blank=False, default=timezone.now)
    nature = models.IntegerField(choices=NATURE, blank=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.description




from rest_framework import serializers
from .models import Category, Transacions

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TransacionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transacions
        fields = '__all__'


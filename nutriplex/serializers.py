from rest_framework import serializers
from .models import Category, Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name']

class CategorySerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'items']
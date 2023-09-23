from django.shortcuts import render
from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer
from django.http import HttpResponse
from .forms import ItemSelectionForm

# Create your views here.

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

def home(request):
    return HttpResponse("Welcome to the homepage!")

def select_items(request):
    categories = Category.objects.all().prefetch_related('item_set')
    selected_items = []

    if request.method == "POST":
        for category in categories:
            selected_in_category = request.POST.getlist(category.name)
            selected_items.extend(selected_in_category)

    context = {
        'categories': categories,
        'selected_items': selected_items
    }
    return render(request, 'select_items.html', context)
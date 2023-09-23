from django.urls import path
from .views import CategoryListView
from .views import select_items

urlpatterns = [
    path('select/', select_items, name='select-items'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
]
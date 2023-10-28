from django.urls import path, re_path
from .views import CategoryListView
from .views import select_items
from . import views

urlpatterns = [
    path('nutriplex/', select_items, name='select-items'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('recipe/', views.send_to_openai, name='send_to_openai'),
    re_path(r'^.*$', views.page_not_found, name='page_not_found'),
]
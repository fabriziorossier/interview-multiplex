import os
from openai import OpenAI
from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer
from django.http import HttpResponse

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

def send_to_openai(request):
    selected_items = []

    if request.method == "POST":
        categories = Category.objects.all()
        for category in categories:
            selected_in_category = request.POST.getlist(category.name)
            selected_items.extend(selected_in_category)
        
        client = OpenAI(
            api_key=os.environ['OPENAI_API_KEY']
        )

        message = f"Necesito una receta con los siguientes ingredientes: {', '.join(selected_items)}, ademas necesito las cantidades de cada ingrediente para la receta, los pasos para realizar la receta y el aporte calorico total de la receta, formatea la receta con codigo HTML utilizando solo tags h2, h3, ul, ol, li, y p, centrando en la pantalla los elementos h2. No indiques en la pagina informacion sobre HTML o los tags HTML."

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                        "type": "text",
                        "text": message
                        }
                    ]
                }
            ]
        )

        response_content = response.choices[0].message.content

        return render(request, 'response_template.html', {'response': response_content})

    return redirect('select_items')

def page_not_found(request):
    return render(request, '404.html', status=404)
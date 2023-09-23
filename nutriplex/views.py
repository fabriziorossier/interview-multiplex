import os
import openai
from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer
from django.http import HttpResponse
from .forms import ItemSelectionForm
from dotenv import load_dotenv

load_dotenv()

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
        
        # Send to OpenAI API
        openai.api_key = os.getenv("OPENAI_API_KEY")

        # Construct your message
        message = f"Necesito una receta con los siguientes ingredientes: {', '.join(selected_items)}, ademas necesito las cantidades de cada ingrediente para la receta, los pasos para realizar la receta y el aporte calorico total de la receta."

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": message}
            ]
        )

        response_content = response.choices[0].message.content

        # You can return this response to your template or handle it as needed
        return render(request, 'response_template.html', {'response': response_content})

    return redirect('select_items')
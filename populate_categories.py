import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'multiplex.settings')

import django
django.setup()

from nutriplex.models import Category

CATEGORIES = ["Frutas", "Vegetales", "Frutos Secos", "Pan y Cereales", "Lácteos", "Carnes y Proteicos", "Grasas", "Condimentos y saborizantes"]

for category in CATEGORIES:
    Category.objects.get_or_create(name=category)

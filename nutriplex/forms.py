from django import forms
from .models import Item

class ItemSelectionForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name']
        widgets = {
            'name': forms.CheckboxSelectMultiple
        }

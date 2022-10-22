from django import forms
from .models import CalorieTracker
class Form(forms.ModelForm):
    class Meta:
        model = CalorieTracker
        fields = ["calorie", "description",]
        labels = {'calorie': "Kalori", 
        "description": "Deskripsi",
        }
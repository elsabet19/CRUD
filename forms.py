from django.forms import ModelForm
from .models import Courses
from django import forms

class CoursesForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = '__all__'
        widgets = {
            'image': forms.ClearableFileInput(attrs={'style': 'width: 100%;'}),
            'type': forms.TextInput(attrs={'style': 'width: 100%; padding: 10px; margin-bottom: 10px; box-sizing: border-box; border: 1px solid #ccc; border-radius: 4px;'}),
            'money': forms.TextInput(attrs={'style': 'width: 100%; padding: 10px; margin-bottom: 10px; box-sizing: border-box; border: 1px solid #ccc; border-radius: 4px;'}),
            'title': forms.TextInput(attrs={'style': 'width: 100%; padding: 10px; margin-bottom: 10px; box-sizing: border-box; border: 1px solid #ccc; border-radius: 4px;'}),
            'description': forms.Textarea(attrs={'style': 'width: 100%; padding: 10px; margin-bottom: 10px; box-sizing: border-box; border: 1px solid #ccc; border-radius: 4px;'}),
            'personimage': forms.ClearableFileInput(attrs={'style': 'width: 100%;'}),
            'personname': forms.TextInput(attrs={'style': 'width: 100%; padding: 10px; margin-bottom: 10px; box-sizing: border-box; border: 1px solid #ccc; border-radius: 4px;'}),
            'trainer': forms.TextInput(attrs={'style': 'width: 100%; padding: 10px; margin-bottom: 10px; box-sizing: border-box; border: 1px solid #ccc; border-radius: 4px;'}),
            'money2': forms.TextInput(attrs={'style': 'width: 100%; padding: 10px; margin-bottom: 10px; box-sizing: border-box; border: 1px solid #ccc; border-radius: 4px;'}),
            'seats': forms.NumberInput(attrs={'style': 'width: 100%; padding: 10px; margin-bottom: 10px; box-sizing: border-box; border: 1px solid #ccc; border-radius: 4px;'}),
            'schedule': forms.TextInput(attrs={'style': 'width: 100%; padding: 10px; margin-bottom: 10px; box-sizing: border-box; border: 1px solid #ccc; border-radius: 4px;'}),
        }
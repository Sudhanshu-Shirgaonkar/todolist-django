from django.forms import ModelForm
from django import forms
from .models import Task

class TaskForm(ModelForm):
    title = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Enter Task'}))
    class Meta:

        model = Task

        fields = '__all__'
from django import forms
from .models import AddTodo

class AddTodoForm(forms.ModelForm):
    class Meta: 
        model = AddTodo
        fields = ('todo', 'description', 'completed')
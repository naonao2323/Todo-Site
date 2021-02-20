from .models import Todo
from django import forms


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        exclude = ('cretaed_at', 'updated_at')

        widgets = {
            'todo': forms.TextInput(attrs={
                'class': 'Todo_form',
               
            }),
        }
        labels = {
            'todo':"",
        }
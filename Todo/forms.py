from .models import Todo
from django import forms


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        exclude = ('cretaed_at', 'updated_at')
        widget=forms.Textarea
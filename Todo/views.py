from django.urls import reverse_lazy
from django.views import generic
from .models import Todo
from .forms import TodoForm


class TodoListView(generic.ListView):
    model = Todo
    paginate_by = 5

class TodoDetailView(generic.DetailView):
    model = Todo

class TodoCreateView(generic.CreateView):
    form_class = TodoForm
    model =Todo
    success_url = reverse_lazy('todo:list')

class TodoUpdateView(generic.UpdateView):
    form_class = TodoForm
    model = Todo
    success_url = reverse_lazy('todo:list')

class TodoDeleteView(generic.DeleteView):
    model = Todo
    success_url = reverse_lazy('todo:list')




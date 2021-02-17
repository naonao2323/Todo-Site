from django.urls import path,include
from . import views

app_name = "todo"
urlpatterns = [
    path('list/',views.TodoListView.as_view(), name="list"),
    path('detail/<pk>/', views.TodoDetailView.as_view(), name="detail"),
    path('create/',views.TodoCreateView.as_view(), name="create"),
    path('update/<pk>/',views.TodoUpdateView.as_view(),name="update"),
    path('delete/<pk>/',views.TodoDeleteView.as_view(), name="delete"),
]
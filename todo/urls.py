from django.urls import path
from . import views

urlpatterns = [
    # path('todos', views.add_todo, name='add_todo'),
    # path('todos', views.TodoListView.as_view(), name='add_todo'),
    path('todosapi/', views.TodoListApiView.as_view(), name='add_todo_api'),
]
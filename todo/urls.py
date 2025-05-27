from django.urls import path
from . import views

urlpatterns = [
    # path('', views.add_todo, name='add_todo'),
    path('', views.TodoListView.as_view(), name='add_todo'),
]
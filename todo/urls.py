from django.urls import path
from . import views

urlpatterns = [
    # path('todos', views.add_todo, name='add_todo'),

    # path('todos', views.TodoListView.as_view(), name='add_todo'),

    # path('todosapi/', views.TodoListApiView.as_view(), name='add_todo_api'),
    
    path('todosapi/', views.TodoListApiView2.as_view(), name='add_todo_api'),

    # path('todosapi/', views.TodoListApiView3.as_view(), name='add_todo_api'),

    # path('todosapi/<str:pk>/' , views.TodoDetailsApiView.as_view(), name='todo_detail_api'),

    path('todosapi/<str:pk>/' , views.TodoDetailsApiView2.as_view(), name='todo_detail_api'),
]
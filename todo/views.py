from django.shortcuts import render , redirect
from django.http import HttpResponse ,JsonResponse
from .forms import AddTodoForm
from .models import AddTodo

from rest_framework.response import Response

from django.views import View
# Create your views here.

def add_todo(request):
    return HttpResponse("This is todo List Page")


class TodoListView(View):
    def get(self , request):
        todos = AddTodo.objects.all()
        contex = {
            'todos' : todos
        }
        return render(request , 'todo.html' , contex)
        # return HttpResponse("This is todo List Page Class View")
    
    def post(self , request):
        # form = AddTodoForm(request.POST)
        # if form.is_valid():
        #     form.save()
        #     return redirect('todo_list')
        return HttpResponse("Form Submitted Seccesfully")
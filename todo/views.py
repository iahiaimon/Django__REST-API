from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import AddTodoForm
from .models import AddTodo

from rest_framework.response import Response
from rest_framework.views import APIView

from django.views import View

import json

# fucntion based view


def add_todo(request):
    return HttpResponse("This is todo List Page")


# class based View


class TodoListView(View):
    def get(self, request):
        todos = AddTodo.objects.all()
        contex = {"todos": todos}
        return render(request, "todo.html", contex)
        # return HttpResponse("This is todo List Page Class View")

    def post(self, request):
        # form = AddTodoForm(request.POST)
        # if form.is_valid():
        #     form.save()
        #     context = {
        #         'form' : form
        #     }
        #     return render(request , "todo.html" , context)

        return HttpResponse("Form Submitted Seccesfully")


# API VIEW


# class TodoListApiView(View):
#     def get(self, request):
#         todos = AddTodo.objects.all()

#         formatted_todo = []
#         for todo in todos:
#             formatted_todo.append(
#                 {
#                     "id": todo.id,
#                     "todo": todo.todo,
#                     "description": todo.description,
#                     "completed": todo.completed,
#                     "created_at": todo.created_at.strftime("%d/%m/%Y, %H:%M:%S"),
#                     "updated_at": todo.updated_at.strftime("%d/%m/%Y, %H:%M:%S"),
#                 }
#             )
#         formatted_todo = json.dumps(formatted_todo)

#         return HttpResponse(formatted_todo, content_type="application/json")


# # need to turn off csrt_token verification for this view

#     def post(self, request):
#         # data = request.body
#         formatted_todo = json.loads(request.body)

#         create_todo =AddTodo.objects.create(
#             todo = formatted_todo["todo"],
#             description = formatted_todo["description"],
#         )

#         data_to_return = {
#             "id": create_todo.id,
#             "todo": create_todo.todo,
#             "description": create_todo.description,

#         }
#         data_to_return = json.dumps(data_to_return)

#         # return HttpResponse("Form Submitted Seccesfully")
#         return HttpResponse(data_to_return , content_type= "application/json")


# Rest Frame Work API View  || This is just make easier to create API view


from rest_framework.serializers import ModelSerializer
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication,
    TokenAuthentication,
)


class AddTodoSerializer(ModelSerializer):
    class Meta:
        model = AddTodo
        fields = "__all__"


class TodoListApiView(APIView):

    # By which class user can authenticate
    authentication_classes = []

    # By which class user can access this view / authotize
    permission_classes = [AllowAny]

    def get(self, request):
        todos = AddTodo.objects.all()

        formatted_todo = AddTodoSerializer(todos, many=True).data

        return Response(formatted_todo)

    def post(self, request):
        # formatted_todo = json.loads(request.body)

        formatted_todo = request.data

        serializer = AddTodoSerializer(data=formatted_todo)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin


class TodoListApiView2(ListCreateAPIView):
    queryset = AddTodo.objects.all()
    serializer_class = AddTodoSerializer


# Need to explore ||

# class TodoListApiView3(ListModelMixin , CreateModelMixin , APIView):
#     queryset = AddTodo.objects.all()
#     serializer_class = AddTodoSerializer



class TodoDetailsApiView(APIView):

    def get(self, request, pk):
        todo = AddTodo.objects.all(pk=pk)
        formatted_todo = AddTodoSerializer(todo).data
        return Response(formatted_todo)

    def put(self, request, pk):
        todo = AddTodo.objects.get(pk=pk)
        formatted_todo = json.loads(request.data)
        serializer = AddTodoSerializer(instance = todo, data=formatted_todo)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        # return Response(serializer.errors)
        return Response({"message": "Todo Updated"})

    def delete(self, request, pk):
        todos = AddTodo.objects.get(pk=pk)
        todos.delete()
        return Response({"message": "Todo Deleted"})



from rest_framework.generics import RetrieveAPIView , UpdateAPIView , DestroyAPIView , RetrieveUpdateDestroyAPIView

class TodoDetailsApiView2(RetrieveUpdateDestroyAPIView):
    queryset = AddTodo.objects.all()
    serializer_class = AddTodoSerializer
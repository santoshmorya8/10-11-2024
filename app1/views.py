from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view()
def First_view(request):
    msg='This is our first view'
    return Response(data={'msg':msg})

@api_view(['GET','POST','PATCH','DELETE'])
def Second_view(request):
    if request.method == 'GET':
        msg='This is our get view'
    elif request.method == 'POST':
        msg='This is our post view'
    elif request.method == 'PATCH':
        msg='This is our patch view'
    elif request.method == 'DELETE':
        msg='This is our delete view'
    return  Response(data={'msg':msg})


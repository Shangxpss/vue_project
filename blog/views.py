from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .readHelper.readFun import readTxt, createFile

# Create your views here.

array = [{"name": "jory", "age": 123}, {"name": "tom", "age": 456}]


def home(request):
    data = createFile(r"C:\Users\Farben\Desktop\changeName",10)
    return JsonResponse({"text": 123}, safe=False)

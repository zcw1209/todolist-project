from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.
def hello(request):
    result = {"message": "測試!", "data": 123, "label": "文字標籤"}

    return JsonResponse(result)

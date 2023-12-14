#-*- code: utf-8 -*-
from django import HttpResponse

def hello(request):
    return HttpResponse("Hello World!")

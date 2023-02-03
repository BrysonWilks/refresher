from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, reverse, render
import time

# Create your views here

def test(request):
    return HttpResponse("Hello World! :) You made it to the second page!")


def home(request):
    render(request, 'home.html')
    time.sleep(10)
    return redirect(reverse(test))


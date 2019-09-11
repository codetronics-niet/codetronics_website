from django.shortcuts import render
from django.contrib import messages


def homepage(request):
    message = messages.get_messages(request)
    return render(request, 'home.html', {'message': message})

from django.shortcuts import render, HttpResponse


def event(request):
    return HttpResponse("hello events page")

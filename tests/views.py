from django.shortcuts import render


def index(request):
    return render(request, 'tests/index.html')


def bg_gray(request):
    return render(request, 'tests/bg_gray.html')
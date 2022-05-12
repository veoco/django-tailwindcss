from django.shortcuts import render


def index(request):
    return render(request, 'tests/index.html')


def index_raw(request):
    return render(request, 'tests/index_raw.html')


def bg_gray(request):
    return render(request, 'tests/bg_gray.html')
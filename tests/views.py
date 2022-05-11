from django.shortcuts import render


def index(request):
    return render(request, 'tests/index.html')


def bg_gray(request):
    return render(request, 'tests/bg_gray.html')


def bg_gray_raw(request):
    return render(request, 'tests/bg_gray_raw.html')


def tpl_bg_slate(request):
    return render(request, 'tests/tpl_bg_slate.html')

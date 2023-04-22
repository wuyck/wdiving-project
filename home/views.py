from django.shortcuts import render

def home(request):

    return render(request, 'home/home.html')


def learnMore(request):

    return render(request, 'home/more_info.html')

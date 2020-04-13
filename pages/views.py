from django.shortcuts import render

def homePageView(request):
    return render(request, 'home.html')

def aboutPageView(request):
    return render(request, 'about.html')
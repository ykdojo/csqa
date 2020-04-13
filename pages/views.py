from django.shortcuts import render

def aboutPageView(request):
    return render(request, 'about.html')
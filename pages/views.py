from django.shortcuts import render

def aboutPageView(request):
    return render(request, 'about.html', {'current_user': request.user})

def searchView(request):
    return render(request, 'search.html', {'current_user': request.user})
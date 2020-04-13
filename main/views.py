from django.shortcuts import render

def homeFeedView(request):
    current_user = request.user
    if not current_user.is_authenticated:
        current_user = None
    context = {'current_user': current_user}
    return render(request, 'home.html', context)
from django.shortcuts import render
from main.models import Question

def homeFeedView(request):
    current_user = request.user
    if not current_user.is_authenticated:
        current_user = None
    
    # TODO: Only retrieve recent questions.
    # questions = Question.objects.all().order_by('-date')
    context = {
        'current_user': current_user,
        'questions': questions
    }
    return render(request, 'home.html', context)
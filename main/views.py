from django.shortcuts import render
from main.models import Question

def homeFeedView(request):
    current_user = request.user
    
    # TODO: Only retrieve recent questions.
    questions = Question.objects.all().order_by('-created')[:30]
    context = {
        'current_user': current_user,
        'questions': questions
    }
    return render(request, 'home.html', context)
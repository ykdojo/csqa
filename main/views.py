from django.shortcuts import render
from main.models import Question

def homeFeedView(request):
    current_user = request.user
    
    hostname = request.get_host()
    questions = Question.objects.all().order_by('-created')[:30]
    questions_exist = len(questions) > 0
    context = {
        'current_user': current_user,
        'questions': questions,
        'questions_exist': questions_exist,
        'hostname': hostname
    }
    return render(request, 'home.html', context)
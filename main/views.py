from django.shortcuts import render
from main.models import Question
from django.core.paginator import Paginator

from django.conf import settings

def listing(request):
    return render(request, 'list.html', {'page_obj': page_obj})

def homeFeedView(request):
    print('DATABASES (yk1):')
    print(settings.DATABASES)
    current_user = request.user
    
    questions = Question.objects.all().order_by('-created')
    paginator = Paginator(questions, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    questions_exist = len(questions) > 0
    context = {
        'current_user': current_user,
        'page_obj': page_obj,
        'questions_exist': questions_exist
    }
    return render(request, 'home.html', context)
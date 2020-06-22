from django.shortcuts import render
from main.models import Question
from users.models import User
from django.core.paginator import Paginator

def homeFeedView(request):
    current_user = request.user
    
    questions = Question.objects.filter(points__gt=-2, hidden=False).order_by('-created')
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

def leaderboardView(request):
    current_user = request.user

    leaders = User.objects.filter(points__gt=0).order_by('-points')[:25]
    context = {'current_user': current_user, 'leaders': leaders}
    return render(request, 'leaderboard.html', context)

def testView(request):
    current_user = request.user
    context = {'username': current_user.username,
               'current_user': current_user}
    return render(request, 'test.html', context)
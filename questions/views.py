from django.http import HttpResponseRedirect, HttpResponseBadRequest, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from main.models import Question, Answer, QuestionForm, AnswerForm

# vote_type could be 'upvote', 'downvote', or 'cancel_vote'
def updateVote(user, question, vote_type):
    user.upvoted_questions.remove(question)
    user.downvoted_questions.remove(question)

    # if this is an upvote, add an upvote. otherwise, add a downvote.
    if vote_type == 'upvote':
        user.upvoted_questions.add(question)
    elif vote_type == 'downvote':
        user.downvoted_questions.add(question)

    question.update_points()
    return question.points

def voteView(request, id):
    current_user = request.user
    question = Question.objects.get(pk=id)
    if not current_user.is_authenticated:
        return JsonResponse({'not_logged_in': True})
    if current_user.id == question.user_id:
        return HttpResponseBadRequest('Same user')
    if request.method != 'POST':
        return HttpResponseBadRequest('The request is not POST')
    vote_type = request.POST.get('vote_type')
    points = updateVote(current_user, question, vote_type)
    return JsonResponse({'vote_type': vote_type, 'points': points})

def questionView(request, id):
    current_user = request.user
    question = Question.objects.get(pk=id)
    answers = Answer.objects.filter(question_id=id).order_by('created')
    upvoted = None
    downvoted = None
    asked_by_user = False

    if not current_user.is_authenticated:
        pass
    elif current_user.upvoted_questions.filter(id=question.id).count() > 0:
        upvoted = 'done'
    elif current_user.downvoted_questions.filter(id=question.id).count() > 0:
        downvoted = 'done'
    elif current_user.id == question.user_id:
        asked_by_user = True
        
    context = {'question': question, 'answers': answers,
               'current_user': current_user,
               'upvoted': upvoted, 'downvoted': downvoted,
               'asked_by_user': asked_by_user}
    return render(request, 'question.html', context)

def newView(request):
    current_user = request.user

    if not current_user.is_authenticated:
        return HttpResponseRedirect(reverse('account_signup'))

    if request.method != 'POST':
        render(request, 'new.html', {'current_user': current_user})
    
    form = QuestionForm(request.POST)
    if not form.is_valid():
        return render(request, 'new.html', {'current_user': current_user})
    
    q = Question(
        user_id = current_user.id,
        title = form.cleaned_data['title'],
        body = form.cleaned_data['body']
    )
    q.save()
    return HttpResponseRedirect('/')

def answerView(request, id):
    current_user = request.user

    if not current_user.is_authenticated:
        return HttpResponseRedirect('/accounts/login')
    if not request.method == 'POST':
        return HttpResponseRedirect(f'/question/{id}')
    form = AnswerForm(request.POST)
    if not form.is_valid():
        return HttpResponseRedirect(f'/question/{id}')
    a = Answer(
        user_id = current_user.id,
        question_id = id,
        text = form.cleaned_data['text']
    )
    a.save()
    return HttpResponseRedirect(f'/question/{id}')

def myAnswersView(request):
    current_user = request.user
    answers = Answer.objects.filter(user_id = current_user.id).order_by('-created')
    answers_exist = len(answers) > 0
    return render(request, 'my_answers.html',
                    {'current_user': current_user,
                    'answers_exist': answers_exist,
                    'answers': answers})

def myQuestionsView(request):
    current_user = request.user
    questions = Question.objects.filter(user_id = current_user.id).order_by('-created')
    questions_exist = len(questions) > 0
    return render(request, 'my_questions.html',
                  {'current_user': current_user, 'questions': questions,
                   'questions_exist': questions_exist})
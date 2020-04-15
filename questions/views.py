from django.http import HttpResponseRedirect
from django.shortcuts import render
from main.models import Question, Answer, QuestionForm, AnswerForm

def questionView(request, id):
    current_user = request.user
    question = Question.objects.get(pk=id)
    answers = Answer.objects.filter(question_id=id).order_by('-created')
    context = {'question': question, 'answers': answers, 'current_user': current_user}
    return render(request, 'question.html', context)

def newView(request):
    current_user = request.user

    if not current_user.is_authenticated:
        return HttpResponseRedirect('/accounts/login')

    if request.method != 'POST':
        render(request, 'new.html')
    
    form = QuestionForm(request.POST)
    if not form.is_valid():
        return render(request, 'new.html')
    
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
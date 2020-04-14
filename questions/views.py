from django.http import HttpResponseRedirect
from django.shortcuts import render
from main.models import Question, QuestionForm

def questionView(request, id):
    question = Question.objects.get(pk=id)
    return render(request, 'question.html', {'question': question})

def newView(request):
    current_user = request.user

    if request.method == 'POST':
        if not current_user.is_authenticated:
            HttpResponseRedirect('/accounts/login')            
        form = QuestionForm(request.POST)
        if form.is_valid():
            q = Question(
                user_id = current_user.id,
                title = form.cleaned_data['title'],
                body = form.cleaned_data['body']
            )
            q.save()
            return HttpResponseRedirect('/')
    else:
        form = QuestionForm()
    return render(request, 'new.html', {'form': form})
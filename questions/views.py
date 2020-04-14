from django.http import HttpResponseRedirect
from django.shortcuts import render
from main.models import Question, QuestionForm

def questionView(request, id):
    question = Question.objects.get(pk=id)
    return render(request, 'question.html', {'question': question})

def newView(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')
    else:
        form = QuestionForm()
    return render(request, 'new.html', {'form': form})
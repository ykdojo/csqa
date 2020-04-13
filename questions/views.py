from django.shortcuts import render
from main.models import Question

def questionView(request, id):
    question = Question.objects.get(pk=id)
    return render(request, 'question.html', {'question': question})

def newView(request):
    return render(request, 'new.html')
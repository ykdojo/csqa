from django.shortcuts import render

def questionView(request, id):
    return render(request, 'question.html', {'id': id})

from django.db import models
from django.contrib.auth.models import User
from django import forms
import datetime

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    created     = models.DateTimeField(editable=False)
    modified    = models.DateTimeField()
    
    # Return a string like:
    # '223 days ago'
    # '3 hours ago'
    # '23 minutes ago'
    # '20 seconds ago'
    @property
    def x_ago(self):
        diff = datetime.datetime.now(datetime.timezone.utc) - self.created
        if diff.days > 0:
            return f'{diff.days} days ago'
        if diff.seconds < 60:
            return f'{diff.seconds} seconds ago'
        if diff.seconds < 3600:
            return f'{diff.seconds // 60} minutes ago'
        return f'{diff.seconds // 3600} hours ago'
        

        
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = datetime.datetime.now()
        self.modified = datetime.datetime.now()
        return super(Question, self).save(*args, **kwargs)
    def __str__(self):
        return self.title

class QuestionForm(forms.Form):
    title = forms.CharField(max_length=200)
    body = forms.CharField(max_length=5000, widget=forms.Textarea)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    def __str__(self):
        return self.text

class AnswerForm(forms.Form):
    text = forms.CharField(max_length=5000, widget=forms.Textarea)
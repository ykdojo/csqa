from django.db import models
from users.models import CustomUser
from django import forms
import datetime

# Taking a time difference as inputs, it returns a string like:
# '223 days ago'
# '3 hours ago'
# '23 minutes ago'
# '20 seconds ago'
def x_ago_helper(diff):
    if diff.days > 0:
        return f'{diff.days} days ago'
    if diff.seconds < 60:
        return f'{diff.seconds} seconds ago'
    if diff.seconds < 3600:
        return f'{diff.seconds // 60} minutes ago'
    return f'{diff.seconds // 3600} hours ago'

class Question(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField(blank=True, null=True)
    created     = models.DateTimeField(editable=False)
    modified    = models.DateTimeField()
    answers_count = models.IntegerField(default=0)

    @property
    def num_answers(self):
        answers = Answer.objects.filter(question_id = self.id)
        return len(answers)
    def x_ago(self):
        diff = datetime.datetime.now(datetime.timezone.utc) - self.created
        return x_ago_helper(diff)
        
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
    body = forms.CharField(max_length=5000, widget=forms.Textarea, required=False)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()

    @property
    def x_ago(self):
        diff = datetime.datetime.now(datetime.timezone.utc) - self.created
        return x_ago_helper(diff)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = datetime.datetime.now()
        self.modified = datetime.datetime.now()
        return super(Answer, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.text

class AnswerForm(forms.Form):
    text = forms.CharField(max_length=5000, widget=forms.Textarea)
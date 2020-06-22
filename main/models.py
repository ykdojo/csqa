from django.db import models
from django.conf import settings
from django.utils.html import urlize
from django import forms
from django.utils import timezone
from rest_framework import serializers
from django.utils.html import escape

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

def update_points_helper(obj):
    upvotes = obj.upvoted_users.filter(is_shadow_banned=False).distinct().count()
    downvotes = obj.downvoted_users.filter(is_shadow_banned=False).distinct().count()
    downvotes += obj.downvoted_users.filter(is_staff=True).count()
    obj.points = upvotes - downvotes
    obj.save()

class Question(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField(blank=True, null=True)
    created     = models.DateTimeField(editable=False)
    modified    = models.DateTimeField()
    answers_count = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    hidden = models.BooleanField(default=False)

    @property
    def num_answers(self):
        answers = Answer.objects.filter(question_id = self.id)
        return len(answers)
    def x_ago(self):
        diff = timezone.now() - self.created
        return x_ago_helper(diff)
    def show_points(self):
        if self.points < 0:
            return 0
        else:
            return self.points

    def update_points(self):
        update_points_helper(self)
        
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Question, self).save(*args, **kwargs)
    def __str__(self):
        return self.title

class QuestionForm(forms.Form):
    title = forms.CharField(max_length=200)
    body = forms.CharField(max_length=5000, widget=forms.Textarea, required=False)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()
    points = models.IntegerField(default=0)
    hidden = models.BooleanField(default=False)

    @property
    def x_ago(self):
        diff = timezone.now() - self.created
        return x_ago_helper(diff)
    
    def update_points(self):
        update_points_helper(self)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Answer, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.text

class AnswerForm(forms.Form):
    text = forms.CharField(max_length=5000, widget=forms.Textarea)

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('user', 'title', 'body', 'created', 'answers_count', 'points')

class CreatedField(serializers.RelatedField):
    def to_representation(self, value):
        diff = timezone.now() - value
        return x_ago_helper(diff)

class UserField(serializers.Field):
    def to_representation(self, value):
        return value.username

class AnswerSerializer(serializers.ModelSerializer):
    user = UserField()
    x_ago = serializers.SerializerMethodField()
    text_html = serializers.SerializerMethodField()

    class Meta:
        model = Answer
        fields = ('text_html', 'x_ago', 'user', 'id', 'points', 'hidden')

    def get_text_html(self, obj):
        return urlize(escape(obj.text))

    def get_x_ago(self, obj):
        return x_ago_helper(timezone.now() - obj.created)

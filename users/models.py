from django.db import models
from django.contrib.auth.models import AbstractUser
from main.models import Question, Answer

class User(AbstractUser):
    class Meta:
        db_table = 'auth_user'
    upvoted_questions = models.ManyToManyField(Question, related_name="upvoted_users")
    downvoted_questions = models.ManyToManyField(Question, related_name="downvoted_users")
    upvoted_answers = models.ManyToManyField(Answer, related_name="upvoted_users")
    downvoted_answers = models.ManyToManyField(Answer, related_name="downvoted_users")

from django.db import models

from django.contrib.auth.models import AbstractUser, UserManager
from django.apps import apps

class CustomUserManager(UserManager):
    pass

class CustomUser(AbstractUser):
    objects = CustomUserManager()
    upvoted_questions = models.ManyToManyField('main.Question', related_name="upvoted_users")
    downvoted_questions = models.ManyToManyField('main.Question', related_name="downvoted_users")
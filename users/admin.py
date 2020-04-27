from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

UserAdmin.list_display += ('points', )

admin.site.register(User, UserAdmin)
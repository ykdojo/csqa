from django.contrib import admin
from django.urls import path, include
from main.views import homeFeedView
from pages.views import aboutPageView
from questions.views import questionView, newView, answerView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeFeedView),
    path('about/', aboutPageView),
    path('accounts/', include('allauth.urls')),
    path('question/<int:id>/', questionView),
    path('question/<int:id>/answer', answerView),
    path('question/new/', newView),
]

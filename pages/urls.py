from django.urls import path
from .views import homePageView, aboutPageView

urlpatterns = [
    path('', homePageView),
    path('about', aboutPageView),
]
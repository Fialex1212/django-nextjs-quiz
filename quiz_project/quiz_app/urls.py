from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home, name='home'),
    path('create_quiz/', create_quiz, name='create_quiz'),
    path('quiz/<int:pk>/', quiz, name='quiz'),
    path('sign-up/', sign_up_page, name='sing_up'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('search/', search, name='search')
]
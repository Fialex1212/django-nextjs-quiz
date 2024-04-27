from django.urls import path
from .views import *

urlpatterns = [
    #login/sign-in
    path('sign-up/', sign_up_page, name='sign_up'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),

    #main
    path('', preloader, name='preloader'),
    path('home/', home, name='home'),
    path('search/', search, name='search'),

    #quiz
    path('create_quiz/', create_quiz, name='create_quiz'),
    path('quiz/<int:id>/', quiz_details, name='quiz_details'),
    path('quiz/<int:quiz_id>/question/<int:question_id>', quiz, name='quiz'),
    path('quiz_result/<int:id>', quiz_result, name='quiz_result'),

    #user
    path('user/<int:pk>/', user_page, name='user'),
    path('user/<int:pk>/settings/', user_settings, name='user_settings'),
    path('user/<int:pk>/liked/', user_liked, name='user_liked'),
]
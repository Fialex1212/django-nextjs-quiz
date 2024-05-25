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
    path('quiz/create/', create_quiz, name='create_quiz'),
    path('quiz/details/<int:id>/', quiz_details, name='quiz_details'),
    path('quiz/<int:quiz_id>/question/<int:question_id>/', quiz, name='quiz'),
    path('quiz/result/<int:quiz_id>/ ', quiz_result, name='quiz_result'),
    path('quiz_like/<int:quiz_id>/', quiz_like, name='quiz_like'),
    path('quiz_dislike/<int:quiz_id>/', quiz_dislike, name='quiz_dislike'),
    path("quiz/<int:quiz_id>/change/", quiz_change, name="quiz_change"),
    path("quiz/<int:quiz_id>/change/question/<int:question_id>", quiz_change_question, name="quiz_change_question"),
    path("quiz/<int:quiz_id>/add/question/", quiz_add_question, name="quiz_add_question"),
    path("quiz/<int:quiz_id>/add/question/<int:question_id>/answer/", quiz_add_answer, name="quiz_add_answer"),

    #user
    path('user/<int:pk>/', user_page, name='user'),
    path('user/<int:pk>/liked/', user_liked, name='user_liked'),
    path('user/<int:pk>/change/username/', user_change_username, name='user_change_username'),
    path('user/<int:pk>/change/email/', user_change_email, name='user_change_email'),
    path('user/<int:pk>/change/password', user_change_passwrod, name='user_change_password'),
]
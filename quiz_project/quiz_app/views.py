from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils import timezone
from .forms import *
from .models import *
import time


#login/sign-in
def sign_up_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)

            username = request.POST.get('username')
            email = request.POST.get('email')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')

            if form.is_valid():
                user = form.save(commit=False)
                user.username = username
                user.email = email
                user.set_password(password1)
                user.save()
                messages.success(request, 'Account was successful created' + username)
                return redirect('login')
    context = {'form': form}
    return render(request, 'quiz_app/login__sign_up/sign_up.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'User successful login')
                return redirect('home')
            else:
                messages.error(request, 'Username or password incorrect')

    return render(request, 'quiz_app/login__sign_up/login.html')


def logout_page(request):
    logout(request)
    messages.success(request, 'You was successful logout')
    return redirect('login')


#main
def preloader(request):
    return render(request, 'quiz_app/preloader.html')


def home(request):
    quizzes = Quiz.objects.all()
    context = {"title": 'home', 'quizzes': quizzes}
    return render(request, 'quiz_app/main/home.html', context)


def search(request):
    query = request.GET.get('q')
    print(query)
    quizzes = Quiz.objects.none()  # Initialize an empty queryset

    if query:  # Check if query parameter exists
        quizzes = Quiz.objects.filter(title__icontains=query)
    context = {'quizzes': quizzes}
    return render(request, 'quiz_app/main/search.html', context)


#quiz
def quiz_details(request,  pk):
    quiz = Quiz.objects.get(pk=pk)
    context = {'quiz': quiz}
    return render(request, 'quiz_app/quiz/quiz_details.html', context)


def quiz(request, quiz_id, question_id):
    quiz = Quiz.objects.get(id=quiz_id)
    question = Question.objects.get(quiz__id=quiz_id, id=question_id)
    next_question = Question.objects.filter(quiz__id=quiz_id, id__gt=question_id).order_by('id').first()
    context = {'quiz': quiz, 'question': question, 'next_question': next_question}
    return render(request, 'quiz_app/quiz/quiz.html', context)


def create_quiz(request):
    form = CreateQuiz()
    if request.method == "POST":
        form = CreateQuiz(request.POST)
        title = request.POST.get('title')
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.title = title
            quiz.author = request.user
            quiz.created_at = timezone.now()
            quiz.save()
            return redirect('quiz_details', pk=quiz.pk)
    context = {'form': form}
    return render(request, 'quiz_app/quiz/create_quiz.html', context)


def quiz_result(request):
    context = {}
    return render(request, 'quiz_app/quiz/quiz_result', context)


def quiz_wrong(request):
    return render(request, 'quiz_app/quiz/quiz_result')


#user
def user_page(request, pk):
    user = User.objects.get(pk=pk)
    user_avatar = UserProfile.objects.get(user=user.pk)
    context = {'user': user, 'user_avatar': user_avatar}
    return render(request, 'quiz_app/user/user.html', context)


def user_settings(request, pk):
    user = User.objects.get(pk=pk)
    context = {'user': user}
    return render(request, 'quiz_app/user/settings.html', context)


def user_liked(request, pk):
    user = User.objects.get(pk=pk)
    context = {'user': user}
    return render(request, 'quiz_app/user/liked.html', context)








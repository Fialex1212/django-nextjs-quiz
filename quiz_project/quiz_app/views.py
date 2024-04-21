from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm
from .models import *


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
    return render(request, 'quiz_app/sign_up.html', context)


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

    return render(request, 'quiz_app/login.html')


def logout_page(request):
    logout(request)
    messages.success(request, 'You was successful logout')
    return redirect('login')


#main
def home(request):
    quizzes = Quiz.objects.all()
    like_counts = {}
    for quiz in quizzes:
        like_counts[quiz.pk] = LikeQuiz.objects.filter(quiz=quiz).count()
    context = {"title": 'home', 'quizzes': quizzes, 'like_counts': like_counts}
    return render(request, 'quiz_app/home.html', context)


def search(request):
    query = request.GET.get('q')
    print(query)
    quizzes = Quiz.objects.none()  # Initialize an empty queryset

    if query:  # Check if query parameter exists
        quizzes = Quiz.objects.filter(title__icontains=query)
    context = {'quizzes': quizzes}
    return render(request, 'quiz_app/search.html', context)


#quiz
def quiz_details(request,  pk):
    quiz = Quiz.objects.get(pk=pk)
    context = {'quiz': quiz}
    return render(request, 'quiz_app/quiz/quiz_details.html', context)


def quiz(request, quiz_pk, question_pk):
    quiz = Quiz.objects.get(pk=quiz_pk)
    question = Question.objects.filter(quiz__title__icontains=quiz.title, pk=question_pk)
    context = {'quiz': quiz, 'question': question}
    return render(request, 'quiz_app/quiz/quiz.html', context)


def create_quiz(request):
    return render(request, 'quiz_app/quiz/create_quiz.html')


#user
def user_page(request, pk):
    user = User.objects.get(pk=pk)
    context = {'user': user}
    return render(request, 'quiz_app/user/user.html', context)


def user_settings(request, pk):
    user = User.objects.get(pk=pk)
    context = {'user': user}
    return render(request, 'quiz_app/user/settings.html', context)


def user_liked(request, pk):
    user = User.objects.get(pk=pk)
    context = {'user': user}
    return render(request, 'quiz_app/user/liked.html', context)








from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm
from .models import *

def home(request):
    quizzes = Quiz.objects.all()
    context = {"title": 'home', 'quizzes': quizzes}
    return render(request, 'quiz_app/home.html', context)


def quiz(request,  pk):
    quiz = Quiz.objects.get(pk=pk)
    context = {'quiz': quiz}
    return render(request, 'quiz_app/quiz.html', context)


def create_quiz(request):
    return render(request, 'quiz_app/create_quiz.html')


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


def search(request):
    query = request.GET.get('q')
    print(query)
    quizzes = Quiz.objects.none()  # Initialize an empty queryset

    if query:  # Check if query parameter exists
        quizzes = Quiz.objects.filter(title__icontains=query)
    context = {'quizzes': quizzes}
    return render(request, 'quiz_app/search.html', context)



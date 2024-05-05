from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils import timezone
from django.http import JsonResponse
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
                messages.success(request, 'Account was successfully created' + username)

                return redirect('login')
            else:
                if password1 != password2:
                    messages.error(request, 'Different passwords')
                else:
                    messages.error(request, 'Some input is wrong')
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
                messages.success(request, 'You have successfully logged!')
                return redirect('home')
            else:
                messages.error(request, 'Username or password incorrect')

    return render(request, 'quiz_app/login__sign_up/login.html')


def logout_page(request):
    logout(request)
    messages.success(request, 'You have successfully logged out!')
    return redirect('login')


#main
def preloader(request):
    return render(request, 'quiz_app/preloader.html')


def home(request):
    quizzes = Quiz.objects.all()
    liked_quizzes = set(LikeQuiz.objects.filter(user__id=request.user.pk).values_list('quiz_id', flat=True))
    context = {"title": 'home', 'quizzes': quizzes, 'liked_quizzes': liked_quizzes}
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
def quiz_details(request,  id):
    quiz = Quiz.objects.get(id=id)
    question = Question.objects.filter(quiz=quiz).first()
    context = {'quiz': quiz, 'question': question}
    return render(request, 'quiz_app/quiz/quiz_details.html', context)


def quiz(request, quiz_id, question_id):
    quiz = Quiz.objects.get(id=quiz_id)
    question = Question.objects.get(quiz__id=quiz_id, id=question_id)
    next_question = Question.objects.filter(quiz__id=quiz_id, id__gt=question_id).order_by('id').first()
    context = {'quiz': quiz, 'question': question, 'next_question': next_question}
    return render(request, 'quiz_app/quiz/quiz.html', context)


def quiz_like(request, quiz_id):
    user = request.user
    quiz = get_object_or_404(Quiz, id=quiz_id)
    like, created = LikeQuiz.objects.get_or_create(user=user, quiz=quiz)
    if created:
        return JsonResponse({'status': 'success'})


def quiz_dislike(request, quiz_id):
    user = request.user
    like = get_object_or_404(LikeQuiz, user=user, quiz_id=quiz_id)
    like.delete()
    return JsonResponse({'status': 'success'})


def create_quiz(request):
    form = CreateQuiz(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            title = form.cleaned_data['title']
            tags_input = form.cleaned_data['tags']
            selected_tags = []

            if tags_input:
                tag_names = [name.strip() for name in tags_input.split(',')]

                for tag_name in tag_names:
                    tag, created = Tag.objects.get_or_create(content=tag_name)
                    selected_tags.append(tag)

            quiz = form.save(commit=False)
            quiz.title = title
            quiz.author = request.user
            quiz.created_at = timezone.now()
            quiz.save()
            quiz.tags.set(selected_tags)
            return redirect('quiz_details', id=quiz.id)
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
    # user_avatar = UserProfile.objects.get(user=user.pk)
    user_avatar = "a"
    context = {'user': user, 'user_avatar': user_avatar}
    return render(request, 'quiz_app/user/user.html', context)


def user_liked(request, pk):
    user = User.objects.get(pk=pk)
    liked = LikeQuiz.objects.filter(user__id=pk).select_related('quiz')
    context = {'user': user, 'liked': liked}
    return render(request, 'quiz_app/user/liked.html', context)








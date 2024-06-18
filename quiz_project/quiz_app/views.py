from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.http import JsonResponse
from .forms import *
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


@login_required()
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
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    questions = quiz.question_set.all()
    total_questions = questions.count()
    current_question = get_object_or_404(Question, id=question_id, quiz=quiz)
    next_question = list(questions.values_list('id', flat=True))
    try:
        next_question_index = next_question.index(current_question.id) + 1
        next_question_id = next_question[next_question_index]
    except IndexError:
        next_question_id = None

    if request.method == "POST":
        form = QuizForm(request.POST, questions=[current_question])
        if form.is_valid():
            if 'quiz_answers' not in request.session:
                request.session['quiz_answers'] = {}
            selected_answer_id = form.cleaned_data[f'question_{current_question.id}']
            request.session['quiz_answers'][str(current_question.id)] = selected_answer_id

            if next_question_id is None:
                return redirect('quiz_result', quiz_id=quiz_id)
            else:
                return redirect('quiz', quiz_id=quiz_id, question_id=next_question_id)
        else:
            print(form.errors)
    else:
        form = QuizForm(questions=[current_question])

    # next_question = Question.objects.filter(quiz__id=quiz_id, id__gt=question_id).order_by('id').first()

    # context = {'quiz': quiz, 'question': question, 'next_question': next_question}
    context = {'quiz': quiz, 'form': form, 'question_id': question_id, 'total_questions': total_questions}
    return render(request, 'quiz_app/quiz/quiz.html', context)


def quiz_result(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    questions = quiz.question_set.all()
    total_questions = questions.count()
    score = 0

    for question in questions:
        selected_answer_id = request.session['quiz_answers'].get(str(question.id))
        if selected_answer_id:
            selected_answer = get_object_or_404(Answer, id=selected_answer_id)
            print(selected_answer)
            if selected_answer.is_correct:
                score += 1
    del request.session['quiz_answers']  # Clear the session after scoring

    context = {
        'quiz': quiz,
        'score': score,
        'total_questions': total_questions
    }
    return render(request, 'quiz_app/quiz/quiz_result.html', context)

@login_required(login_url='login')
def quiz_like(request, quiz_id):
    user = request.user
    quiz = get_object_or_404(Quiz, id=quiz_id)
    like, created = LikeQuiz.objects.get_or_create(user=user, quiz=quiz)
    if created:
        return JsonResponse({'status': 'success'})


@login_required(login_url='login')
def quiz_dislike(request, quiz_id):
    user = request.user
    like = get_object_or_404(LikeQuiz, user=user, quiz_id=quiz_id)
    like.delete()
    return JsonResponse({'status': 'success'})


@login_required(login_url='login')
def create_quiz(request):
    form = CreateQuizForm(request.POST or None)
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
        else:
            print(form.errors)
    context = {'form': form}
    return render(request, 'quiz_app/quiz/create/create_quiz.html', context)


@login_required(login_url='login')
def quiz_delete(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    try:
        quiz.delete()
        messages.success(request, f"{quiz.title} deleted successfuly")
    except Exception as e:
        messages.error(request, f"Error deleting quiz: {str(e)}")
    return redirect('home')


@login_required(login_url='login')
def quiz_question_delete(request, quiz_id, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        question.delete()
        messages.success(request, f"{question.content} deleted successfuly")
    except Exception as e:
        messages.error(request, f"Error deleting question: {str(e)}")
    return redirect('quiz_change', quiz_id=quiz_id)



@login_required(login_url='login')
def quiz_change(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    questions = Question.objects.filter(quiz=quiz)
    if request.method == "POST":
        new_title = request.POST.get('title')
        quiz.title = new_title
        quiz.save()
        return redirect('quiz_change', quiz_id=quiz.id)
    context = {'quiz': quiz, 'questions': questions}
    return render(request, 'quiz_app/quiz/quiz_change.html', context)


@login_required(login_url='login')
def quiz_change_question(request, quiz_id, question_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    question = get_object_or_404(Question, pk=question_id)
    answers = Answer.objects.filter(question=question)
    form_question = CreateQuestionForm(request.POST or None, request.FILES or None, instance=question)
    form_answer = CreateAnswerForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if request.POST.get('from-question') == "update_question":
            form_question = CreateQuestionForm(request.POST, request.FILES)
            if form_question.is_valid():
                question = form_question.save(commit=False)
                question.quiz = quiz
                question.content = form_question.cleaned_data['content']
                if 'content_image' in request.FILES:
                    question.content_image = request.FILES['content_image']
                question.save()
        elif request.POST.get('form-answer') == "update_answer":
            form_answer = CreateAnswerForm(request.POST, request.FILES)
            if form_answer.is_valid():
                answer = form_answer.save(commit=False)
                answer.question = question
                if 'content_image' in request.FILES:
                    answer.content_image = request.FILES['content_image']
                elif 'is_correct' in request.FILES:
                    answer.is_correct = request.FILES['is_correct']
                answer.save()
    context = {'quiz': quiz, 'question': question, 'answers': answers, 'form_question': form_question, 'form_answer': form_answer}
    return render(request, 'quiz_app/quiz/quiz_change_question.html', context)

@login_required(login_url='login')
def quiz_add_question(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    if request.method == "POST":
        form = CreateQuestionForm(request.POST, request.FILES)
        if form.is_valid():
            print("Form is valid")
            question = form.save(commit=False)
            question.quiz = quiz
            question.content = form.cleaned_data['content']
            if 'content_image' in request.FILES:
                question.content_image = request.FILES['content_image']
            question.save()
            return redirect('quiz_add_answer', quiz_id=quiz.id, question_id=question.id)
        else:
            print("Form is invalid")
            print(form.errors)
            print("POST data:", request.POST)
    else:
        form = CreateQuestionForm()
        form = CreateQuestionForm()
    context = {'quiz': quiz, 'question_form': form}
    return render(request, 'quiz_app/quiz/create/quiz_add_question.html', context)


def quiz_add_answer(request, quiz_id, question_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = CreateAnswerForm(request.POST, request.FILES)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            if 'content_image' in request.FILES:
                answer.content_image = request.FILES['content_image']
            elif 'is_correct' in request.FILES:
                answer.is_correct = request.FILES['is_correct']
            answer.save()
            return redirect('quiz_change', quiz_id=quiz.id)
        else:
            print("Form erros")
            print(form.errors)
            print("POST data:", request.POST)
    else:
        form = CreateAnswerForm()
    context = {'quiz': quiz, 'answer_form': form}
    return render(request, 'quiz_app/quiz/create/quiz_add_answer.html', context)


#user
def user_page(request, pk):
    user = User.objects.get(pk=pk)
    # user_avatar = UserProfile.objects.get(user=user.pk)
    user_avatar = "a"
    users_quizzes = Quiz.objects.filter(author=user)
    liked_quizzes = set(LikeQuiz.objects.filter(user__id=request.user.pk).values_list('quiz_id', flat=True))
    context = {'user': user, 'user_avatar': user_avatar, 'users_quizzes': users_quizzes, 'liked_quizzes': liked_quizzes}
    return render(request, 'quiz_app/user/user.html', context)


@login_required(login_url='login')
def user_liked(request, pk):
    user = User.objects.get(pk=pk)
    liked = LikeQuiz.objects.filter(user__id=pk).select_related('quiz')
    liked_quizzes = set(LikeQuiz.objects.filter(user__id=request.user.pk).values_list('quiz_id', flat=True))
    context = {'user': user, 'liked': liked, 'liked_quizzes': liked_quizzes}    
    return render(request, 'quiz_app/user/liked.html', context)


@login_required(login_url='login')
def user_change_username(request, pk):
    user = get_object_or_404(User, pk=pk)

    if request.method == "POST":
        new_username = request.POST.get("new-username")
        password = request.POST.get("password")
        names = User.objects.all()
        
        if check_password(password, user.password):
            user.username = new_username
            user.save()
            messages.success(request,   f"Username was successful changed to {new_username}")
        else:
            messages.error(request, "Incorect password")
    return redirect("user", pk=pk)


@login_required(login_url='login')
def user_change_email(request, pk):
    user = get_object_or_404(User, pk=pk)

    if request.method == "POST":
        new_email = request.POST.get('new-email')
        password = request.POST.get('password')

        if check_password(password, user.password):
            user.email = new_email
            user.save()
            messages.success(request, f"Email of {user.username} was successful changed to {new_email}")
        else:
            messages.error(request, "Incorect password or email")

    return redirect("user", pk=pk)


@login_required(login_url='login')
def user_change_passwrod(request, pk):
    user = get_object_or_404(User, pk=pk)

    if request.method == "POST":
        new_password = request.POST.get('new-password')
        new_password_repeated = request.POST.get('new-password-repeated')
        password = request.POST.get('password')
        if new_password == new_password_repeated:
            if check_password(password, user.password):
                user.set_password(new_password)
                user.save()
                messages.success(request, f"Passwrod of {user.username } was successful changed")
            else:
                messages.error(request, "Incorect old password or new password")
        else:
            messages.error(request, "Password isn't same")

    return redirect("user", pk=pk)










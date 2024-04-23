1. User settings(change username, email, password, avatar)
2. User profile 
3. Create a quiz +
4. Change a quiz
5. Use images as answer +
6. Search quiz +
7. Ratting system
8. Login/Sign in pages +
9. Like system
10. Take test
11. Quiz tags and description
12. Searching by tags


git add .

git commit -m "version of commit"

git branch -M main

git remote add origin https://github.com/Fialex1212/django-quiz_test.git

git push -u origin main

home.html

    {{ like_counts|get_item:quiz.id }}

quiz.html

    {{ answer.content }}
    {% if answer.content_image %}
        <img src="{{ answer.content_image.url }}" alt="{{ answer }}">
    {% endif %}
    {% if answer.is_correct %}(Correct){% endif %}


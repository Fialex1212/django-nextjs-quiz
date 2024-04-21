1. User settings(change username, email, password, avatar)
2. User profile 
3. Create a quiz
4. Change a quiz
5. Use images as answer +
6. Search quiz +
7. Ratting system
8. Login/Sign in pages +
9. Like system






echo "# django-quiz_test" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Fialex1212/django-quiz_test.git
git push -u origin main

home.html
{{ like_counts|get_item:quiz.id }}


1. User set up(change username, email, password, avatar)
2. Create a quiz
3. Change a quiz
4. Use imgages as answer +
5. Search quiz +
6. Ratting system
7. Create style for site +-
8. User profile






echo "# django-quiz_test" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Fialex1212/django-quiz_test.git
git push -u origin main

home.html
{{ like_counts|get_item:quiz.id }}


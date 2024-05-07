# Generated by Django 5.0.3 on 2024-05-07 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0018_alter_quiz_difficulty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='difficulty',
            field=models.IntegerField(choices=[('Easy', 'Easy'), ('Moderately Easy', 'Moderately Easy'), ('Intermediate', 'Intermediate'), ('Moderately Hard', 'Moderately Hard'), ('Hard', 'Hard')], default='Easy'),
        ),
    ]
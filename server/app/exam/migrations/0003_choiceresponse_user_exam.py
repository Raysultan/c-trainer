# Generated by Django 3.0.6 on 2020-06-13 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_sequenceresponse_user_exam'),
    ]

    operations = [
        migrations.AddField(
            model_name='choiceresponse',
            name='user_exam',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='exam.UserExam', verbose_name='UserExam'),
            preserve_default=False,
        ),
    ]

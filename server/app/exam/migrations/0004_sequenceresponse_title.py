# Generated by Django 3.0.6 on 2020-06-13 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0003_choiceresponse_user_exam'),
    ]

    operations = [
        migrations.AddField(
            model_name='sequenceresponse',
            name='title',
            field=models.CharField(default=1, max_length=214, verbose_name='Title'),
            preserve_default=False,
        ),
    ]

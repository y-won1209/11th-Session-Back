# Generated by Django 4.2 on 2023-05-04 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_hashtag'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='hashtag',
            field=models.ManyToManyField(to='blog.hashtag'),
        ),
    ]

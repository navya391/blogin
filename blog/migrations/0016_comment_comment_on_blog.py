# Generated by Django 3.2.3 on 2021-05-23 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_remove_comment_comment_on_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_on_blog',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='blog.blog'),
        ),
    ]
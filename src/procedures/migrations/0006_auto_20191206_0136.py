# Generated by Django 3.0 on 2019-12-06 01:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('procedures', '0005_auto_20191206_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='comment-files'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='like',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='contentstep',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='content-files'),
        ),
        migrations.DeleteModel(
            name='File',
        ),
    ]

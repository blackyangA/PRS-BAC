# Generated by Django 4.0.2 on 2022-04-15 15:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import middleware.current_user


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(upload_to='', verbose_name='上传文件')),
                ('is_public', models.IntegerField(choices=[(1, '公开'), (0, '不公开')], default=1, verbose_name='是否公开')),
                ('created_by', models.ForeignKey(default=middleware.current_user.get_current_user, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(default=middleware.current_user.get_current_user, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PulseRecognitionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('file_name', models.CharField(max_length=255, verbose_name='文件名')),
                ('results', models.CharField(choices=[(1, '是脉象数据'), (0, '不是脉象数据')], default=0, max_length=255, verbose_name='脉象识别结果')),
                ('created_by', models.ForeignKey(default=middleware.current_user.get_current_user, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(default=middleware.current_user.get_current_user, editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
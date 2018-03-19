# Generated by Django 2.0.3 on 2018-03-19 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='제목')),
                ('embed', models.CharField(blank=True, max_length=500, null=True, verbose_name='동영상 주소')),
                ('is_active', models.BooleanField(default=True, verbose_name='활성화 여부')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='생성일')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='수정일')),
            ],
        ),
    ]

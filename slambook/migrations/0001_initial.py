# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2020-12-11 23:29
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ans', models.BigIntegerField(blank=True)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CharacterTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cq_template', models.CharField(max_length=32)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('rmess', models.TextField(blank=True)),
                ('is_to', models.BooleanField(default=True)),
                ('response', models.BooleanField(default=False)),
                ('isreadgift', models.BooleanField(default=False)),
                ('contrib', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gto', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cquestion', models.TextField()),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typ', models.IntegerField()),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('cquestion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slambook.CQuestion')),
            ],
        ),
        migrations.CreateModel(
            name='GiftAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ans', models.BigIntegerField(blank=True)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('contrib', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slambook.Contributor')),
                ('cquestion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slambook.CQuestion')),
            ],
        ),
        migrations.CreateModel(
            name='GiftChart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('mess', models.TextField(blank=True)),
                ('giftmess', models.TextField(blank=True)),
                ('is_fr', models.BooleanField(default=True)),
                ('is_re', models.BooleanField(default=True)),
                ('fr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gfr', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Gifts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gift_name', models.CharField(max_length=32)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Group_User_Add',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RCTemplateCQuestions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('cquestion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slambook.CQuestion')),
                ('ctemplate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slambook.CharacterTemplate')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Slam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typ', models.IntegerField()),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('cquestion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slambook.CQuestion')),
            ],
        ),
        migrations.CreateModel(
            name='Slam_Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=32)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SlamChart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('mess', models.TextField(blank=True)),
                ('rmess', models.TextField(blank=True)),
                ('is_fr', models.BooleanField(default=True)),
                ('is_to', models.BooleanField(default=True)),
                ('response', models.BooleanField(default=False)),
                ('isreadslam', models.BooleanField(default=False)),
                ('fr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fr', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Slams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slam_name', models.CharField(max_length=32)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserExtension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateField(default=datetime.datetime(1900, 1, 1, 0, 0))),
                ('pro_pic', models.ImageField(blank=True, null=True, upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='slamchart',
            name='slam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slambook.Slams'),
        ),
        migrations.AddField(
            model_name='slamchart',
            name='to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='slam',
            name='slam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slambook.Slams'),
        ),
        migrations.AddField(
            model_name='slam',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='group_user_add',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slambook.Slam_Group'),
        ),
        migrations.AddField(
            model_name='group_user_add',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='giftchart',
            name='gift',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slambook.Gifts'),
        ),
        migrations.AddField(
            model_name='giftchart',
            name='re',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gre', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='gift',
            name='gift',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slambook.Gifts'),
        ),
        migrations.AddField(
            model_name='gift',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contributor',
            name='giftchart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gc', to='slambook.GiftChart'),
        ),
        migrations.AddField(
            model_name='answer',
            name='cquestion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slambook.CQuestion'),
        ),
        migrations.AddField(
            model_name='answer',
            name='slamchart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slambook.SlamChart'),
        ),
    ]

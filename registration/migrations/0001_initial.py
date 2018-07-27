# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-07-27 09:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mentee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(db_index=True, max_length=100)),
                ('middlename', models.CharField(blank=True, db_index=True, max_length=100)),
                ('lastname', models.CharField(db_index=True, max_length=100)),
                ('department', models.CharField(db_index=True, max_length=100)),
                ('roomno', models.IntegerField(db_index=True)),
                ('hostel', models.IntegerField(db_index=True)),
                ('contactno', models.IntegerField(db_index=True)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.IntegerField(db_index=True, primary_key=True, serialize=False)),
                ('code', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(default='Some String', max_length=200, unique=True)),
                ('discp', models.TextField(blank=True)),
                ('company', models.CharField(max_length=200)),
                ('designation', models.CharField(max_length=200)),
                ('available', models.BooleanField(default=True)),
                ('alloted', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-tags', '-id'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(db_index=True, max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='mentor',
            name='tags',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mentors', to='registration.Tag'),
        ),
    ]
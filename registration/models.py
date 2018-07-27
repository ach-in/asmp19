
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.urls import reverse

# Create your models here.

class Tag(models.Model):
	tag = models.CharField(max_length = 15, db_index=True)

	def __str__(self):
		return self.tag

class Mentor(models.Model):
	id=models.IntegerField(db_index=True, primary_key=True)
	code=models.CharField(max_length=200, db_index=True)
	slug=models.SlugField(max_length=200, unique=True, default="Some String", db_index=True)
	discp=models.TextField(blank=True)
	company=models.CharField(max_length=200)
	designation=models.CharField(max_length=200)
	tags=models.ForeignKey(Tag, related_name='mentors')
	available=models.BooleanField(default=True)
	alloted=models.BooleanField(default=False)
	created=models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-tags','-id']

	def get_tags(self):
		return ', '.join([elem.tag for elem in self.tags.all()])

	def __unicode__(self):
		return self.code

	def get_absolute_url(self):
		return reverse('mentors:mentor_detail', args=[self.id, self.slug])

class Mentee(models.Model):
	firstname = models.CharField(max_length=100, db_index=True, blank=False)
	middlename = models.CharField(max_length=100, db_index=True, blank=True)
	lastname = models.CharField(max_length=100, db_index=True, blank=False)
	department = models.CharField(max_length=100, db_index=True, blank=False)
	roomno = models.IntegerField(db_index=True, blank=False)
	hostel = models.IntegerField(db_index=True, blank=False)
	contactno = models.IntegerField(db_index=True, blank=False)
	available=models.BooleanField(default=True)

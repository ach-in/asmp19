# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.urls import reverse
import csv, io
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Tag(models.Model):
	tag = models.CharField(max_length = 15, db_index=True)

	def __str__(self):
		return self.tag

class Mentor(models.Model):
	id=models.IntegerField(db_index=True, primary_key=True, default = "1")
	code=models.CharField(max_length=200, db_index=True)
	slug=models.SlugField(max_length=200, unique="True", default=False, db_index=True)
	hostel=models.CharField(max_length=20, default=False)
	discp=models.TextField(blank=True)
	company=models.CharField(max_length=200)
	designation=models.CharField(max_length=200)
	year=models.CharField(max_length=20, default="2018")
	degree=models.CharField(max_length=100, default="BTech")
	city=models.CharField(max_length=100, default="Mumbai")
	department=models.CharField(max_length=100, default="Civil")
	tags=models.ForeignKey(Tag, related_name='mentors', default=False)
	available=models.BooleanField(default=True)
	alloted=models.BooleanField(default=False)
	created=models.DateTimeField(auto_now_add=True)
	# def update_user_profile(self,sender, instance, created, **kwargs):
	# 	with open('registration/YeLeAchin.csv') as csvfile:
	# 		reader = csv.reader(csvfile)
	# 		next(reader, None)  
	# 		for row in reader:
	# 			_, created = Mentor.objects.create(
	# 				id = row[0],
	# 				code = row[1],
	# 				department = row[2],
	# 				# tags = row[3],
	# 				degree = row[4],
	# 				hostel = row[5],
	# 				year = row[6],
	# 				city = row[7],
	# 				designation = row[9],
	# 				company = row[10],
	# 				discp = row[11],
	# 			)
	# 			print(Mentor.objects.discp)
	# 			# if created:
	# 			# 	Mentor.objects.create(user=instance)
	# 			# 	instance.mentor.save()
	class Meta:
		ordering = ['-tags','-id']

	def get_tags(self):
		return ', '.join([elem.tag for elem in self.tags.all()])

	def __unicode__(self):
		return self.code

	def get_absolute_url(self):
		return reverse('registration:mentor_detail', args=[self.id, self.slug])

@receiver(post_save, sender = User)
def update_user_profile(sender, instance, created, **kwargs):
	with open('registration/YeLeAchin.csv') as csvfile:
			reader = csv.reader(csvfile)
			i=0
			next(reader, None)  
			for row in reader:
				i = i+1
				_, created1 = Tag.objects.get_or_create(
					defaults = None,
					tag = row[3],
					)
				if created1:
					Tag.objects.create
					instance.save()
				tag = Tag.objects.get(tag = row[3])	
				_, created = Mentor.objects.get_or_create(
					defaults = None,
					id = row[0],
					slug = row[0],
					code = row[1],
					department = row[2],
					tags = tag,
					degree = row[4],
					hostel = row[5],
					year = row[6],
					city = row[7],
					designation = row[9],
					company = row[10],
					discp = row[11],
				)
				if created:
					# Mentor.get_tags
					Mentor.objects.create
					instance.save()
				if i>100:
					break
				# _, created1 = Tag.objects.get_or_create(
				# 	defaults = None,
				# 	tag = row[3],
				# 	)
				# if created1:
				# 	Tag.objects.create
				# 	instance.save()			
					
# @receiver(post_save, sender = Tag)
# def update_user_profile1(sender, instance, created, **kwargs):
# 	with open('registration/YeLeAchin.csv') as csvfile:
# 			reader = csv.reader(csvfile)
# 			next(reader, None)  
# 			for row in reader:
# 				_, created = Tag.objects.create(
# 					# tag = row[3],
# 					)
# 				if created:
# 					Tag.objects.create(user=instance)
# 					instance.tag.save()
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models

# Create your models here.
from registration.models import Mentor
User = settings.AUTH_USER_MODEL


class Cart(models.Model):
	user = models.ForeignKey(User, null = True, blank = True)
	mentors = models.ManyToManyField(Mentor, blank = True)
	total = models.IntegerField(default = 0)
	timestamp = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)

	def __str__(self):
		return str(self.id)

	
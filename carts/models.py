# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from registration.models import Mentor
from django.db.models.signals import pre_save, post_save, m2m_changed

# Create your models here.
User = settings.AUTH_USER_MODEL

class CartManager(models.Manager):
	def new_or_get(self, request):
		cart_id = request.session.get("cart_id", None)
		qs = self.get_queryset().filter(id = cart_id)
		if qs.count() == 1 :
			new_obj = False
			cart_obj = qs.first()
			if request.user.is_authenticated() and cart_obj.user is None:
				cart_obj.user = request.user
				cart_obj.save()
		else:
			cart_obj = Cart.objects.new(user=request.user)
			new_obj = True
			request.session['cart_id'] = cart_obj.id
		return cart_obj, new_obj
	
	def new(self, user = None):
		user_obj = None
		if user is not None:
			if user.is_authenticated():
				user_obj = user
		return self.model.objects.create(user = user_obj)

class Cart(models.Model):
	user = models.ForeignKey(User, null = True, blank = True)
	mentors = models.ManyToManyField(Mentor, blank = True)
	total = models.IntegerField(default = 0)
	timestamp = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
	objects = CartManager()

	def __str__(self):
		return str(self.id)

def pre_save_cart_receiver(sender, instance, action, *args, **kwargs)	:
	if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
		mentors = instance.mentors.all()
		total = 0
		for i in mentors:
			total  = total + 1
		print (total)
		instance.total = total
		instance.save()

m2m_changed.connect(pre_save_cart_receiver, sender = Cart.mentors.through)
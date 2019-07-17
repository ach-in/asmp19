# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .models import Cart
from registration.models import Mentor
# Create your views here.

def cart_home(request):

	cart_obj, new_obj = Cart.objects.new_or_get(request)
	print(cart_obj.mentors.all())
	return render(request, "cart.html", {"cart": cart_obj})

def cart_update(request):
	print(request.POST)
	mentor_id = request.POST.get("mentor")
	print(mentor_id)
	if mentor_id is not None:
		try:
			mentor_obj = Mentor.objects.get(id=mentor_id)
		except Mentor.DoesNotExist:
			print("Product is gone")
			return redirect("registration:cart_home")
		cart_obj, new_obj = Cart.objects.new_or_get(request)
		if mentor_obj in cart_obj.mentors.all():
			cart_obj.mentors.remove(mentor_obj)
		else:
			cart_obj.mentors.add(mentor_obj)
		# cart_obj.mentors.add(mentor_id)
		# return redirect(mentor_obj.get_absolute_url()) 
	return redirect("registration:cart_home")

	
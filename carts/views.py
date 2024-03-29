# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Cart
# Create your views here.

def cart_create(user = None):
	cart_obj = Cart.objects.create(user = None)
	print ("New Cart Created")
	return cart_obj

def cart_home(request):
	# print(request.session)
	# del request.session['cart_id']
	request.session['cart_id'] = 12
	cart_id = request.session.get("cart_id", None)
	
	qs = Cart.objects.filter(id = cart_id)	
	if qs.count() == 1 :
		cart_obj = qs.first()
		print('Cart ID exists')
	else:
		cart_obj = cart_create()
		request.session['cart_id'] = cart_obj.id
	cart_obj = Cart.objects.get(id = cart_id)
	return render(request, "cart.html", {})
	
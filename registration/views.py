# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Mentor, Tag

appname = 'registration'

def registration(request):
	return render(request, 'registration.html')

def mentor_list(request, tag_slug=None):
	if request.method == "GET":
		tags = Tag.objects.all()
		all_mentors = Mentor.objects.all().filter(available=True).order_by('alloted')
		return render(request, 'main.html',{'all_mentors':all_mentors})

def analytics(request):

	all_mentors = Mentor.objects.filter(tags__tag__startswith='Analytics').order_by('alloted')
	return render(request, 'main.html',{'all_mentors':all_mentors})

def finance(request):
	if request.method == "GET":
		all_mentors = Mentor.objects.filter(tags__tag__startswith='Finance').order_by('alloted')
		return render(request, 'main.html',{'all_mentors':all_mentors})

def consult(request):
	if request.method == "GET":
		all_mentors = Mentor.objects.filter(tags__tag__startswith='Consult').order_by('alloted')
		return render(request, 'main.html',{'all_mentors':all_mentors})

def management(request):

        all_mentors = Mentor.objects.filter(tags__tag__startswith='Management').order_by('alloted')
        return render(request, 'main.html',{'all_mentors':all_mentors})

def Research(request):

        all_mentors = Mentor.objects.filter(tags__tag__startswith='Research').order_by('alloted')
        return render(request, 'main.html',{'all_mentors':all_mentors})

def analytics(request):

        all_mentors = Mentor.objects.filter(tags__tag__startswith='Analytics').order_by('alloted')
        return render(request, 'main.html',{'all_mentors':all_mentors})

def mentor_detail(request, id, slug):
	mentor = get_object_or_404(Mentor, id=id, slug=slug, available=True)
	return render(request, 'detail.html',{'mentor':mentor})

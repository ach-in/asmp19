# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Mentor, Tag
import csv, io

# with open('registration/YeLeAchin.csv') as csvfile:
# 		reader = csv.reader(csvfile)
# 		next(reader, None)  
# 		for row in reader:
# 			all_mentors, created = Mentor.objects.update_or_create(
# 				id = row[0],
# 				code = row[1],
# 				department = row[2],
# 				tags = row[3],
# 				degree = row[4],
# 				hostel = row[5],
# 				year = row[6],
# 				city = row[7],
# 				designation = row[9],
# 				company = row[10],
# 				discp = row[11],
# 			)

def registration(request):
	return render(request, 'registration.html')

def mentor_list(request, tag_slug=None):
	if request.method == "GET":
		tags = Tag.objects.all()
		all_mentors = Mentor.objects.filter(available=True).order_by('alloted')
		return render(request, 'mentorlist.html',{'all_mentors':all_mentors})

def analytics(request):
	all_mentors = Mentor.objects.filter(tags__tag__startswith='Analytics').order_by('alloted')
	# all_mentors = all_mentors.filter(tags__tag__startswith='Analytics').order_by('alloted')
	return render(request, 'mentorlist.html',{'all_mentors':all_mentors})

def finance(request):
	if request.method == "GET":
		all_mentors = Mentor.objects.filter(tags__tag__startswith='Finance').order_by('alloted')
		return render(request, 'mentorlist.html',{'all_mentors':all_mentors})

def management(request):
	if request.method == "GET":
		all_mentors = Mentor.objects.filter(tags__tag__startswith='Management').order_by('alloted')
		return render(request, 'mentorlist.html',{'all_mentors':all_mentors})

def manageconsult(request):
	if request.method == "GET":
		all_mentors = Mentor.objects.filter(tags__tag__startswith='ManageConsult').order_by('alloted')
		return render(request, 'mentorlist.html',{'all_mentors':all_mentors})

def core(request):
	if request.method == "GET":
		all_mentors = Mentor.objects.filter(tags__tag__startswith='Core').order_by('alloted')
		return render(request, 'mentorlist.html',{'all_mentors':all_mentors})

def strategyconsult(request):
	if request.method == "GET":
		all_mentors = Mentor.objects.filter(tags__tag__startswith='Strategy consulting').order_by('alloted')
		return render(request, 'mentorlist.html',{'all_mentors':all_mentors})

def civilservice(request):
	if request.method == "GET":
		all_mentors = Mentor.objects.filter(tags__tag__startswith='Civil Services/Govt. of').order_by('alloted')
		return render(request, 'mentorlist.html',{'all_mentors':all_mentors})

def designno(request):
	if request.method == "GET":
		all_mentors = Mentor.objects.filter(tags__tag__startswith='Design').order_by('alloted')
		return render(request, 'mentorlist.html',{'all_mentors':all_mentors})

def research(request):
	if request.method == "GET":
		all_mentors = Mentor.objects.filter(tags__tag__startswith='Research').order_by('alloted')
		return render(request, 'mentorlist.html',{'all_mentors':all_mentors})

def infotech(request):
	if request.method == "GET":
		all_mentors = Mentor.objects.filter(tags__tag__startswith='IT').order_by('alloted')
		return render(request, 'mentorlist.html',{'all_mentors':all_mentors})

def mentor_detail(request, id, slug):
	mentor = get_object_or_404(Mentor, id=id, slug=slug, available=True)
	return render(request, 'detail.html',{'mentor':mentor})

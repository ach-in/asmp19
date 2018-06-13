# -*- codin	g: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.
app_name='team'

def team(request):
	return render(request, 'team.html')
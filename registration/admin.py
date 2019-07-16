
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Mentor, Tag

class MentorAdmin(admin.ModelAdmin):
	"""docstring for MentorAdmin"""
	list_display= ['id','code','tags','discp','hostel','company','designation','created','alloted','available']
	list_filter= ['available','tags']
	list_editable= ['available','alloted']		
admin.site.register(Mentor, MentorAdmin)

class TagAdmin(admin.ModelAdmin):
	list_display = ['tag']
admin.site.register(Tag,TagAdmin)


from django.contrib import admin
from .models import User, Project, Like, Notice
from datetime import date
import datetime
import csv
from django.http import HttpResponse
import os

def download_csv(modeladmin, request, queryset):    
	today = str(date.today())

	# local writing and download
	if os.path.isfile("{}(EUC-KR).csv".format(today)):
		fE = open("{}(EUC-KR).csv".format(today), "a", encoding='EUC-KR')
		fU = open("{}(UTF-8).csv".format(today), "a", encoding='UTF-8')
		now = str(datetime.datetime.now())
		writerE = csv.writer(fE)
		writerU = csv.writer(fU)
		writerE.writerow(["{}".format(now)])
		writerU.writerow(["{}".format(now)])
		writerE.writerow(['date', 'major', 'studentId', 'name', 'comment'])
		writerU.writerow(['date', 'major', 'studentId', 'name', 'comment'])
		for q in queryset:
			writerE.writerow([q.date, q.major, q.studentId, q.name, q.comment])
			writerU.writerow([q.date, q.major, q.studentId, q.name, q.comment])
		fE.close()
		fU.close()
	else:
		fE = open("{}(EUC-KR).csv".format(today), "w", encoding='EUC-KR')
		fU = open("{}(UTF-8).csv".format(today), "w", encoding='UTF-8')
		writerE = csv.writer(fE)
		writerU = csv.writer(fU)
		writerE.writerow(["{}".format(now)])
		writerU.writerow(["{}".format(now)])
		writerE.writerow(['date', 'major', 'studentId', 'name', 'comment'])
		writerU.writerow(['date', 'major', 'studentId', 'name', 'comment'])
		for q in queryset:
			writerE.writerow([q.date, q.major, q.studentId, q.name, q.comment])
			writerU.writerow([q.date, q.major, q.studentId, q.name, q.comment])
		fE.close()
		fU.close()
	
	# download by admin side
	response = HttpResponse(open('{}(UTF-8).csv'.format(today), 'rt',encoding='UTF-8').read())
	response['Content-Type']='text/csv'
	response['Content-Disposition'] = 'attachment; filename={}(UTF-8).csv'.format(today)
	return response

# admin customizing
@admin.register(User) # decorator 형태로 등록
class StoryAdmin(admin.ModelAdmin):
	list_display = ['date', 'major', 'studentId', 'name', 'comment']
	actions = [download_csv]

@admin.register(Project)
class StoryAdmin(admin.ModelAdmin):
	list_display = ['title', 'lecture', 'group', 'groupName', 'members', 'description', 'pdf', 'video', 'likeCount']

@admin.register(Like)
class StoryAdmin(admin.ModelAdmin):
	list_display = ['userId', 'projectId']

@admin.register(Notice)
class StoryAdmin(admin.ModelAdmin):
	list_display = ['title', 'contents', 'date']
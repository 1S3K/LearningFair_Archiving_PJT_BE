from django.contrib import admin
from .models import User, Project, Like, Notice

# admin customizing
@admin.register(User) # decorator 형태로 등록
class StoryAdmin(admin.ModelAdmin):
	list_display = ['date', 'major', 'studentId', 'name', 'comment']

@admin.register(Project)
class StoryAdmin(admin.ModelAdmin):
	list_display = ['title', 'lecture', 'group', 'groupName', 'members', 'description', 'pdf', 'video', 'likeCount']

@admin.register(Like)
class StoryAdmin(admin.ModelAdmin):
	list_display = ['userId', 'projectId']

@admin.register(Notice)
class StoryAdmin(admin.ModelAdmin):
	list_display = ['title', 'contents', 'date']
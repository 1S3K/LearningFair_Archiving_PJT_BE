from django.db import models
from django.utils import timezone

class User(models.Model):
    studentId = models.CharField(max_length=10, null=False) # 학번
    name = models.CharField(max_length=15, null=False) # 이름

class Project(models.Model):
    title = models.CharField(max_length=30, null=False) # 프로젝트 제목
    lecture = models.CharField(max_length=3, null=False) # 분반
    group = models.IntegerField(null=False) # 분반 내 각 팀
    groupName = models.CharField(max_length=30, null=False)
    members = models.CharField(max_length=100, null=False) # 프로젝트 멤버
    description = models.TextField(null=False)  # 프로젝트 설명
    pdf = models.TextField()    # PDF 파일 경로
    video = models.TextField()  # Video 파일 경로
    likeCount = models.IntegerField(default=0)  # 좋아요 수

class Like(models.Model):
    userId = models.TextField(null=False)   # 유저 고유 ID
    projectId = models.TextField(null=False)    # 프로젝트 고유 ID

class Notice(models.Model):
    title = models.CharField(max_length=50) # 제목
    contents = models.TextField(null=False) # 내용
    date = models.DateTimeField(default=timezone.now, null=False) # 작성일


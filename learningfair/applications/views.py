from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse, HttpResponse

from .modules import resMessage, statusCode, success, fail
from django.views.decorators.csrf import csrf_exempt

from datetime import date
from .models import Project, Notice, Like
import logging
import time
import json


logger = logging.getLogger('django')
insa = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13']
jagwa = ['41', '42', '43', '44', 'i1', 'i2']


# GET /hotprojcets
# 각 캠퍼스별로 인기플젝 3개 조회
@csrf_exempt
def hotprojects(req):
    if req.method != 'GET':
        return JsonResponse(fail(statusCode['BAD_REQUEST'], resMessage['BAD_REQUEST']), status=statusCode['BAD_REQUEST'])

    try:
        insa_projects = Project.objects.filter(lecture__in=insa).order_by('-likeCount')[:3]
        jagwa_projects = Project.objects.filter(lecture__in=jagwa).order_by('-likeCount')[:3]

        data = {
            'insa':list(insa_projects.values()),
            'jagwa':list(jagwa_projects.values())
        }

        return JsonResponse(success(statusCode['OK'], resMessage['SUCCESS'], data))
    except Exception as err:
        print('hotprojects ERROR : ' + err)
        return JsonResponse(fail(statusCode['DB_ERROR'], resMessage['DB_ERROR']))


# GET /lectures/02/projects
# 02분반 프로젝트 조회
# query : page, sortBy
def lectures(req, lecture_id):
    page = int(req.GET.get('page'))  # 1 2 3 4 -> 0~9 10~19 20~29 30~39
    sortBy = req.GET.get('sortBy')
    if sortBy == 'likes':
        projects = Project.objects.filter(lecture=lecture_id).order_by('-likeCount')[(page - 1) * 10:page * 10]
        project_list = serializers.serialize('json', projects)
        return HttpResponse(project_list, content_type="text/json")
    else:
        projects = Project.objects.filter(lecture=lecture_id)[(page - 1) * 10:page * 10]
        project_list = serializers.serialize('json', projects)
        return HttpResponse(project_list, content_type="text/json")


# GET /projects?searchBy='머신러닝'
# 프로젝트 전체에서 '머신러닝' 검색결과 조회
def projects(req):
    searchBy = req.GET.get('searchBy')
    if searchBy:
        projects = Project.objects.filter(title__contains=searchBy)
        project_list = serializers.serialize('json', projects)
        return HttpResponse(project_list, content_type="text/json")
    else:
        projects = Project.objects.all()
        project_list = serializers.serialize('json', projects)
        return HttpResponse(project_list, content_type="text/json")


# GET /notices
# 공지사항 조회
def notices(req):
    notices = Notice.objects.all()
    notice_list = serializers.serialize('json', notices)
    return HttpResponse(notice_list, content_type="text/json")


# POST /projects/:project_id/likes
# DELETE /projects/:project_id/likes
def project_likes(req, project_id):
    if req.method == 'POST':
        # TODO : 좋아요 증가 처리
        return JsonResponse({'status': f'{project_id} 좋아요 성공'})
    elif req.method == 'DELETE':
        # TODO : 좋아요 삭제 처리
        return JsonResponse({'status': f'{project_id} 좋아요삭제 성공'})
    else:
        return JsonResponse({'status': '유효하지 않은 접근'})


# GET? POST? 둘 중 하나 고르자 /login
def login(req, student_id):
    # TODO : 로그파일에 기록 남기기
    logger.info(student_id)
    return JsonResponse({'status': f"{student_id} 학생 로그남기기 성공"})

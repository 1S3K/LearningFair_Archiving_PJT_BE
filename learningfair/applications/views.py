from django.shortcuts import render
from django.http import JsonResponse

from .modules import resMessage, statusCode, success, fail
from django.views.decorators.csrf import csrf_exempt

from datetime import date
from .models import Project, Notice, Like
import logging
import time
import json


logger = logging.getLogger('django')
insa = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13']
jagwa_icam = ['41', '42', '43', '44', 'i1', 'i2']


# GET /hotprojcets
# 각 캠퍼스별로 인기플젝 3개 조회
@csrf_exempt
def hotprojects(req):
    if req.method != 'GET':
        return JsonResponse(fail(statusCode['BAD_REQUEST'], resMessage['BAD_REQUEST']), status=statusCode['BAD_REQUEST'])

    try:
        insa_projects = Project.objects.filter(lecture__in=insa).order_by('-likeCount')[:3]
        jagwa_icam_projects = Project.objects.filter(lecture__in=jagwa_icam).order_by('-likeCount')[:3]

        data = {
            'insa':list(insa_projects.values()),
            'jagwa_icam':list(jagwa_icam_projects.values())
        }

        return JsonResponse(success(statusCode['OK'], resMessage['SUCCESS'], data), status=statusCode['OK'])
    except Exception as err:
        print('hotprojects ERROR : ' + err)
        return JsonResponse(fail(statusCode['DB_ERROR'], resMessage['DB_ERROR']), status=statusCode['DB_ERROR'])


# GET /lectures/02/projects
# 02분반 프로젝트 조회
@csrf_exempt
def lectures(req, lecture_id):
    if req.method != 'GET':
        return JsonResponse(fail(statusCode['BAD_REQUEST'], resMessage['BAD_REQUEST']), status=statusCode['BAD_REQUEST'])
    
    try:
        projects = Project.objects.filter(lecture=lecture_id).order_by('group')
        data = list(projects.values())
        return JsonResponse(success(statusCode['OK'], resMessage['SUCCESS'], data), status=statusCode['OK'])
    except Exception as err:
        print('lectures ERROR : ' + err)
        return JsonResponse(fail(statusCode['DB_ERROR'], resMessage['DB_ERROR']), status=statusCode['DB_ERROR'])


# GET /projects?searchBy='머신러닝'
# 프로젝트 전체에서 '머신러닝' 검색결과 조회
@csrf_exempt
def projects(req):
    if req.method != 'GET':
        return JsonResponse(fail(statusCode['BAD_REQUEST'], resMessage['BAD_REQUEST']), status=statusCode['BAD_REQUEST'])

    searchBy = req.GET.get('searchBy')
    try:
        if searchBy:
            projects = Project.objects.filter(title__contains=searchBy).order_by('group')
            data = list(projects.values())
        else:
            data = []
        
        return JsonResponse(success(statusCode['OK'], resMessage['SUCCESS'], data), status=statusCode['OK'])
    
    except Exception as err:
        print('lectures ERROR : ' + err)
        return JsonResponse(fail(statusCode['DB_ERROR'], resMessage['DB_ERROR']), status=statusCode['DB_ERROR'])


# GET /notices
# 공지사항 조회
@csrf_exempt
def notices(req):
    if req.method != 'GET':
        return JsonResponse(fail(statusCode['BAD_REQUEST'], resMessage['BAD_REQUEST']), status=statusCode['BAD_REQUEST'])

    try:
        notices = Notice.objects.all()
        data = list(notices.values())
        return JsonResponse(success(statusCode['OK'], resMessage['SUCCESS'], data), status=statusCode['OK'])
    
    except Exception as err:
        print('notices ERROR : ' + err)
        return JsonResponse(fail(statusCode['DB_ERROR'], resMessage['DB_ERROR']), status=statusCode['DB_ERROR'])


# POST /projects/:project_id/likes
# DELETE /projects/:project_id/likes
@csrf_exempt
def project_likes(req, project_id):
    if req.method == 'POST':
        # TODO : 좋아요 증가 처리
        return JsonResponse(success(statusCode['OK'], resMessage['LIKE_CANCEL_SUCCESS']), status=statusCode['OK'])
    elif req.method == 'DELETE':
        # TODO : 좋아요 삭제 처리
        return JsonResponse(success(statusCode['OK'], resMessage['LIKE_CANCEL_SUCCESS']), status=statusCode['OK'])
    else:
        return JsonResponse(fail(statusCode['BAD_REQUEST'], resMessage['BAD_REQUEST']), status=statusCode['BAD_REQUEST'])


# POST /login
@csrf_exempt
def login(req):
    # TODO : 로그파일에 기록 남기기
    logger.info(student_id)
    return JsonResponse({'status': f"{student_id} 학생 로그남기기 성공"})

from django.shortcuts import render
from django.http import JsonResponse

from .modules import resMessage, statusCode, success, fail
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.forms.models import model_to_dict

from .models import Project, Notice, Like, User
import json


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


# POST /lectures/02/projects/02/like
# DELETE /lectures/02/projects/02/like
# body엔 userInfo가 들어감.
@csrf_exempt
def project_likes(req, lecture_id, group_id):
    try:
        if req.method == 'POST':
            project = Project.objects.get(lecture=lecture_id, group=group_id)
            project.likeCount += 1
            project.save()
            data = model_to_dict(project)
            return JsonResponse(success(statusCode['OK'], resMessage['LIKE_SUCCESS'], data), status=statusCode['OK'])
        elif req.method == 'DELETE':
            project = Project.objects.get(lecture=lecture_id, group=group_id)
            project.likeCount -= 1
            project.save()
            data = model_to_dict(project)
            return JsonResponse(success(statusCode['OK'], resMessage['LIKE_CANCEL_SUCCESS'], data), status=statusCode['OK'])
        else:
            return JsonResponse(fail(statusCode['BAD_REQUEST'], resMessage['BAD_REQUEST']), status=statusCode['BAD_REQUEST'])
    except Exception as err:
        print('project_likes ERROR : ' + err)
        return JsonResponse(fail(statusCode['DB_ERROR'], resMessage['DB_ERROR']), status=statusCode['DB_ERROR'])


# POST /login
@csrf_exempt
def login(req):
    if req.method != 'POST':
        return JsonResponse(fail(statusCode['BAD_REQUEST'], resMessage['BAD_REQUEST']), status=statusCode['BAD_REQUEST'])
    try:
        info = json.loads(req.body)
        new_user = User(studentId=info['studentId'], name=info['name'], comment=info['comment'], major=info['major'])
        new_user.save()
        return JsonResponse(success(statusCode['CREATED'], resMessage['SUCCESS'], model_to_dict(new_user)), status=statusCode['CREATED'])
    except Exception as err:
        print('project_likes ERROR : ' + err)
        return JsonResponse(fail(statusCode['DB_ERROR'], resMessage['DB_ERROR']), status=statusCode['DB_ERROR'])  

'''
<로그인 방식 둘 중에 어떤거 택할것인가>
1. 학번값이 db에 들어가고 로그에 저장되며, 좋아요 처리 시 '학번' '타임스탬프' '게시물' 이 좋아요 정보로 저장되며, answerCount += 1 된다. 다음에 똑같은 학번으로 로그인시, 프로젝트 리스트 조회시 isClicked 값 또한 들어가 좋아요를 했는지에 대한 정보가 저장된다.
2. 학번값은 로그에만 저장되며, 그냥 좋아요 누를때마다 answerCount += 1 된다.

=> 학번은
'''
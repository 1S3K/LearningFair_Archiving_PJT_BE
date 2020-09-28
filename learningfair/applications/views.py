from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from datetime import date
from .models import Project

# json response 테스트 view
def test(req):
    projects = Project.objects.filter()
    project_list = serializers.serialize('json', projects)
    return HttpResponse(project_list, content_type="text/json")

# GET /hotprojcets
# 인기플젝 3개 조회
def hotprojects(req):
    projects = Project.objects.all().order_by('-likeCount')[:3]
    project_list = serializers.serialize('json', projects)
    return HttpResponse(project_list, content_type="text/json")

# GET /lectures/02/projects
# 02분반 프로젝트 조회
# query : page, sortBy
def lectures(req, lecture_id):
    page = req.GET.get('page')
    sortBy = req.GET.get('sortBy')
    projects = Project.objects.filter()
    data = {
        'lecture_id': lecture_id,
        'page':page,
        'sortBy':sortBy,
    }
    return JsonResponse(data)

# GET /projects?searchBy='머신러닝'
# 프로젝트 전체에서 '머신러닝' 검색결과 조회
def projects(req):
    searchBy = req.GET.get('searchBy')
    projects = Project.objects.filter(title__contains=searchBy)
    project_list = serializers.serialize('json', projects)
    return HttpResponse(project_list, content_type="text/json")

# GET /notices
# 공지사항 조회
def notices(req):
    data = {
        '1':{
            'title':'공지1',
            'contents':'공지내용1',
            'date':date(2020,1,1)
        },
        '2':{
            'title':'공지1',
            'contents':'공지내용1',
            'date':date(2020,2,1)
        },
        '3':{
            'title':'공지1',
            'contents':'공지내용1',
            'date':date(2020,3,1)
        }
    }
    return JsonResponse(data)

# POST /projects/:project_id/likes
# DELETE /projects/:project_id/likes
def project_likes(req, project_id):
    if req.method == 'POST':
        # TODO : 좋아요 증가 처리
        return JsonResponse({'status':f'{project_id} 좋아요 성공'})
    elif req.method == 'DELETE':
        # TODO : 좋아요 삭제 처리
        return JsonResponse({'status':f'{project_id} 좋아요삭제 성공'})
    else:
        return JsonResponse({'status':'유효하지 않은 접근'})

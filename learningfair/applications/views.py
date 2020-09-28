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
    # TODO : db에서 좋아요 많은 플젝 3개 찾기
    data = {
        '1': {
            'title':'인기많은플젝',
            'campus':1,
            'lecture':1,
            'groupNumber':1,
            'groupName':'그룹1',
            'members':['멤버1','멤버2','멤버3'],
            'description':'그룹1 플젝입니다',
            'pdf':'해당피디에프아이디',
            'description':'프로젝트 설명설명',
            'video':'비디오 아이디',
            'likeCount':100
        },
        '2':{
            'title':'두번째로인기많은플젝',
            'campus':2,
            'lecture':2,
            'groupNumber':2,
            'groupName':'그룹2',
            'members':['멤버1','멤버2','멤버3'],
            'description':'그룹2 플젝입니다',
            'pdf':'해당피디에프아이디',
            'description':'프로젝트 설명설명',
            'video':'비디오 아이디',
            'likeCount':10
        },
        '3':{
            'title':'세번째로인기많은플젝',
            'campus':3,
            'lecture':3,
            'groupNumber':3,
            'groupName':'그룹3',
            'members':['멤버1','멤버2','멤버3'],
            'description':'그룹3 플젝입니다',
            'pdf':'해당피디에프아이디',
            'description':'프로젝트 설명설명',
            'video':'비디오 아이디',
            'likeCount':1
        },
    }
    return JsonResponse(data)

# GET /lectures/02/projects
# 02분반 프로젝트 조회
# query : page, sortBy
def lectures(req, lecture_id):
    page = req.GET.get('page')
    sortBy = req.GET.get('sortBy')
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

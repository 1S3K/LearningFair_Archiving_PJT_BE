from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from datetime import date
from .models import Project, Notice, Like

# GET /hotprojcets
# 인기플젝 3개 조회
# TODO : 캠퍼스별로 상위 3개 보내주기 (총 9개, 금방함)
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
    # TODO : pagination 추가
    if sortBy == 'likes':
        projects = Project.objects.filter(lecture=lecture_id).order_by('-likeCount')
        project_list = serializers.serialize('json', projects)
        return HttpResponse(project_list, content_type="text/json")
    else:
        projects = Project.objects.filter(lecture=lecture_id)
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
        return JsonResponse({'status':f'{project_id} 좋아요 성공'})
    elif req.method == 'DELETE':
        # TODO : 좋아요 삭제 처리
        return JsonResponse({'status':f'{project_id} 좋아요삭제 성공'})
    else:
        return JsonResponse({'status':'유효하지 않은 접근'})

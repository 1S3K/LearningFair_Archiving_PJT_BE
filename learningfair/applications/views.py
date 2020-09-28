from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from datetime import date
from .models import Project, Notice, Like



insa = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13']
jagwa = ['41', '42', '43', '44']
icam = ['i1', 'i2']

# GET /hotprojcets
# 각 캠퍼스별로 인기플젝 3개 조회
def hotprojects(req):
    insa_projects = Project.objects.filter(lecture__in=insa).order_by('-likeCount')[:3]
    jagwa_projects = Project.objects.filter(lecture__in=jagwa).order_by('-likeCount')[:3]
    icam_projects = Project.objects.filter(lecture__in=icam).order_by('-likeCount')[:3]
    insa_project_list = serializers.serialize('json', insa_projects)
    jagwa_project_list = serializers.serialize('json', jagwa_projects)
    icam_project_list = serializers.serialize('json', icam_projects)
    project_list = insa_project_list + jagwa_project_list + icam_project_list
    return HttpResponse(project_list, content_type="text/json")

# GET /lectures/02/projects
# 02분반 프로젝트 조회
# query : page, sortBy
def lectures(req, lecture_id):
    page = int(req.GET.get('page')) # 1 2 3 4 -> 0~9 10~19 20~29 30~39
    sortBy = req.GET.get('sortBy')
    if sortBy == 'likes':
        projects = Project.objects.filter(lecture=lecture_id).order_by('-likeCount')[(page-1)*10:page*10]
        project_list = serializers.serialize('json', projects)
        return HttpResponse(project_list, content_type="text/json")
    else:
        projects = Project.objects.filter(lecture=lecture_id)[(page-1)*10:page*10]
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

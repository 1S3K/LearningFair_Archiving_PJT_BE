from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Project

# json response 테스트 view
def test(req):
    projects = Project.objects.filter()
    project_list = serializers.serialize('json', projects)
    return HttpResponse(project_list, content_type="text/json")


def hotprojects(req):
    # db에서 찾기
    data = {
        '1':{
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

def classes(req):
    pass

def projects(req):
    pass

def notices(req):
    pass

def project_likes(req):
    pass

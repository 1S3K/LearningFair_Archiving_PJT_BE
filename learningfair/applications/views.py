from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

# /hotprojcets
# 인기플젝 3개 조회
def hotprojects(req):
    # TODO : db에서 좋아요 많은 플젝 3개 찾기
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

# /lectures/02/projects
# 02분반 프로젝트 조회

# TODO : 쿼리스트링 : page, sortBy=likes
def lectures(req, lecture_id):
    page = req.GET.get('page')
    sortBy = req.GET.get('sortBy')
    data = {
        'lecture_id': lecture_id,
        'page':page,
        'sortBy':sortBy,
    }
    return JsonResponse(data)

# /projects
def projects(req):
    pass

def notices(req):
    pass

def project_likes(req):
    pass

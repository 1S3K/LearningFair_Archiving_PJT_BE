from django.urls import path
from . import views

app_name = 'applications'

urlpatterns = [
    path('hotprojects', views.hotprojects, name='hotprojects'),
    path('lectures/<lecture_id>/projects', views.lectures, name='lecture_projects'),
    path('projects', views.projects, name='projects'),
    path('notices', views.notices, name='notices'),
    path('lectures/<lecture_id>/groups/<group_id>/like', views.project_likes, name='edit_likes'),
    path('login', views.login, name='login')
]

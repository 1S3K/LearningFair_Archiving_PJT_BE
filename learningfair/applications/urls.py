from django.urls import path
from . import views

app_name = 'applications'

urlpatterns = [
    path('hotprojects', views.hotprojects, name='hotprojects'),
    path('classes/<class_id>/projects', views.classes, name='class_projects'),
    path('projects', views.projects, name='projects'),
    path('notices', views.notices, name='notices'),
    path('projects/<project_id>/likes', views.project_likes, name='edit_likes')
]

from django.urls import path

from . import views

app_name = "pdfdocx"

urlpatterns = [
    path('', views.index, name='index'),
    path('upload', views.upload, name='upload'),
    path('file_name',views.switch_docx,name = 'switch_docx'),
]
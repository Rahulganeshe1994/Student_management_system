
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index),
    path('user', views.user),
    path('courses', views.courses),
    path('student', views.student),
    path('teacher', views.teacher),
    path('dashboard/', views.dashboard),
    path('student', views.student),
    path('login', views.login),
    path('signup',views.signup),
    path('addcourses', views.addcourses),
    path('delete', views.delete),
    path('updatecourse', views.updatecourse),
    path('addstudent', views.addstudent),
    path('allstudent', views.allstudent),
    path('deletestudent', views.deletestudent),
    path('searchstudent', views.searchstudent),
    path('addteacher', views.addteacher),
    path('deleteteacher', views.deleteteacher),
    path('updateteacher/<int:uid>/', views.updateteacher),
    path('searchteacher', views.searchteacher),
    path('update_teacher/', views.update_teacher),
    path('logout', views.logout),

]

from django.urls import path
from .api import (UserModelView, UserModelView1, CourseModelView, CourseModelView1,StudentModelView,
                  StudentModelView1, TeacherModelView, TeacherModelView1, LoginView)


urlpatterns = [
    path('userapi/',UserModelView.as_view()),
    path('userapi/<int:pk>/',UserModelView1.as_view()),
    path('courseapi/',CourseModelView.as_view()),
    path('courseapi/<int:pk>/',CourseModelView1.as_view()),
    path('studentapi/', StudentModelView.as_view()),
    path('studentapi/<int:pk>/', StudentModelView1.as_view()),
    path('teacherapi/', TeacherModelView.as_view()),
    path('teacherapi/<int:pk>/',TeacherModelView1.as_view()),
    path('login/',LoginView.as_view()),
] 

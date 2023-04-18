from django.shortcuts import render,redirect
from django.contrib.auth.hashers import check_password,make_password
from django.contrib import messages
from django.contrib import auth
from .models import Courses
from .models import User
from .models import Student
from .models import Teacher
from django.db.models import Q
def index(request):
   return render(request,'index.html') 

def courses(request):
    data=Courses.objects.all()
    return render(request, 'courses.html',{'data':data})

def student(request):
    data=Courses.objects.all()
    studentdata=Student.objects.all()
    return render(request, 'viewstudents.html',{'data':data,'studentdata':studentdata})

def dashboard(request):
    return render(request,'dashboard.html')
def signup(request):
    return render(request,'sign-up.html')
def teacher(request):
    teacher=Teacher.objects.all()
    return render(request,'teacher.html',{'teacher':teacher})


def updateteacher(request, uid):
    teachers = Teacher.objects.get(id=uid)
    return render(request, 'updateteacher.html', context={'teachers': teachers})

def user(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        password=make_password(request.POST['password'])
        if User.objects.filter(email=email).exists():
            messages.error(request,'This Email Is Alredy Exists')
            return redirect('/')
        else:
            user=User.objects.create(name=name,email=email,password=password)
            user.save()
            return redirect('/')
def login(request):
    if request.method=="POST":
        email=request.POST['email']
        Password=request.POST['password']
        if User.objects.filter(email=email).exists():
            us=User.objects.get(email=email)
            password=us.password
            if check_password(Password,password):
              return render(request,'dashboard.html')
            else:
               messages.error(request," Password is invalid")
               return redirect('/')
        else:
           messages.error(request,'Email is Invalid')
           return redirect('/')
    else:
        return redirect('/')
    
    
def addcourses(request):
        course=request.POST['course']
        duration = request.POST['duration']
        text=request.POST['text']
        fees=request.POST['fees']
        fees=int(fees)
        if Courses.objects.filter(Courses_name=course).exists():
            messages.info(request,'Course Alredy exists')
            data=Courses.objects.all()
            return render(request,"Courses.html",{"data":data})
        else:
            Courses.objects.create(Courses_name=course, Courses_duration=duration, Courses_textbox=text, Courses_fees=fees)
            messages.success(request,"Suucessfully Added Course")
            data=Courses.objects.all()
            return render(request,'Courses.html',{'data':data})
        
        
def delete(request):
    id=request.GET['id']
    Courses.objects.filter(id=id).delete()
    data=Courses.objects.all()
    return render(request,'Courses.html',{'data':data})


def updatecourse(request):
    id=request.POST['id']
    c=Courses.objects.get(id=id)
    c.Courses_name=request.POST['course']
    c.Courses_duration = request.POST['duration']
    c.Courses_fees = request.POST['fees']
    c.Courses_textbox = request.POST['text']
    c.save()
    data=Courses.objects.all()
    return render(request,'Courses.html',{'data':data})

def addstudent(request):
    s=Student()
    s.student_name=request.POST['sname']
    s.student_email=request.POST['semail']
    s.student_mobile = request.POST['smobile']
    s.student_college=request.POST['scollege']
    s.student_degree=request.POST['sdegree']
    sid=request.POST['scourse']
    s.Courses_name=Courses.objects.get(id=sid)
    s.save()
    studentdata=Student.objects.all()
    data=Courses.objects.all()
    return render(request,'viewstudents.html',{'studentdata':studentdata,'data':data})


def allstudent(request):
    s=Student()
    s.id=request.POST['id']
    s.student_name=request.POST['tname']
    s.student_email=request.POST['temail']
    s.student_mobile=request.POST['tmobile']
    s.student_college=request.POST['tcollege']
    s.student_degree=request.POST['tdegree']
    usid=request.POST['course']
    s.Courses_name=Courses.objects.get(id=usid)
    s.save()
    studentdata = Student.objects.all()
    data=Courses.objects.all()
    return render(request,'viewstudents.html',{'data':data,'studentdata':studentdata})


def deletestudent(request):
    did=request.GET['stud']
    Student.objects.filter(id=did).delete()
    studentdata = Student.objects.all()
    data=Courses.objects.all()
    return render(request,'viewstudents.html',{'data':data ,'studentdata':studentdata})


def searchstudent(request):
    name=request.POST['name']
    s=Student.objects.filter(Q(student_email=name) | Q(student_name=name) | Q(student_college=name) | Q(student_degree=name)).all()
    return render(request,'viewstudents.html',{'studentdata':s})


def totalfields(request):
    data=Courses.objects.all()
    x=Courses.objects.all().count()
    y = Student.objects.all().count()
    z=Teacher.objects.all().count()
    return render(request,'dashboard.html',{'data':data,'x':x,'y':y,'z':z})


def addteacher(request):
    teacher_name=request.POST['tname']
    teacher_email = request.POST['temail']
    teacher_phone= request.POST['tphone']
    teacher_joining = request.POST['tdate']
    teacher_education = request.POST['teducation']
    teacher_id = request.POST['tid']
    teacher_work_exp = request.POST['texp']
    teacher_packeg = request.POST['tpackeg']
    if Teacher.objects.filter(teacher_name=teacher_name).exists():
        messages.info(request,'Teacher is already registerd')
        return render(request,'teacher.html')
    elif Teacher.objects.filter(teacher_email=teacher_email).exists():
        messages.info(request,'Teachere is alredy registerd')
        return render(request,'teacher.html')
    else:
        Teacher.objects.create(teacher_name=teacher_name,teacher_email=teacher_email,teacher_phone=teacher_phone,teacher_joining=teacher_joining,teacher_education=teacher_education,teacher_id=teacher_id,teacher_work_exp=teacher_work_exp,teacher_packeg=teacher_packeg)
        teacher=Teacher.objects.all()
        return render(request,'teacher.html',{'teacher':teacher})

def deleteteacher(request):
    id=request.GET['tid'] 
    Teacher.objects.filter(id=id).delete()
    teacher=Teacher.objects.all()
    return render(request,'teacher.html',{'teacher':teacher})

def searchteacher(request):
    name = request.POST['tname']
    s=Teacher.objects.filter(Q(teacher_name=name) | Q(teacher_email=name)).all()
    return render(request,'teacher.html',{'teacher':s})

def update_teacher(request):
    t=Teacher()
    t.id = request.POST['uid']
    t.teacher_name=request.POST['ttname']
    t.teacher_email=request.POST['ttemail']
    t.teacher_phone= request.POST['ttphone']
    t.teacher_joining = request.POST['ttdate']
    t.teacher_education = request.POST['tteducation']
    t.teacher_id = request.POST['ttid']
    t.teacher_work_exp = request.POST['ttexp']
    t.teacher_packeg = request.POST['ttpackeg']
    t.save()
    teacher=Teacher.objects.all()
    return render(request,'teacher.html',{'teacher':teacher})
def lgout(request):
    auth.logout(request)
    return render(request,'sign-up.html')









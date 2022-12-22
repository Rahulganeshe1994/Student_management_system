from django.db import models
class User(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=500,blank=True,null=True)
    is_active=models.BooleanField(default=True)
class Courses(models.Model):
    Courses_name=models.CharField(max_length=200)
    Courses_fees = models.CharField(max_length=200)
    Courses_duration= models.CharField(max_length=200)
    Courses_textbox = models.TextField()
    is_active=models.BooleanField(default=True)
    def __str__(self) -> str:
        return self.Courses_name
class Student(models.Model):
    student_name=models.CharField(max_length=200)
    student_email= models.CharField(max_length=200)
    student_mobile= models.IntegerField()
    student_college = models.CharField(max_length=200)
    student_degree= models.CharField(max_length=200)
    Courses_name = models.ForeignKey(Courses,on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
class Teacher(models.Model):
    teacher_name=models.CharField(max_length=200)
    teacher_email=models.CharField(max_length=200)
    teacher_phone = models.IntegerField()
    teacher_joining = models.DateField()
    teacher_education = models.CharField(max_length=200)
    teacher_id= models.CharField(max_length=200)
    teacher_work_exp= models.CharField(max_length=200)
    teacher_packeg = models.CharField(max_length=200)
    is_active=models.BooleanField(default=True)
    def __str__(self) -> str:
        return self.teacher_name




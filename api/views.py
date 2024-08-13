from django.shortcuts import render
from rest_framework.views import APIView
from student.models import Student
from teacher.models import Teacher
from class_periods.models import ClassPeriod
from classes.models import Classes
from course.models import Course
from .serializers import StudentSerializer
from .serializers import TeacherSerializer
from .serializers import ClassPeriodSerializer
from .serializers import CourseSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        lastname = request.query_params.get("lastname")
        email = request.query_params.get("email")
        if lastname:
            students=students.filter(lastname=lastname)
            if email:
                email=email.filter(email=email)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class ClassPeriodListView(APIView):
    def get(self, request):
        class_period = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(class_period, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = ClassPeriodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class CourseListView(APIView):
    def get(self, request):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    
class ClassesListView(APIView):
    def get(self, request):
        classes = Classes.objects.all()
        serializer = ClassesSerializer(classes, many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = ClassesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
    
class StudentDetailView(APIView):
    def get(self,request,id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)  
    def email_student(self,student,course_id):
        course =Course.objects.get(id=course_id)
        student.course.add(course)
    def post(self,request,id):
        student = Student.objects.get(id=id)
        action=request.data.get("action")
        if action(email):
            course_id=request.data.get("course")
            self.email_student(student,course_id)
        return Response(status.HTTP_201_CREATED)
    def put(self,request,id):
        student =Student.objects.get(id=id)
        serializer = StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        student = Student.objects.get(id=id)
        student.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
class TeacherDetailView(APIView):
    def get(self,request,id):
            teacher = Teacher.objects.get(id=id)
            serializer = TeacherSerializer(teacher)
            return Response(serializer.data)    
    def put(self,request,id):
        teacher =Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teacher,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        teacher = Teacher.objects.get(id=id)
        teacher.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
class ClassPeriodDetailView(APIView):
    def get(self,request,id):
            class_period = Teacher.objects.get(id=id)
            serializer = TeacherSerializer(class_period)
            return Response(serializer.data)    
    def put(self,request,id):
        class_period =ClassPeriod.objects.get(id=id)
        serializer = ClassPeriodSerializer(class_period,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        class_period = Teacher.objects.get(id=id)
        class_period.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
class CourseDetailView(APIView):
    def get(self,request,id):
            course = Course.objects.get(id=id)
            serializer = CourseSerializer(course)
            return Response(serializer.data)    
    def put(self,request,id):
        course =Course.objects.get(id=id)
        serializer = CourseSerializer(course,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        course = Course.objects.get(id=id)
        course.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

class ClassesDetailView(APIView):
    def get(self,request,id):
            classes = Classes.objects.get(id=id)
            serializer = ClassesSerializer(classes)
            return Response(serializer.data)    
    def put(self,request,id):
        classes =Classes.objects.get(id=id)
        serializer = ClassesSerializer(classes,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        classes = Teacher.objects.get(id=id)
        classes.delete()
        return Response(status=status.HTTP_202_ACCEPTED)    



           
    
    
    

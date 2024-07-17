from django.shortcuts import render
from rest_framework.views import APIView
from student.models import Student
from teacher.models import Teacher
from classPeriod.models import ClassPeriod
from course.models import Course
from .serializers import StudentSerializer
from .serializers import TeacherSerializer
from .serializers import ClassPeriodSerializer
from .serializers import CourseSerializer
from rest_framework.response import Response
# Create your views here.
class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
class ClassPeriodListView(APIView):
    def get(self, request):
        classPeriod = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(classPeriod, many=True)
        return Response(serializer.data)
class CourseListView(APIView):
    def get(self, request):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)    
class ClassListView(APIView):
    def get(self, request):
        classes = Class.objects.all()
        serializer = CourseSerializer(classes, many=True)
        return Response(serializer.data)        
    
    
    

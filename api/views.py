from django.shortcuts import render
from rest_framework.views import APIView
from student.models import Student
from teacher.models import Teacher
from class_periods.models import ClassPeriod
from classes.models import Classes
from course.models import Course
from .serializers import StudentSerializer
from .serializers import TeacherSerializer
from .serializers import  ClassesSerializer
from .serializers import ClassPeriodSerializer
from .serializers import CourseSerializer
from rest_framework.response import Response
from rest_framework import status
from datetime import timedelta
from django.utils import timezone
from .serializers import MinimalStudentSerializer
from .serializers import (
    StudentSerializer, MinimalStudentSerializer,
    ClassesSerializer, MinimalClassesSerializer,
    ClassPeriodSerializer, MinimalClassPeriodSerializer,
    CoursesSerializer, MinimalCoursesSerializer,
    TeacherSerializer, MinimalTeacherSerializer
)

# Create your views here.
class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        lastname = request.query_params.get("first_name")
        if lastname:
            students = students.filter(first_name=lastname)
        serializer = MinimalStudentSerializer(students, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = MinimalTeacherSerializer(teachers, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ClassPeriodListView(APIView):
    def get(self, request):
        class_periods = ClassPeriod.objects.all()
        serializer = MinimalClassPeriodSerializer(class_periods, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = ClassPeriodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class CourseListView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = MinimalCoursesSerializer(courses, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = CoursesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
class ClassesListView(APIView):
    def get(self, request):
        classes = Classes.objects.all()
        serializer = MinimalClassesSerializer(classes, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = ClassesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class StudentDetailView(APIView):
    def get(self, request, id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    def put(self, request, id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        student = Student.objects.get(id=id)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def post(self, request, id):
        student = Student.objects.get(id=id)
        action = request.data.get("action")
        if action == "enroll":
            course_id = request.data.get("course")
            self.enroll_student(student, course_id)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    def enroll_student(self, student, course_id):
        course = Course.objects.get(id=course_id)
        student.courses.add(course)
    
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
    def post(self, request):
        serializer = ClassPeriodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
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
    def post(self, request, id):
        course = Course.objects.get(id=id)
        action = request.data.get("action")
        if action == "assign_teacher":
            teacher_id = request.data.get("teacher")
            teacher = Teacher.objects.get(id=teacher_id)
            course.teacher.add(teacher)
            return Response({"status": "teacher assigned"}, status=status.HTTP_201_CREATED)
        return Response({"error": "invalid action"}, status=status.HTTP_400_BAD_REQUEST)

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
    def post(self, request, id):
        classes = Classes.objects.get(id=id)
        action = request.data.get("action")
        if action == "add_student":
            student_id = request.data.get("student")
            student = Student.objects.get(id=student_id)
            classes.students.add(student)
            return Response({"status": "student added"}, status=status.HTTP_201_CREATED)
        return Response({"error": "invalid action"}, status=status.HTTP_400_BAD_REQUEST)     


class WeeklyTimetableView(APIView):
    def get(self, request):
        now = timezone.now()
        start_of_week = now - timedelta(days=now.weekday())
        end_of_week = start_of_week + timedelta(days=6)
        timetable_data = {
            "start_of_week": start_of_week.isoformat(),
            "end_of_week": end_of_week.isoformat(),
        }
        return Response(timetable_data, status=status.HTTP_200_OK)       
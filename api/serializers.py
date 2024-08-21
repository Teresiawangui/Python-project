from rest_framework import serializers
from student.models import Student
from teacher.models import Teacher
from course.models import Course
from class_periods.models import ClassPeriod
from classes.models import Classes

class StudentSerializer(serializers.ModelSerializer):
   class Meta:
     model = Student
     fields = "__all__"
class MinimalStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Student
        fields = ["lastname"]      
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model= Teacher
        fields = "__all__"
class MinimalTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ["id", "name"]        
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model= Course
    fields = "__all__"
class MinimalCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "name"]
class ClassPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model= ClassPeriod
        fields ="__all__"
class MinimalClassPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassPeriod
        fields = ["id", "start_time", "end_time"]        
class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model= Classes
        fields ="__all__"
class MinimalClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = ["id", "name"]

       
    
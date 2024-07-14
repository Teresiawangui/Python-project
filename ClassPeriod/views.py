from django.shortcuts import render

# Create your views here.

from .models import ClassPeriod
from .serializers import ClassPeriodSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class ClassPeriod(APIView):
    def get(self,request):
        students = ClassPeriodSerializer(students,many = True)
        return Response(serializer.data)
    


from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Subject, Course
from .serializers import SubjectSerializer


class SubjectListAPIView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer



class SubjectDetailAPIView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer



class CourseEnrollAPIView(APIView):
    def post(self, request, pk, format=None):
        course = get_object_or_404(Course, pk=pk)
        course.students.add(request.user)
        return Response({'enrolled': True})

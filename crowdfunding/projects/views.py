from django.shortcuts import render
from rest_framework.views import APIView #added
from rest_framework.response import Response #added
from django.http import Http404

from rest_framework import status, generics
from .models import Project, Pledge #added
from .serializers import ProjectSerializer, PledgeSerializer, ProjectDetailSerializer #added

# Create your views here. #https://ccbv.co.uk/ # https://www.cdrf.co/ # https://www.cdrf.co/3.13/rest_framework.views/APIView.html

# models > serializers > views > project urls > crowdfunding urls

# the below is templatey / boilerplate... you would change the word Project from below code to suit the new app
# eg: ProjectList to Pledge list
# PROJECT will always be long form
# PLEDGE will be the same, but the shortcut way
class ProjectList(APIView):
    
    def get(self, request):
        projects = Project.objects.all() # retrieves list of all projects
        serializer = ProjectSerializer(projects, many=True) #tell it to do many because list
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data) # serialise data for me
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# above is the same as:
# class ProjectList(generics.ListCreateAPIView):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer

class ProjectDetail(APIView):

    def get_object(self, pk): #this pk is arbitrary 
        try:
            return Project.objects.get(pk=pk) #primary key = the value we have been given. pk from the url will be parsed to this as the variable
        except Project.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data) #allows adding pk to urls

class PledgeList(generics.ListCreateAPIView):
    queryset = Pledge.objects.all()
    serializer_class = PledgeSerializer

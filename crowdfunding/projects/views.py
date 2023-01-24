from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from django.http import Http404

from rest_framework import status, generics, permissions
from .models import Project, Pledge 
from .serializers import ProjectSerializer, PledgeSerializer, ProjectDetailSerializer , PledgeDetailSerializer
from .permissions import IsOwnerOrReadOnly, IsSupporterOrReadOnly

# Create your views here. 
# References:
# https://ccbv.co.uk/ # https://www.cdrf.co/ # https://www.cdrf.co/3.13/rest_framework.views/APIView.html
class ProjectList(APIView): # long form version / template
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] # only logged in users can create new projects
    
    def get(self, request):
        projects = Project.objects.all() # retrieves list of all projects
        serializer = ProjectSerializer(projects, many=True) #tell it to do many because list
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data) # serialize data for me
        if serializer.is_valid():
            serializer.save(owner=request.user) #add the owner to overcome error when adding project [missing owner]
            # owner is readonly - cannot create the object
            # serializer wont work because it wasn't given an owner and cannot do this
            # add an owner serializer (Readonly)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# above is the same as:
# class ProjectList(generics.ListCreateAPIView):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer

class ProjectDetail(APIView): #same as project, but shortcut - uses same boilerplate [quicker]
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get_object(self, pk): #this pk is arbitrary
        try:
            project = Project.objects.get(pk=pk) #primary key = the value we have been given. pk from the url will be parsed to this as the variable
            self.check_object_permissions(self.request, project)
            return project
        except Project.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data) #allows adding pk to urls
    
    def put(self, request, pk): # added to correspond with update project serializer
        project = self.get_object(pk)
        data = request.data
        serializer = ProjectDetailSerializer(
            instance=project,
            data=data,
                partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class PledgeList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Pledge.objects.all()
    serializer_class = PledgeSerializer

    def perform_create(self, serializer): # added to remove the need to input a supporter {automates to logged in user}
        serializer.save(supporter=self.request.user)

class PledgeDetailView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsSupporterOrReadOnly]
    queryset = Pledge.objects.all()
    serializer_class = PledgeDetailSerializer
    
    # https://www.cdrf.co/3.13/rest_framework.generics/RetrieveUpdateAPIView.html
    def put(self, request, pk): # copied from project serializer
        return self.update(request,pk)



'''
    FLOW:
    
    projects app > crowdfunding settings > project models > make / migrate > project serializers > project views > project urls > Crowdfunding urls
    
    USERS:
    user app > crowdfunding settings > user models > make / migrate > project models > make / migrate > create superuser > user serializer > user view > user urls > crowdfunding urls

    Permissions:
    project views > project serializers > project views > project permissions > project views
'''

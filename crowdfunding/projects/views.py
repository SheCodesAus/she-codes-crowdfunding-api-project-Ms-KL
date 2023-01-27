from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from rest_framework import status, generics, permissions
from .models import Project, Pledge
from .serializers import ProjectSerializer, PledgeSerializer, ProjectDetailSerializer , PledgeDetailSerializer
from .permissions import IsOwnerOrReadOnly, IsSupporterOrReadOnly

from rest_framework.exceptions import NotFound
from django.db import IntegrityError #unique = True handling

class ProjectList(APIView): # long form version / template
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] # only logged in users can create new projects

    def get(self, request):
        projects = Project.objects.all() # retrieves list of all projects
        serializer = ProjectSerializer(projects, many=True) #tell it to do many because list

        if not projects:
            return Response({"message": "Sorry, no tree-hugging projects here!"}, status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data) # serialize data for me
        if serializer.is_valid():
            try:
                serializer.save(owner=request.user)
                # add the owner to overcome error when adding project [missing owner]
                # owner is readonly - cannot create the object
                # serializer wont work because it wasn't given an owner and cannot do this
                # add an owner serializer (Readonly)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except IntegrityError: #responding to unique field
                return Response({"error":"This Project title already exists. Please enter another."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# NOTE: above is the same as:
    # class ProjectList(generics.ListCreateAPIView):
    #     queryset = Project.objects.all()
    #     serializer_class = ProjectSerializer

class ProjectDetail(APIView):
    #same as project, but shortcut - uses same boilerplate [quicker]
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get_object(self, pk): #this pk is arbitrary
        try:
            project = Project.objects.get(pk=pk)
            #primary key = the value we have been given. pk from the url will be parsed to this as the variable
            self.check_object_permissions(self.request, project)
            return project
        except Project.DoesNotExist:
            raise NotFound("Sorry, no Tree-Hugging project here!")

    #---- TODO: >>>> can get_object and get be combined?

    def get(self, request, pk):
        # project = self.get_object(pk)
        # serializer = ProjectDetailSerializer(project)
        # return Response(serializer.data) #allows adding pk to urls
        try:
            project = Project.objects.get(pk=pk)
            self.check_object_permissions(request, project)
            serializer = ProjectDetailSerializer(project)
            return Response(serializer.data)
        except Project.DoesNotExist:
            raise NotFound("Sorry, no tree-hugger project here!")

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

    def delete(self, request, pk):
        project = self.get_object(pk)
        project.delete()
        return Response("Project Deleted", status=status.HTTP_204_NO_CONTENT)

class PledgeList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Pledge.objects.all()
    serializer_class = PledgeSerializer

    def perform_create(self, serializer): # added to remove the need to input a supporter {automates to logged in user}
        serializer.save(supporter=self.request.user)

    def get(self, request):
        pledges = self.get_queryset()
        if not pledges:
            return Response({"message": "Sorry, no tree-huggers here! Pick a project and send a pledge to get things started!"}, status=status.HTTP_204_NO_CONTENT)

        serializer = self.get_serializer(pledges, many=True)
        return Response(serializer.data)

class PledgeDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsSupporterOrReadOnly]
    queryset = Pledge.objects.all()
    serializer_class = PledgeDetailSerializer

    def handle_exception(self, exc):
        '''
        REFERENCES:
            - https://stackoverflow.com/questions/51836535/django-rest-framework-custom-message-for-404-errors
            - http://www.tomchristie.com/rest-framework-2-docs/tutorial/3-class-based-views
            - https://www.cdrf.co/3.1/rest_framework.generics/RetrieveUpdateDestroyAPIView.html
        '''
        if isinstance(exc, Http404):
            return Response({'data': 'Sorry, no tree-hugging here!'},
            status=status.HTTP_404_NOT_FOUND)
        return super(PledgeDetailView, self).handle_exception(exc)


'''
    References:
    - https://ccbv.co.uk/
    - https://www.cdrf.co/
    - https://www.cdrf.co/3.13/rest_framework.views/APIView.html
    - https://docs.djangoproject.com/en/3.2/ref/models/fields/#django.db.models.Field.unique

    FLOW:

    projects app > crowdfunding settings > project models > make / migrate > project serializers > project views > project urls > Crowdfunding urls

    USERS:
    user app > crowdfunding settings > user models > make / migrate > project models > make / migrate > create superuser > user serializer > user view > user urls > crowdfunding urls

    Permissions:
    project views > project serializers > project views > project permissions > project views
'''

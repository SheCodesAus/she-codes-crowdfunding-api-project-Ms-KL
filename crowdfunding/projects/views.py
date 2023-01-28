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

from django_filters.rest_framework import DjangoFilterBackend

class ProjectList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filterset_fields = ['is_open', 'owner']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        # auto adds userid as owner

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        # serialize data for me
        if serializer.is_valid():
            try:
                serializer.save(owner=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except IntegrityError:
                #responding to unique field
                return Response({"error":"This Project title already exists. Please enter another."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer

    def handle_exception(self, exc):
        if isinstance(exc, Http404):
            return Response({'data': 'Sorry, no tree-hugging here!'},
            status=status.HTTP_404_NOT_FOUND)
        return super(ProjectDetail, self).handle_exception(exc)

class PledgeList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Pledge.objects.all()
    serializer_class = PledgeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('supporter', 'project')

    def perform_create(self, serializer):
        # added to remove the need to input a supporter {automates to logged in user}
        serializer.save(supporter=self.request.user)

class PledgeDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsSupporterOrReadOnly]
    queryset = Pledge.objects.all()
    serializer_class = PledgeDetailSerializer

    def handle_exception(self, exc):
        if isinstance(exc, Http404):
            return Response({'data': 'Sorry, no tree-hugging here!'},
            status=status.HTTP_404_NOT_FOUND)
        return super(PledgeDetailView, self).handle_exception(exc)

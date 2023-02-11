from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from rest_framework import status, generics, permissions, renderers
from .models import Project, Pledge, Comment
from .serializers import ProjectSerializer, PledgeSerializer, ProjectDetailSerializer , PledgeDetailSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly, IsSupporterOrReadOnly, IsCommenterOrReadOnly

from rest_framework.exceptions import NotFound
from django.db import IntegrityError #unique = True handling

from django_filters.rest_framework import DjangoFilterBackend

#-- API-Root Config
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from users.models import CustomUser
from users.serializers import CustomUserSerializer

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

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(commenter=self.request.user)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsCommenterOrReadOnly]

@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "projects": reverse("project-list", request=request, format=format),
            "comments": reverse("comment-list", request=request, format=format),
            "pledges": reverse("pledge-list", request=request, format=format),
            "users": reverse("customuser-list", request=request, format=format),
        }
    )

# https://www.django-rest-framework.org/tutorial/5-relationships-and-hyperlinked-apis/
# https://stackoverflow.com/a/49393797

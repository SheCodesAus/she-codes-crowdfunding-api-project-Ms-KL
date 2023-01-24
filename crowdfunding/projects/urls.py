# models > serializers > views > urls(self) > crowdfunding urls
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('projects/', views.ProjectList.as_view(), name="project-list"), # naming convention
    path('projects/<int:pk>/', views.ProjectDetail.as_view(), name="project-detail"),
    path('pledges/', views.PledgeList.as_view(), name="pledge-list"),
    path('pledges/<int:pk>/', views.PledgeDetailView.as_view(), name="pledge-detail"),
]

url_patterns = format_suffix_patterns(urlpatterns)
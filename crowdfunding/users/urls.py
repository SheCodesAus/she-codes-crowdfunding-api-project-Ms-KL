from django.urls import path

from . import views

# to use the new user view add the urls 

urlpatterns = [
    path('', views.CustomUserList.as_view(), name='customuser-list'),
    path('<int:pk>/', views.CustomUserDetail.as_view(), name='customuser-detail'),

]

'''
    FLOW:
    
    projects app > crowdfunding settings > project models > make / migrate > project serializers > project views > project urls > Crowdfunding urls
    
    user app > crowdfunding settings > user models > make / migrate > project models > make / migrate > create superuser > user serializer > user view > user urls > crowdfunding urls
    
'''
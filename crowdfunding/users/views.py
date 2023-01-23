# from django.shortcuts import render
# used for templates / HTML

# # Create your views here.

from django.http import Http404
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status, generics, permissions

from .models import CustomUser
from .serializers import CustomUserSerializer, ChangePasswordSerializer


class CustomUserList(APIView):

    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)
        #same as project
    
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class CustomUserDetail(APIView):

    def get_object(self,pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
    
    # copied from projects > views.py > project detail > def put
    def put(self, request, pk):
        user = self.get_object(pk)
        data = request.data # this is dict. need to add restriction to password change here as updated password does not hash from here
        data.pop('password', None) # if a password is added to the json file to be PUT, it will remove it so it doesn't update
        serializer = CustomUserSerializer(
            instance = user,
            data=data,
                partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)



# class ChangePasswordView(UpdateAPIView):
#         """
#         An endpoint for changing password.
#         """
#         serializer_class = ChangePasswordSerializer
#         model = User
#         permission_classes = (IsAuthenticated,)

#         def get_object(self, queryset=None):
#             obj = self.request.user
#             return obj

#         def update(self, request, *args, **kwargs):
#             self.object = self.get_object()
#             serializer = self.get_serializer(data=request.data)

#             if serializer.is_valid():
#                 # Check old password
#                 if not self.object.check_password(serializer.data.get("old_password")):
#                     return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
#                 # set_password also hashes the password that the user will get
#                 self.object.set_password(serializer.data.get("new_password"))
#                 self.object.save()
#                 response = {
#                     'status': 'success',
#                     'code': status.HTTP_200_OK,
#                     'message': 'Password updated successfully',
#                     'data': []
#                 }

'''
    FLOW:
    
    projects app > crowdfunding settings > project models > make / migrate > project serializers > project views > project urls > Crowdfunding urls
    
    user app > crowdfunding settings > user models > make / migrate > project models > make / migrate > create superuser > user serializer > user view > user urls > crowdfunding urls
    
'''
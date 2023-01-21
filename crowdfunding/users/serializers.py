from rest_framework import serializers
from .models import CustomUser

# class CustomUserSerializer(serializers.Serializer):
#     id = serializers.ReadOnlyField()
#     username = serializers.CharField(max_length=150)
#     # cling data (clean data - check to see if username is email)
#     email = serializers.EmailField()
#     # added 21/1 below
#     is_active = serializers.BooleanField()

    # def create(self, validated_data):
    #     return CustomUser.objects.create(**validated_data)
    #     # what is **validated_data

# CONVERT TO MODEL SERIALIZER
# https://www.django-rest-framework.org/api-guide/serializers/#additional-keyword-arguments
# 
class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password')
    
    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

'''
TODO: change password, validate changes

https://studygyaan.com/django/django-rest-framework-tutorial-change-password-and-reset-password

https://www.grepper.com/tpc/django+rest+framework+serializer+hash+password

https://stackoverflow.com/questions/38845051/how-to-update-user-password-in-django-rest-framework

TODO: add a view etc to the below.

'''
class PasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

'''
    FLOW:
    
    projects app > crowdfunding settings > project models > make / migrate > project serializers > project views > project urls > Crowdfunding urls
    
    user app > crowdfunding settings > user models > make / migrate > project models > make / migrate > create superuser > user serializer > user view > user urls > crowdfunding urls
'''
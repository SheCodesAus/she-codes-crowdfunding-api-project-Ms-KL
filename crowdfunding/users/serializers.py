from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'is_active', 'password','bio','avatar')

        extra_kwargs = {
            'email':{
                'allow_blank':False,
                'required':True},
            'password':{
                'write_only':True},
            'is_active':{'read_only':True}
        }

    def create(self, validated_data):
        user = CustomUser.objects.create(**validated_data)
        user.set_password(validated_data['password']) 
        user.save()
        return user

# Start of Change Password
class PasswordChangeSerializer(serializers.Serializer):
    model = CustomUser
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

# Notes on process (For own info)

'''
    NOTE: 
    - Changed original code to Model Serializer, added extra kwarg restrictions, set password for security
    - https://www.django-rest-framework.org/api-guide/serializers/#additional-keyword-arguments
    TODO:
    - finish change password
    - make creation view like a form (similar to pledges)
    - edit profile
    
    ** FLOW **

    projects app > crowdfunding settings > project models > make / migrate > project serializers > project views > project urls > Crowdfunding urls
    
    user app > crowdfunding settings > user models > make / migrate > project models > make / migrate > create superuser > user serializer > user view > user urls > crowdfunding urls
'''

# --- ORIGINAL CLASS SETUP CODE
'''
    class CustomUserSerializer(serializers.Serializer):
        id = serializers.ReadOnlyField()
        username = serializers.CharField(max_length=150)
        # cling data (clean data - check to see if username is email)
        email = serializers.EmailField()
        # added 21/1 below
        is_active = serializers.BooleanField()

        def create(self, validated_data):
            return CustomUser.objects.create(**validated_data)
            # what is **validated_data
    
    TODO:
    - set password > done
    - try Model Serializer > done
    - enforce field completion > done
    - change/reset password
    - validate changes
'''

# ------------ EXPERIMENTATION + CODE HISTORY -----------

# --- CLASS SETUP CODE W/ password added
'''
    NOTE:
    - Password is not being protected (Can see in database)
    - Try refactoring as Model Serializer

    class CustomUserSerializer(serializers.Serializer):
        id = serializers.ReadOnlyField()
        username = serializers.CharField(max_length=150)
        # cling data (clean data - check to see if username is email)
        email = serializers.EmailField()
        # added 21/1 below
        is_active = serializers.BooleanField()
        password = serializers.CharField(write_only=True)

        def create(self, validated_data):
            return CustomUser.objects.create(**validated_data)
            # what is **validated_data
'''
# --- CONVERT TO MODEL SERIALIZER W/ set_password + alternative validation method
''' 
    NOTE:
    - CONVERT TO MODEL SERIALIZER
    - 
    - using set_password to hash passwords
    - def create validation could be simplified

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
# --- MODEL SERIALIZER w/ simplified validation and no set_password
'''
    NOTE:
    - Efficient but not secure.
    - set_password hashes passwords so they can't be viewed by admin/code

    class CustomUserSerializer(serializers.ModelSerializer):
        password = serializers.CharField(write_only=True)

        class Meta:
            model = CustomUser
            fields = ('id', 'username', 'email', 'is_active', 'is_staff', 'password')

            def create(self, validated_data):
                user = CustomUser.objects.create(**validated_data)
                return user
'''
# --- EXPERIMENT WITH ALL FIELDS AND GROUPS -----

'''
    - https://stackoverflow.com/questions/33844003/how-to-serialize-groups-of-a-user-with-django-rest-framework

from django.contrib.auth.models import Group

    class GroupSerializer(serializers.ModelSerializer):    
        class Meta:
            model = Group
            fields = ('name',)

    class CustomUserSerializer(serializers.ModelSerializer):
        class Meta:
            model = CustomUser
            fields = ('__all__')
            extra_kwargs = {
                'username':{'required':True},
                'email':{
                    'allow_blank':False,
                    'required':True},
                'password':{
                    'write_only':True, 
                    'required':True},
                'is_active':{'read_only':True}
                'is_staff':{'write_only':True},
                'groups':{'write_only':True},
                'user_permissions':{'write_only':True},
                'is_superuser':{'read_only':True},
                }

            def create(self, validated_data):
                user = CustomUser.objects.create(**validated_data)
                user.set_password(validated_data['password'])
                user.save()
                return user

'''
# --- RESOURCES
'''
    https://studygyaan.com/django/django-rest-framework-tutorial-change-password-and-reset-password
    https://www.grepper.com/tpc/django+rest+framework+serializer+hash+password
    https://stackoverflow.com/questions/38845051/how-to-update-user-password-in-django-rest-framework
'''

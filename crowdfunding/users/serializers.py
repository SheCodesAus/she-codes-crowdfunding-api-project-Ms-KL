from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'is_active', 'password')

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
            user.set_password(validated_data['password']) # protects password
            user.save()
            return user

# Start of Change Password
class PasswordChangeSerializer(serializers.Serializer):
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
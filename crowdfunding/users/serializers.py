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
        user.set_password(validated_data['password']) # protects password
        user.save()
        return user

# Start of Change Password

class ChangePasswordSerializer(serializers.Serializer):
    # https://stackoverflow.com/a/38846554
    model = CustomUser
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

# See user_profile_playground branch for code history, experiment etc

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
# --- RESOURCES
'''
    https://studygyaan.com/django/django-rest-framework-tutorial-change-password-and-reset-password
    https://www.grepper.com/tpc/django+rest+framework+serializer+hash+password
    https://stackoverflow.com/questions/38845051/how-to-update-user-password-in-django-rest-framework
'''

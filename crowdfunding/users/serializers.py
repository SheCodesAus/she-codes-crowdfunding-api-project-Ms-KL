from rest_framework import serializers, validators
from .models import CustomUser
class CustomUserSerializer(serializers.ModelSerializer):
    '''
    validator added as unique is not permitted in extra_kwargs
    - https://stackoverflow.com/questions/65342238/django-rest-framework-extra-kwargs-fields-for-password-and-unique-email
    - http://www.django-rest-framework.org/api-guide/validators/#uniquevalidator
    '''

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'is_active', 'password','bio','avatar')

        extra_kwargs = {
            'email':{
                'validators':
                [validators.UniqueValidator(queryset=CustomUser.objects.all())],
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

class CustomUserDetail(CustomUserSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'is_active','bio','avatar')
        read_only_fields = ['id']

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

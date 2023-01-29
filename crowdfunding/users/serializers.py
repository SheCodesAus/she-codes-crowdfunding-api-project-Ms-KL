from rest_framework import serializers, validators
from .models import CustomUser

from projects.serializers import CommentSerializer, ProjectSerializer, PledgeSerializer
class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'is_active', 'password','bio','avatar')
        # fields = ('id', 'username', 'email', 'is_active', 'password','bio','avatar','comments','projects','pledges')

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
    # below based on ProjectSerializer approach for owner
    comments = CommentSerializer(many=True, source='commenter_comments')
    pledges = PledgeSerializer(many=True, source='supporter_pledges')
    projects = ProjectSerializer(many=True, source='owner_projects')
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'is_active','bio','avatar','comments','pledges','projects')
        read_only_fields = ['id','comments','pledges','projects']

# Start of Change Password

class ChangePasswordSerializer(serializers.Serializer):

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

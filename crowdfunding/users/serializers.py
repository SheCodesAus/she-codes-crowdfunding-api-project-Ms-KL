from rest_framework import serializers, validators
from .models import CustomUser
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
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'is_active','bio','avatar')
        read_only_fields = ['id']

# Start of Change Password

class ChangePasswordSerializer(serializers.Serializer):

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

# alt:

# from projects.models import Project, Pledge, Comment
# from projects.serializers import CommentSerializer, ProjectDetailSerializer, PledgeDetailSerializer

# class CustomUserSerializer(serializers.ModelSerializer):
    # alt:
    # owner = serializers.ReadOnlyField(source='customuser_comments')
    # projects = serializers.ReadOnlyField(source='customuser_projects')
    # pledges = serializers.ReadOnlyField(source='customuser_pledges')

# class CustomUserDetail(CustomUserSerializer):
#     comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#     projects = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#     pledges = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#     class Meta:
#         model = CustomUser
#         fields = ('id', 'username', 'email', 'is_active','bio','avatar','comments','projects','pledges')
#         read_only_fields = ['id']

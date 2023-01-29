from rest_framework import serializers
# for every model, create a serializer.
# You can use a model serializer - like a model form.
# Can build itself off a model. Automates

from .models import Project, Pledge, Comment

class PledgeSerializer(serializers.ModelSerializer):
    '''
    SlugRelatedField:
    changing the way project title displays in GET request. Displays the title of the project and not the id # using slug (human readable label)

    '''
    project = serializers.SlugRelatedField(
        queryset = Project.objects.all(),
        slug_field='title'
    )
    supporter = serializers.SerializerMethodField()
    class Meta:
        model = Pledge
        fields = ['id','amount','comment','anonymous','project','supporter']
        read_only_fields = ['id', 'supporter'] # added to remove the needs to input a supporter {automates to logged in user}

    def get_supporter(self, instance):
        '''

        if the instance (supporter) has anonymous = True:
            replace True with "anonymous"
        else
            replace False with the username of the supporter
        '''
        if instance.anonymous:
            return "anonymous"
        else:
            return instance.supporter.username

class PledgeDetailSerializer(PledgeSerializer):
    '''
    Slug:changing the way project title displays in POST or PUT request. Displays the title of the project and not the id # using slug (human readable label)
    '''

    project = serializers.SlugRelatedField(
        queryset = Project.objects.all(),
        slug_field='title'
    )
    class Meta:
        model = Pledge
        fields = ['id','amount','comment','anonymous','project','supporter']
        read_only_fields = ['id', 'supporter','amount','project']

class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner_id')
    sum_pledges = serializers.ReadOnlyField()
    goal_balance = serializers.ReadOnlyField()
    funding_status = serializers.ReadOnlyField()
    class Meta:
        model = Project
        fields = ['id','title','description','goal','image','is_open','date_created','owner','sum_pledges','goal_balance','funding_status']
        read_only_fields = ['id', 'owner','sum_pledges', 'goal_balance','funding_status']

class CommentSerializer(serializers.ModelSerializer):
    commenter = serializers.ReadOnlyField(source='commenter.username')
    class Meta:
        model = Comment
        fields = ['id','created','body','commenter','project']
        read_only_fields = ['id', 'commenter'] # added to remove the needs to input a supporter {automates to logged in user}


class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['pledges','comments']


    # split out from Project Serializer to reduce amount of data fetching when viewing all projects
    # put it in views



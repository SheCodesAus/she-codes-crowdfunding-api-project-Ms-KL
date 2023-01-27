from rest_framework import serializers
# for every model, create a serializer.
# You can use a model serializer - like a model form.
# Can build itself off a model. Automates

from .models import Project, Pledge

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


class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField()
    description = serializers.CharField(max_length=None)
    goal = serializers.IntegerField() #want to set a min of 1
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.ReadOnlyField()
    owner = serializers.ReadOnlyField(source='owner_id')
    '''
    - owner = serializers.CharField(max_length=200) replaced w/ read only field
    - saving a query to the db.
    - when someone creates a project, the logged in user becomes the owner
    '''
    sum_pledges = serializers.ReadOnlyField()
    goal_vs_pledges = serializers.ReadOnlyField()

    def create(self, validated_data):
        return Project.objects.create(**validated_data)
        # ** take everything in the dic and process it as pairs... eg key=value

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance

class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)
    # split out from Project Serializer to reduce amount of data fetching when viewing all projects
    # put it in views


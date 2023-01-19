from rest_framework import serializers
# for every model, create a serializer. You can use a model serializer - like a model form. Can build itself off a model. Automate

from .models import Project, Pledge #added

class PledgeSerializer(serializers.ModelSerializer):
    # add specifications here or in models
    # owner = serializers.CharField(max_length=200) removed
    class Meta:
        model = Pledge
        fields = ['id','amount','comment','anonymous','project','supporter']
        read_only_fields = ['id', 'supporter'] # added to remove the needs to input a supporter {automates to logged in user}

class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField()
    description = serializers.CharField(max_length=None)
    goal = serializers.IntegerField()
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField()
    # owner = serializers.CharField(max_length=200) - removed to replace with a readonly field
    owner = serializers.ReadOnlyField(source='owner_id')
    # saving a query to the db.
    # now when someone creates a project, the logged in user becomes the owner

    def create(self, validated_data):
        return Project.objects.create(**validated_data) # ** take everything in the dic and process it as pairs... eg key=value
    
    def update(self, instance, validated_data): # adds an update method to serializer
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


'''
    FLOW:
    
    projects app > crowdfunding settings > project models > make / migrate > project serializers > project views > project urls > Crowdfunding urls
    
    USERS:
    user app > crowdfunding settings > user models > make / migrate > project models > make / migrate > create superuser > user serializer > user view > user urls > crowdfunding urls

    Permissions:
    project views > project serializers > project views > project permissions > project views
'''


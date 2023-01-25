from rest_framework import serializers
# for every model, create a serializer. 
# You can use a model serializer - like a model form. 
# Can build itself off a model. Automates

from .models import Project, Pledge

class PledgeSerializer(serializers.ModelSerializer):
    '''
    SlugRelatedField:
    changing the way project title displays in GET request. Displays the title of the project and not the id # using slug (human readable label)

    https://www.django-rest-framework.org/api-guide/relations/#slugrelatedfield

    https://docs.djangoproject.com/en/4.1/topics/db/queries/#retrieving-all-objects

    https://www.django-rest-framework.org/api-guide/relations/

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
        * SerializerMethodField *

        if the instance (supporter) has anonymous = True:
            replace True with "anonymous"
        else
            replace False with the username of the supporter
        
        References:
        https://www.django-rest-framework.org/api-guide/fields/#serializermethodfield
        https://www.django-rest-framework.org/api-guide/serializers/#dealing-with-complex-data-types
        https://stackoverflow.com/a/69160982
        '''
        if instance.anonymous:
            return "anonymous"
        else:
            return instance.supporter.username

class PledgeDetailSerializer(PledgeSerializer):
    '''
    changing the way project title displays in POST or PUT request. Displays the title of the project and not the id # using slug (human readable label)

    https://www.django-rest-framework.org/api-guide/relations/#slugrelatedfield

    https://docs.djangoproject.com/en/4.1/topics/db/queries/#retrieving-all-objects

    https://www.django-rest-framework.org/api-guide/relations/

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
    date_created = serializers.DateTimeField()
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


'''
    FLOW:
    
    projects app > crowdfunding settings > project models > make / migrate > project serializers > project views > project urls > Crowdfunding urls
    
    USERS:
    user app > crowdfunding settings > user models > make / migrate > project models > make / migrate > create superuser > user serializer > user view > user urls > crowdfunding urls

    Permissions:
    project views > project serializers > project views > project permissions > project views
'''

# alternative solution to SerializerMethodField():

    # https://dev.to/abdenasser/my-personal-django-rest-framework-serializer-notes-2i22
    # https://testdriven.io/tips/ed79fa08-6834-4827-b00d-2609205129e0/
    # https://www.django-rest-framework.org/api-guide/serializers/#overriding-serialization-and-deserialization-behavior

    # def to_representation(self, instance):
    #     data = super().to_representation(instance) # allows you to change what is shown after serialization
    #     if data.get('anonymous') and data.get('supporter'): #if anon = true and supporter exists
    #         data.pop('supporter') # delete supporter value from return (not db)
    #         data['supporter'] = "anonymous"  # return "anonymous" instead
    #     elif data.get('anonymous') == False:
    #         data.pop('supporter')
    #         data['supporter'] = data['username']
    #     return data


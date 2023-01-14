from rest_framework import serializers
# for every model, create a serializer. You can use a model serializer - like a model form. Can build itself off a model. Automate

# models > serializers > views > urls projects > urls crowdfunding

from .models import Project, Pledge #added

class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField()
    description = serializers.CharField(max_length=None)
    goal = serializers.IntegerField()
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField()
    owner = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return Project.objects.create(**validated_data) # ** take everything in the dic and process it as pairs... eg key=value

class PledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pledge
        fields = ['id','amount','comment','anonymous','project','supporter']
        


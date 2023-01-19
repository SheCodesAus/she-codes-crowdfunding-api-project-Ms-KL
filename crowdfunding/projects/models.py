from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

# for every model, create a serializer

User = get_user_model()
# added to use the user
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    goal = models.IntegerField() #want to set a min of 1
    image = models.URLField()
    is_open = models.BooleanField() #alt = is_active or status
    date_created = models.DateTimeField(auto_now_add=True) #TIP: auto_now_add=True... will update to time when created
    # owner = models.CharField(max_length=200) - no longer used
    owner = models.ForeignKey( # the below connects the ID of the owner to the owner_projects
        User, 
        on_delete=models.CASCADE, 
        related_name='owner_projects'
        )

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        Project, 
        on_delete=models.CASCADE, 
        related_name="pledges")
    # supporter = models.CharField(max_length=200)
    supporter = models.ForeignKey( # foreign key triggers a rename to a number/id. Eg supporter will be supporter ID
        User,
        on_delete=models.CASCADE, # is null or protect as alternatives instead of delete to protect that data
        related_name='supporter_pledges'
    )

'''
    FLOW:
    
    projects app > crowdfunding settings > project models > make / migrate > project serializers > project views > project urls > Crowdfunding urls
    
    user app > crowdfunding settings > user models > make / migrate > project models > make / migrate > create superuser > user serializer > user view > user urls > crowdfunding urls
'''
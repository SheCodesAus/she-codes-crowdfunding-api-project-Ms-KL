from django.db import models
from django.contrib.auth.models import AbstractUser #added 17/1

# Create your models here.

# added: abstract user below to return the user name as a string instead of the database raw name
# next: update the project models to use the user

class CustomUser(AbstractUser):

    def __str__(self):
        return self.username

'''
    FLOW:
    
    projects app > crowdfunding settings > project models > make / migrate > project serializers > project views > project urls > Crowdfunding urls
    
    user app > crowdfunding settings > user models > make / migrate > project models > make / migrate > create superuser > user serializer > user view > user urls > crowdfunding urls
'''

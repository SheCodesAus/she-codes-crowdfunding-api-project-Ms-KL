from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

# for every model, create a serializer

User = get_user_model() # added to use the user
class Project(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    goal = models.IntegerField() #want to set a min of 1
    image = models.URLField()
    is_open = models.BooleanField() #alt = is_active or status
    date_created = models.DateTimeField(auto_now_add=True) #TIP: auto_now_add=True... will update to time when created
    owner = models.ForeignKey( # the below connects the ID of the owner to the owner_projects
        User, 
        on_delete=models.CASCADE, 
        related_name='owner_projects'
        )
    
    @property
    def sum_pledges(self):
        '''
        Calculates the total of each pledge for each project.
        '''
        pledge_sum = self.pledges.aggregate(sum=models.Sum('amount'))['sum']
        if pledge_sum == None:
            return 0
        else:
            return pledge_sum

    @property
    def goal_vs_pledges(self):
        '''
        Looks at the goal and compares to the total number of pledges.
        '''
        goal_balance = self.goal - self.sum_pledges
        
        if goal_balance <= 0:
            return f"Congratulations! {self.title} project has been funded with {self.sum_pledges} worth of pledges!"
        else:
            return f"There's {goal_balance} left to raise until the goal of {self.goal} is reached!"
    
    def __str__(self):
        '''
        Changing representation of project object id to title so when ModelSerializer form is rendered, the title of the project will display, not the ID number.
        
        Same way as in admin portal from django project
        '''
        return self.title

class Pledge(models.Model):
    '''
    Foreign key triggers a rename to a number/id. Eg supporter will be supporter ID
    on_delete alternatives: is null or protect as alternatives instead of delete to protect that data

    '''
    # amount = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.IntegerField() #want to set a min of 1
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        Project, 
        on_delete=models.CASCADE, 
        related_name="pledges",
        )
    supporter = models.ForeignKey( 
        User,
        on_delete=models.CASCADE, 
        related_name='supporter_pledges'
    )

'''
    FLOW:
    
    projects app > crowdfunding settings > project models > make / migrate > project serializers > project views > project urls > Crowdfunding urls
    
    user app > crowdfunding settings > user models > make / migrate > project models > make / migrate > create superuser > user serializer > user view > user urls > crowdfunding urls
'''
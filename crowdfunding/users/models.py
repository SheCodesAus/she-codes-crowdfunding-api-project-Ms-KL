from django.db import models
from django.contrib.auth.models import AbstractUser #added 17/1

class CustomUser(AbstractUser):
    bio = models.CharField(blank=True, null=True, max_length=150)
    avatar = models.URLField(blank=True, null=True)

    # comments = models.ForeignKey(
    #     Comment,
    #     on_delete=models.CASCADE,
    #     related_name='user_comments'
    # )
    # pledges = models.ForeignKey(
    #     Pledge,
    #     on_delete=models.CASCADE,
    #     related_name='user_pledges'
    # )
    # projects = models.ForeignKey(
    #     Project,
    #     on_delete=models.CASCADE,
    #     related_name='user_projects'
    # )

    # alt:
    # comments = models.ManyToManyField('projects.Comment', related_name='customuser_comments')
    # projects = models.ManyToManyField('projects.Comment', related_name='customuser_projects')
    # pledges = models.ManyToManyField('projects.Comment', related_name='customuser_pledges')

    def __str__(self):
        return self.username

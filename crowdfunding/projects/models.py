from django.db import models

# Create your models here.
# added in W1 Sat class following Ben - Step 7 Thinkific... added lines settings (line 34 + 35). Saved both. Makemigrations and migrate # for every model, create a serializer

# models > serializers > views > urls
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    goal = models.IntegerField() #want to set a min of 1
    image = models.URLField()
    is_open = models.BooleanField() #alt = is_active or status
    date_created = models.DateTimeField(auto_now_add=True) #TIP: auto_now_add=True... will update to time when created
    owner = models.CharField(max_length=200)


from django.db import models
from datetime import datetime
# Create your models here.

class Snippet(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=10000000000)
    created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=True,blank=True)
    snippet_image = models.FileField(null=True,blank=True,upload_to="images/profile")

    def __str__(self):
        return self.name

    @property
    def days_till(self):
        today = date.today()
        days_till = self.created.date() - today
        if self.created.date() < today:
            days_till_stripped = "Past"
        else:
            days_till_stripped = str(days_till).split(",",1)[0]
    
class SnippetImage(models.Model):
    post = models.ForeignKey(Snippet,default=None,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/profile')
    
    def __str__(self):
        return self.post.name



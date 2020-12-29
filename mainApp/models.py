from django.db import models

# Create your models here.

class Protfolio(models.Model):
    project_name = models.CharField(max_length=40)
    project_link = models.URLField(max_length=100,db_index=True, blank=True)
    project_image = models.ImageField(blank=True,upload_to='images')
    SELECT = (
        ('mobile','mobile'),
        ('development','development'),
        ('design','design'),
    )
    project_type = models.CharField(max_length=100,choices=SELECT)
    project_description = models.TextField(blank=True)

    def __str__(self):
        return self.project_name

class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.CharField(max_length=100)
    comment_from_admin = models.TextField(max_length=None,blank=True)
    SELECT = (
        ('unseen','UnSeen'),
        ('seen','Seen'),
        ('done','Done'),
        ('in Progress','In Progress'),
    )
    action = models.CharField(max_length=20, choices=SELECT,default=SELECT[0][0])

    def __str__(slef):
        return "{} | {}".format(slef.full_name,slef.action)
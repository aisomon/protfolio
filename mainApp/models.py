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
    

class Setting(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    company = models.CharField(max_length=50)
    address = models.CharField(blank=True,max_length=100)
    phone = models.CharField(blank=True,max_length=15)
    fax = models.CharField(blank=True,max_length=15)
    email = models.CharField(blank=True,max_length=50)
    smtpserver = models.CharField(blank=True,max_length=50)
    smtpemail = models.CharField(blank=True,max_length=50)
    smtppassword = models.CharField(blank=True,max_length=10)
    smtpport = models.CharField(blank=True,max_length=5)
    icon = models.ImageField(blank=True,upload_to='images/')
    backround_image = models.ImageField(blank=True,upload_to='images/')
    facebook = models.CharField(blank=True,max_length=50)
    instagram = models.CharField(blank=True,max_length=50)
    twitter = models.CharField(blank=True,max_length=50)
    github = models.CharField(blank=True,max_length=50)
    youtube = models.CharField(blank=True, max_length=50)
    aboutus = models.TextField(blank=True)
    contact = models.CharField(blank=True, max_length=80)
    references = models.CharField(blank=True, max_length=80)
    status=models.CharField(max_length=10,choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class MyArea(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=150)
    fa_fa_awsome_icon = models.CharField(blank=True,max_length=15)
    area_image = models.ImageField(blank=True,upload_to='images/')
    status=models.CharField(max_length=10,choices=STATUS)

    def __str__(self):
        return self.title
    

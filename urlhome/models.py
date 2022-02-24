from django.db import models

# For Blogs
class Blogs(models.Model):
    title = models.CharField(max_length=30)
    slug = models.CharField()
    post_unique_id=models.CharField(max_length=30)
    f_Image= models.ImageField(upload='/static/f_images')
    Content = models.TextField(max_length=30)
    view=models.CharField(default=0)
    date=models.DateTimeField(auto_now_add=True)


# For Person's Comment
class Comments(models.Model):
    person = models.CharField(max_length=30)
    person_image= models.ImageField(upload='/static/c_images',default='/static/default/def.png')
    comment = models.TextField(max_length=30)
    post_unique_id=models.IntegerField(max_length=30)
    date=models.DateTimeField(auto_now_add=True)


# For Person's Contact Details
class Contact(models.Model):
    name = models.CharField()
    email=models.CharField()
    website=models.CharField(default=None)
    Content=models.TextField()
    date=models.DateTimeField(auto_now_add=True)


# For New User's Details
class NewUser(models.Model):
    username=models.CharField()
    email=models.CharField()
    password=models.CharField()
    Secret_key=models.CharField()
    date=models.DateTimeField(auto_now_add=True)


# For Users To Submit Their Site To Our Database 
class NewSites(models.Model):
    site=models.CharField()
    date=models.DateTimeField(auto_now_add=True)


# For Hosting Ip To put our ip To User's Sits
class HostIp(models.Model):
    ip=models.CharField()
    date=models.DateTimeField(auto_now_add=True)

# For Short Urls
class ShortUrl(models.Model):
    long_url=models.CharField()
    short_url=models.CharField()
    view=models.CharField(default=0)
    date=models.DateTimeField(auto_now_add=True)

# For Short Blog Urls
class ShortBlogUrl(models.Model):
    long_url=models.CharField()
    short_url=models.CharField()
    view=models.CharField(default=0)
    date=models.DateTimeField(auto_now_add=True)

# For Pages
class Pages(models.Model):
    title = models.CharField(max_length=30)
    slug = models.CharField()
    post_unique_id=models.CharField(max_length=30)
    f_Image= models.ImageField(upload='/static/f_images')
    Content = models.TextField(max_length=30)
    view=models.CharField(default=0)
    date=models.DateTimeField(auto_now_add=True)

# For Referal Url
class Invite(models.Model):
    Secret_key=models.CharField()
    view=models.CharField(default=0)
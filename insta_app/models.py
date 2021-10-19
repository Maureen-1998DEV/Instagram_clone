from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from tinymce.models import HTMLField
from cloudinary.models import CloudinaryField
# Create your models here.

# class Profile
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    bio = models.CharField(max_length=200)
    profile_pic = CloudinaryField('profile/')
    pub_date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.first_name
    def save_profile(self):
        self.save() 
    def delete_profile(self): 
        self.delete() 
    @classmethod
    def get_profile(cls):
        profiles = cls.objects.all()
        return profiles 
    @classmethod
    def search_by_username(cls,search_term):
        profiles = cls.objects.filter(title__icontains=search_term)
        return profiles
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
     if created:
        Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
     instance.profile.save() 

     #class Image
class Image(models.Model):
    image = CloudinaryField('images/')
    image_name = models.CharField(max_length=30)
    image_caption = models.CharField(max_length=30)
    image_location = models.CharField(max_length=30,null=True)
    
    profile = models.ImageField(Profile,on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    posted_time = models.DateTimeField(auto_now_add=True,)
    likes = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-posted_time']

    def save_images(self):
        self.save()
    
    @classmethod
    def get_images(cls):
        images = cls.objects.all()
        return images

# class comments
class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(Image, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length = 500)
    posted_on = models.DateTimeField(auto_now=True)
    

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    @classmethod
    def get_comments_images(cls, id):
        comments = Comments.objects.filter(image__pk = id)
        return comments               

        
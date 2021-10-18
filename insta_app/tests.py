from django.test import TestCase
from .models import Profile, Image,Comments
from django.contrib.auth.models import User


class ProfileTestClass(TestCase):
    
    def setUp(self):
        self.user = User(username='Maureen123')
        self.user.save()
        self.profile = Profile(id=1,user=self.user,photo='nopic.jpg',bio='Artist that is art', name='person')
        self.profile.save_profile()

    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()
        Image.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.user,User))
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save_method(self):
        self.profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)


class ImageTestClass(TestCase):
    def setUp(self):
        self.profile = Profile(user=User(username='Maureen123'))
        self.profile.user.save()
        self.profile.save()
        self.image = Image(user=self.profile,image='nopic.jpg', name='person', caption='we only live once')
        self.image.save_image()

    def test_insatance(self):
        self.assertTrue(isinstance(self.profile,Profile))
        self.assertTrue(isinstance(self.image, Image))

    def save_image(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def update_image_caption(self):
        self.image.save_image()
        new_caption =Image.update_image('i wanna live my life','live it')
        image = Image.objects.get(new_caption='live it')
        self.assertEqual(image.new_caption,'live it')


class CommentsTestClass(TestCase):
    def setUp(self):
        self.profile = Profile(user=User(username='Maureen123'))
        self.profile.user.save()
        self.profile.save()
        self.image = Image(user=self.profile,image='nopic.jpg', name='person', caption='we only live once')
        self.image.save_image()
        self.comments = Comments(comments=self.comments,image='nopic.jpg',caption='we only live once',posted_on="2021/10/07",comments='Amaizing one Girrl')
        self.image.save_comments()
    def test_insatance(self):
        self.assertTrue(isinstance(self.profile,Profile))
        self.assertTrue(isinstance(self.image, Image))
        self.assertTrue(isinstance(self.comments, Comments))

    def save_comments(self):
        self.comments.save_comments()
        comments = Comments.objects.all()
        self.assertTrue(len(comments) > 0)

    def delete_caption(self):
        self.comments.delete_comments()
        delete_caption =Comments.delete_comments('good one girl')
        self.assertEqual(delete_caption,'good one girl')

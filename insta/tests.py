from django.test import TestCase
from .models import Image, Comment, Profile
from django.contrib.auth.models import User


class ImageTestClas(TestCase):
    '''
    Class that tests the images
    '''
    def setUp(self):
        '''
        Creates new instances before a test
        '''
        self.diana = User(username = "diana", email = "diana@gmail.com",password = "12345678")
        self.sun = Image(image = 'imageurl', name ='sun', caption = 'It is bright', profile = self.diana, likes=0)

        self.diana.save()
        self.sun.save_image()

    def tearDown(self):
        '''
        Clears database after each test
        '''
        Image.objects.all().delete()
     
    def test_image_instance(self):
        '''
        This will test whether the new image created is an instance of the Image class
        '''
        self.assertTrue(isinstance(self.sun, Image))

    def test_save_image_method(self):
        '''
        This tests whether new image is added to the db 
        '''
        self.sun.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)> 0)

    def test_delete_image(self):
        '''
        This tests whether image is deleted
        '''
        self.sun.save_image()
        images1 = Image.objects.all()
        self.assertEqual(len(images1),1)
        self.sun.delete_image()
        images2 = Image.objects.all()
        self.assertEqual(len(images2),0)

    def test_update_caption(self):
        '''
        This tests whether the image is updated
        '''
        self.sun.save_image()
        self.sun.update_caption('Yellow')
        self.assertEqual(self.sun.caption, 'Yellow')
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
        self.sun = Image(image = 'imageurl', name ='sun', caption = 'It is bright', profile = self.diana)

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

    def test_get_profile_image_(self):
        '''
        This tests whether images for profiles are retrieved
        '''
        self.sun.save_image
        self.diana.save()
        profile_image = Image.get_profile_images(self.diana)
        self.assertEqual(len(profile_image),1 )

    


class CommentTestClas(TestCase):
    '''
    Class that tests the images
    '''
    def setUp(self):
        '''
        Creates new instances before a test
        '''
        self.diana = User(username = "diana", email = "diana@gmail.com",password = "12345678")
        self.sun = Image(image = 'imageurl', name ='sun', caption = 'It is bright', profile = self.diana)
        self.comment = Comment(image=self.sun, content= 'Beautiful', user = self.diana)

        self.diana.save()
        self.sun.save_image()
        self.comment.save_comment()

    def tearDown(self):
        '''
        Clears database after each test
        '''
        Image.objects.all().delete()
        Comment.objects.all().delete()

    def test_comment_instance(self):
        '''
        This will test whether the new comment created is an instance of the Comment class
        '''
        self.assertTrue(isinstance(self.comment, Comment))

    def test_save_comment_method(self):
        '''
        This tests whether new comment is added to the db 
        '''
        self.comment.save_comment()
        comments = Comment.objects.all()
        self.assertTrue(len(comments)> 0)

    def test_delete_comment(self):
        '''
        This tests whether comment is deleted
        '''
        self.comment.save_comment()
        comments1 = Comment.objects.all()
        self.assertEqual(len(comments1),1)
        self.comment.delete_comment()
        comments2 = Comment.objects.all()
        self.assertEqual(len(comments2),0)

    def test_get_image_comments(self):
        '''
        This tests whether comments can be obtained by image id
        '''
        comments = Comment.get_image_comments(self.sun)
        self.assertTrue(len(comments) > 0)
    

class ProfileTestClas(TestCase):
    '''
    Class that tests the profile
    '''
    def setUp(self):
        '''
        Creates new instances before a test
        '''
        self.diana = User(username = "diana", email = "diana@gmail.com",password = "12345678")
        self.diana.save()
        

    def tearDown(self):
        '''
        Clears database after each test
        '''
        Profile.objects.all().delete()
        User.objects.all().delete()
     
    def test_image_instance(self):
        '''
        This will test whether the new image created is an instance of the Image class
        '''
        self.assertTrue(isinstance(self.diana.profile , Profile))

    def test_search_user(self):
        '''
        This tests whether search method is functioning well
        '''
        self.diana.save()
        user = Profile.search_user(self.diana)
        self.assertEqual(len(user), 1)

    
     
from django.test import TestCase, Client
from . models import *

# Create your tests here.
class UserTestCase(TestCase):

    def setUp(self):
        # Create users
        user1 = User.objects.create(username="Joe")
        user2 = User.objects.create(username="Amy")
        user3 = User.objects.create(username="Bob")

        # Create posts
        Post.objects.create(content="hi", user=user1)
        Post.objects.create(content="jo", user=user1)
        Post.objects.create(content="ho", user=user2)
        Post.objects.create(content="get", user=user2)
        Post.objects.create(content="pel", user=user3)
        Post.objects.create(content="dog", user=user3)
        
        # Create Follows
        Follower.objects.create(user=user1, followingUser=user2)
        Follower.objects.create(user=user3, followingUser=user3)
        Follower.objects.create(user=user2, followingUser=user1)

    def test_post_count(self):
        a = User.objects.get(username="Joe")
        self.assertEqual(a.user.count(), 2)

    def test_follow_valid(self):
        user1 = User.objects.get(username="Joe")
        user2 = User.objects.get(username="Amy")
        f = Follower.objects.get(user=user1, followingUser=user2)
        self.assertTrue(f.is_valid_follow())

    def test_follow_invalid(self):
        user1 = User.objects.get(username="Bob")
        f = Follower.objects.get(user=user1, followingUser=user1)
        self.assertFalse(f.is_valid_follow())

    def test_index(self):
        # Set up client to make requests
        c = Client()

        # Send a get request to the index page and store response
        response = c.get("") 

        # Make sure the status code is 200
        self.assertEqual(response.status_code, 200)

    
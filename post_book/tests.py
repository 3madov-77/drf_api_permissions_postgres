from django.test import TestCase
from .models import Book
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

class TestModels(APITestCase):
    
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='3madov',
            email='3madov@gmail.com',
            password='3madov'
        )
        self.post = Book.objects.create(
            title='new test post',
            author=self.user,
            body='this is test for posting..'
        )

        ################ im tired to find way for checking auth...
        
            
        # user = User.objects.create(username="nerd")

        # # Initialize client and force it to use authentication
        # self.client = APIClient()
        # self.client.force_authenticate(user=user)

    # def test_book_has_an_author(self):
    #     # book = Book.objects.create(title="The man in the high castle")
    #     # self.assertEqual(str(book), "The man in the high castle")
    #     response = self.client.get(reverse('book_detils', args='1'))
    #     self.assertContains(response, {'id': 1, 'title': 'new test post', 'body': 'this is test for posting..'})
    
    def test_post_request_can_create_new_entity(self):
        data = {
            "author": self.user,
            "title": "try testing",
            "body": "Would or not?",
        }
        self.client.post(reverse("all_books"), data=data)
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)


    def test_none_post_owner_can_change(self):
        change_post = {'title': 'test edit new'}
        res = self.client.put(
            reverse('book_detils', args='1'),
            change_post, format='json'
        )
        self.assertEqual(res.status_code, 403)

    def test_none_post_owner_can_delete(self):
        # bucketlist = Book.objects.get()
        response = self.client.delete(
            reverse('book_detils', args='1'),
            format='json',
            follow=True)
        self.assertEquals(response.status_code, 403)

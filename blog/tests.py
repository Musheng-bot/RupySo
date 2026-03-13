from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class BlogTestCase(TestCase):
    def test_blog_list(self):
        blog_list_url = reverse('blog:list')
        response = self.client.get(blog_list_url)
        self.assertEqual(response.status_code, 200)


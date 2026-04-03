from django.test import TestCase
from django.urls import reverse


class AboutTest(TestCase):
    def test_about_page(self):
        response = self.client.get(reverse('about:index'))
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, '一名热衷于技术探索的学习者，喜欢构建有意思的数字产品。')
        self.assertContains(response, 'icon.jpg')
       

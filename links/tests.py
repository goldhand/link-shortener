from django.test import TestCase

from .models import Link
from django.contrib.auth import get_user_model

User = get_user_model()


class LinkTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username='testuser')
        Link.objects.create(base_url='https://google.com',
                                     owner=user, name='google')

    def test_key_unique_on_init(self):
        g_link = Link.objects.get(name='google')
        user = User.objects.get(username='testuser')
        fb_link = Link(base_url='https://facebook.com',
                       owner=user, name='facebook',
                       link_key=g_link.link_key)
        self.assertNotEqual(fb_link.link_key, g_link.link_key)

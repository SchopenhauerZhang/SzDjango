import unittest
from unittest import mock
from route import route 

class TestRoute(unittest.TestCase):
    def test_url(self):
        mock.Mock(return_value=['app/views.py'])
        self.assertEqual(route.url,'www.django.com/app/views.py')
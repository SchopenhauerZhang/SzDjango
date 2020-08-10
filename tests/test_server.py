import unittest
from unittest import mock
from server import Server 

class TestServer(unittest.TestCase):
    def test_url(self):
        mock.Mock(return_value=['app/views.py'])
        self.assertEqual(Server.run,'www.django.com/app/views.py')
from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory

from .views import index

<<<<<<< HEAD

=======
>>>>>>> 8bf5e16791af5989c93baf0971df91b517c89780
class SimpleTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_details(self):
        # Create an instance of a GET request.
<<<<<<< HEAD
        request = self.factory.get("/")
=======
        request = self.factory.get('/')
>>>>>>> 8bf5e16791af5989c93baf0971df91b517c89780
        request.user = AnonymousUser()

        # Test my_view() as if it were deployed at /customer/details
        response = index(request)
<<<<<<< HEAD
        self.assertEqual(response.status_code, 200)
=======
        self.assertEqual(response.status_code, 200)
>>>>>>> 8bf5e16791af5989c93baf0971df91b517c89780

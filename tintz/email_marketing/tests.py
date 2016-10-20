from rest_framework.test import APITestCase
from rest_framework import status
from email_marketing.models import Subscriber


# Create your tests here.
class SubscribersTestCase(APITestCase):

    def setUp(self):
        self.url = '/api/v1/email/subscribers/'

    def test_add_subscriber(self):
        self.assertEqual(Subscriber.objects.all().count(), 0)

        valid_email = 'anonymous@invalid.com'
        invalid_email = 'invalidEmail'

        # Missing email
        response = self.client.post(self.url,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json()['email'][0], "This field is required.")

        # Invalid email
        response = self.client.post(self.url,
                                    data={
                                        'email': invalid_email
                                    },
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json()['email'][0], "Enter a valid email address.")

        # Valid email
        response = self.client.post(self.url,
                                    data={
                                        'email': valid_email
                                    },
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check if it was created
        self.assertEqual(Subscriber.objects.filter(email=valid_email).count(), 1)

        # Can't insert duplicated
        response = self.client.post(self.url,
                                    data={
                                        'email': valid_email
                                    },
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json()['email'][0], "subscriber with this Email already exists.")

    def test_method_not_allowed(self):
        response = self.client.get(self.url,
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

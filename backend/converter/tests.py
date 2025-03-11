from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status


class ConvertNumberAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.valid_number = 12345678
        self.invalid_number = "abcd"

    def test_get_valid_number(self):
        response = self.client.get(f'/num_to_english?number={self.valid_number}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('num_in_english', response.json())

    def test_get_invalid_number(self):
        response = self.client.get(f'/num_to_english?number={self.invalid_number}')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

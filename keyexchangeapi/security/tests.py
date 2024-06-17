from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from .models import Channel

class ChannelTests(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='testpass')
        self.user2 = User.objects.create_user(username='user2', password='testpass')

    def test_create_channel(self):
        self.client.force_authenticate(user=self.user1)
        data = {
            'sender_user': self.user1.id,
            'recipient_user': self.user2.id,
        }
        response = self.client.post('/api/channels/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('id', response.data)
        self.assertEqual(response.data['sender_user'], self.user1.id)
        self.assertEqual(response.data['recipient_user'], self.user2.id)

    def test_accept_channel(self):
        self.client.force_authenticate(user=self.user2)
        channel = Channel.objects.create(sender_user=self.user1, recipient_user=self.user2, name='Test Channel')
        data = {}
        response = self.client.post(f'/api/channels/{channel.id}/accept_channel/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        channel.refresh_from_db()
        self.assertTrue(channel.accepted)

    def test_secret_exchange_view(self):
        self.client.force_authenticate(user=self.user1)
        channel = Channel.objects.create(sender_user=self.user1, recipient_user=self.user2, name='Test Channel')
        response = self.client.post(f'/api/channels/{channel.id}/exchange/', {})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('sender_secret', response.data)

    def test_key_generation_view(self):
        self.client.force_authenticate(user=self.user1)
        channel = Channel.objects.create(sender_user=self.user1, recipient_user=self.user2, name='Test Channel')
        data = {
            'secret_key': 'test_secret_key',
        }
        response = self.client.post(f'/api/channels/{channel.id}/generate-key/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('sender_secret', response.data)
        self.assertIn('recipient_secret', response.data)

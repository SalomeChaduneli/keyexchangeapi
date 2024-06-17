# security/views.py

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Channel
from .serializers import ChannelSerializer

class ChannelListCreateAPIView(generics.ListCreateAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer

class ChannelDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer

class ChannelAcceptAPIView(APIView):
    def post(self, request, pk):
        channel = generics.get_object_or_404(Channel, pk=pk)
        channel.accepted = True
        channel.save()
        return Response(status=status.HTTP_200_OK)

class SecretExchangeAPIView(APIView):
    def post(self, request, pk):
        channel = generics.get_object_or_404(Channel, pk=pk, accepted=True)
        # Implement your secret exchange logic here
        sender_secret = "your_generated_sender_secret"
        recipient_secret = "your_generated_recipient_secret"
        return Response({'sender_secret': sender_secret, 'recipient_secret': recipient_secret})

class KeyGenerationAPIView(APIView):
    def post(self, request, pk):
        channel = generics.get_object_or_404(Channel, pk=pk, accepted=True)
        # Implement your key generation logic here
        sender_key = "your_generated_sender_key"
        recipient_key = "your_generated_recipient_key"
        return Response({'sender_key': sender_key, 'recipient_key': recipient_key})

from rest_framework import serializers
from .models import Channel

class ChannelSerializer(serializers.ModelSerializer):
    sender_user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    recipient_user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Channel
        fields = ['id', 'sender_user', 'recipient_user', 'name', 'accepted', 'initial_sender_secret', 'initial_recipient_secret']

from django.contrib.auth.models import User, Group
from models import ChatMessage
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class ChatMessageSerializer(serializers.ModelSerializer):
	class Meta:
		model = ChatMessage
		fields = ('id', 'messagetext', 'usertext', 'roomtext','pubdate')
		
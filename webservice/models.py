from django.db import models

# Create your models here.
class ChatMessage(models.Model):
	messagetext = models.CharField(max_length=200)
	usertext = models.CharField(max_length=100)
	roomtext = models.CharField(max_length=2)
	pubdate = models.DateTimeField(auto_now_add=True)
	class Meta:
		ordering = ("pubdate",)
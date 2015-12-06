from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, Group
from models import ChatMessage
from rest_framework import viewsets,permissions
from rest_framework.views import APIView
from serializers import UserSerializer, GroupSerializer, ChatMessageSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes,api_view
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import chatcommons

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class JSONResponse(HttpResponse):
	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def chat_messeages_list(request):
	if request.method == 'GET':
		print "chat_messeages_list get\n"
		chatMessages = ChatMessage.objects.all()
		serializer = ChatMessageSerializer(chatMessages, many=True)
		return JSONResponse(serializer.data,status=200)
	elif request.method == 'POST':
		print "chat_messeages_list post\n"
		data=chatcommons.transDataFromMetatoJson(request)
		serializer = ChatMessageSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data, status=200)
		return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def chatMessage_detail(request, id):
	print "chatMessage_detail %s" % (id)
	try:
		chatMess = ChatMessage.objects.get(id=id)
	except:
		return JSONResponse({"status":"404"},status=200)
	if request.method == 'GET':
		print "chatMessage_detail get\n"
		serializer = ChatMessageSerializer(chatMess)
		return JSONResponse(serializer.data,status=200)
	elif request.method == 'PUT':
		print "chatMessage_detail put\n"
		data=chatcommons.transDataFromMetatoJson(request)
		serializer = ChatMessageSerializer(chatMess, data=data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data,status=200)
		return JSONResponse(serializer.errors, status=400)
	elif request.method == 'DELETE':
		print "chatMessage_detail delete\n"
		chatMess.delete()
		return JSONResponse({"status":"204"},status=200)

from serializers import ChatMessageSerializer


DATA_HEADING="HTTP"
# chatmessFields=ChatMessageSerializer().fields.keys()
# chatmessFields=[cmField for cmField in chatmessFields if cmField!="id" and cmField!="pubdate"]

def transDataFromMetatoJson(request):
	data={}
	rBody=request.body.split('&')
	for kv in rBody:
		tmp=kv.split('=')
		data[tmp[0]]=tmp[1]
	# for cmField in chatmessFields:
		# try:
			# data[cmField]=request.META[DATA_HEADING+'_'+cmField.upper()]
		# except KeyError:
			# continue
	return data
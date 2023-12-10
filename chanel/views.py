from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ChanelSerializer
from .models import Chanel

# Create your views here.

@api_view(['GET'])
def chanels(request):
    if request.method == 'GET':
        try:
            all_chanels = Chanel.objects.all()
            serializer = ChanelSerializer(all_chanels, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except:
            return Response({'error': 'Channels Not Found'}, status=status.HTTP_404_NOT_FOUND)
        
    return Response({'error':'Wrong Method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

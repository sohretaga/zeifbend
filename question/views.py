from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist

from .models import Question
from .serializers import QuestionSerializer


@api_view(['GET'])
def get_question(request):
    if request.method == 'GET':
        try:
            random_question = Question.objects.order_by('?')[0]
            serializer = QuestionSerializer(random_question)

            return  Response(serializer.data, status=status.HTTP_200_OK)
        
        except ObjectDoesNotExist:
            return Response({'error': 'Not Found Any Question!'}, status=status.HTTP_404_NOT_FOUND)
    
    return Response({'error': 'Wrong method!'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
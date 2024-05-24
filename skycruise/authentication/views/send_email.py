from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from skycruise.authentication.serializers.send_email import SendEmailSerializer

User = get_user_model()


class SendEmailView(APIView):

    @staticmethod
    def post(request):
        try:
            serializer = SendEmailSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            code = serializer.save()
            return Response({'code': code}, status=status.HTTP_200_OK)

        except Exception as e:
            response = {'message': str(e), 'code': status.HTTP_400_BAD_REQUEST}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

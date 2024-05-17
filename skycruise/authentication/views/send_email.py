from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from skycruise.authentication.serializers.send_email import SendEmailSerializer

User = get_user_model()

class SendEmailView(APIView):
    
    @staticmethod
    def post(request):
        serializer = SendEmailSerializer(data=request.data)
        if serializer.is_valid():
            code = serializer.save()
            return Response({"code": code}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


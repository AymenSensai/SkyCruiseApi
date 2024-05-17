from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from skycruise.authentication.serializers.password_reset import PasswordResetSerializer
from skycruise.general.authentication import get_user_auth_data

class PasswordResetView(APIView):
    
    @staticmethod
    def post(request):
        serializer = PasswordResetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(get_user_auth_data(user, request), status=status.HTTP_200_OK)
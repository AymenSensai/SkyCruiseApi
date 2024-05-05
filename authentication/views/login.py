from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.serializers.login import LoginSerializer
from general.authentication import get_user_auth_data


class LoginView(APIView):

    @staticmethod
    def post(request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        return Response(get_user_auth_data(user, request), status=status.HTTP_200_OK)
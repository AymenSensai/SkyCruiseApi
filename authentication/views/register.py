from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.serializers.register import RegisterSerializer
from general.authentication import get_user_auth_data

class RegisterView(APIView):

    @staticmethod
    def post(request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(get_user_auth_data(user, request), status=status.HTTP_200_OK)
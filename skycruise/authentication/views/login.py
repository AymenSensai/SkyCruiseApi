from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from skycruise.authentication.serializers.login import LoginSerializer
from skycruise.general.authentication import get_user_auth_data


class LoginView(APIView):

    @staticmethod
    def post(request):
        try:
            serializer = LoginSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            user_auth_data = get_user_auth_data(user, request)

            return Response(user_auth_data, status=status.HTTP_200_OK)

        except Exception as e:
            response = {'message': str(e), 'code': status.HTTP_400_BAD_REQUEST}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

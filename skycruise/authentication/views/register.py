from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from skycruise.authentication.serializers.register import RegisterSerializer
from skycruise.general.authentication import get_user_auth_data


class RegisterView(APIView):

    @staticmethod
    def post(request):
        try:
            serializer = RegisterSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            return Response(get_user_auth_data(user, request), status=status.HTTP_200_OK)

        except Exception as e:
            response = {'message': str(e), 'code': status.HTTP_400_BAD_REQUEST}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

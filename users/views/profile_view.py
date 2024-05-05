from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers.profile_serializer import ProfileReadSerializer, ProfileUpdateSerializer


class ProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get(request):
        user = request.user
        serializer = ProfileReadSerializer(user)
        return Response(serializer.data)

    @staticmethod
    def put(request):
        user = request.user
        serializer = ProfileUpdateSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

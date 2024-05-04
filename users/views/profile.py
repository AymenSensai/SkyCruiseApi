from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from users.serializers.profile import UserReadSerializer, UserUpdateSerializer
from rest_framework.response import Response


class UserViewSet(APIView):
    permission_classes = (IsAuthenticated,)
    
    @staticmethod
    def get(request):
        user = request.user
        serializer = UserReadSerializer(user)
        return Response(serializer.data)
        
    @staticmethod
    def put(request):
        user = request.user
        serializer = UserUpdateSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
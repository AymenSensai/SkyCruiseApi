from authentication.serializers.token import TokenSerializer

def get_user_auth_data(user, request):
    return {
        'authentication': TokenSerializer(user).data,
    }

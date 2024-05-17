from skycruise.authentication.serializers.token_pair import TokenSerializer


def get_user_auth_data(user, request):
    return TokenSerializer(user).data

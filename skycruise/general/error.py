from rest_framework.response import Response


def get_error_request(message, status):
    return Response({
        'message': message,
        'code': status,
    }, status=status)


class CustomExceptionHandlerMixin:

    def handle_exception(self, exc):
        response = super().handle_exception(exc)
        if response is not None:
            response.data = {'message': response.data.get('detail', 'An error occurred'), 'code': response.status_code}
        return response

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


def api_response(code, message, result=None, status_code=HTTP_200_OK):
    return Response({
        'code': code,
        'message': message,
        'result': result
    }, status=status_code)

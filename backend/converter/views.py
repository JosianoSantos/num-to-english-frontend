import time

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializers import NumberSerializer
from .utils import number_to_words


class ConvertNumberView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('number', openapi.IN_QUERY, description="Number to convert", type=openapi.TYPE_INTEGER)
        ],
        responses={200: openapi.Response("Success", NumberSerializer), 400: "Invalid input"}
    )
    def get(self, request):
        number = request.GET.get('number')
        time.sleep(5)
        if not number or not number.isdigit():
            return Response({"status": "error", "message": "Invalid number provided."},
                            status=status.HTTP_400_BAD_REQUEST)

        num_in_words = number_to_words(int(number))
        return Response({"num_in_english": num_in_words})

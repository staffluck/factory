from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .serializers import TradePointOutputSerializer, BaseAuthSerializer
from .models import TradePoint

class TradePointListAPIView(GenericAPIView):

    def get(self, request):
        serializer_input = BaseAuthSerializer(data=request.query_params)
        serializer_input.is_valid(raise_exception=True)

        tradepoints = TradePoint.objects.filter(employee__phone=serializer_input.validated_data["phone"])

        serializer_output = TradePointOutputSerializer(tradepoints, many=True)
        return Response(serializer_output.data, 200)

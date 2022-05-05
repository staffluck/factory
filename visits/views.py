from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from .serializers import TradePointOutputSerializer, BaseAuthSerializer, VisitInputSerializer, VisitOutputSerializer
from .models import TradePoint, Visit


class TradePointListAPIView(GenericAPIView):

    def get(self, request):
        serializer_auth_input = BaseAuthSerializer(data=request.query_params)
        serializer_auth_input.is_valid(raise_exception=True)

        tradepoints = TradePoint.objects.filter(employee__phone=serializer_auth_input.validated_data["phone"])

        serializer_output = TradePointOutputSerializer(tradepoints, many=True)
        return Response(serializer_output.data, 200)


class VisitCreateAPIView(GenericAPIView):

    def post(self, request):
        serializer_auth_input = BaseAuthSerializer(data=request.query_params)
        serializer_auth_input.is_valid(raise_exception=True)
        phone = serializer_auth_input.validated_data["phone"]

        serializer_input = VisitInputSerializer(data=request.data)
        serializer_input.is_valid(raise_exception=True)
        data = serializer_input.validated_data

        #  Я бы вывел это в сериализатор, используя MethodField - передавал tradepoint queryset с фильтром по полю phone
        if data["tradepoint"].employee.phone != phone:
            raise ValidationError({"phone": "Телефон не связан с переданной торговой точкой"})

        visit = Visit.objects.create(
            tradepoint=data["tradepoint"],
            latitude=data["latitude"],
            longitude=data["longitude"],
        )

        serializer_output = VisitOutputSerializer(visit)
        return Response(serializer_output.data, status=201)

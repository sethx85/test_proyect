from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from serializers.serializers import BalanceSerializer

class KriptoWallet(APIView):
    def get(self, request: Request):
        serializer = BalanceSerializer(data= request.query_params)
        serializer.is_valid(raise_exception=True)
        current_balance =  serializer.data
        return Response({
            "current_balance": current_balance
        })

    def post(self, request: Request):
        serializer = BalanceSerializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        current_balance =  serializer.data
        # DB request.

        return Response({
            "current_balance": current_balance
        })
    
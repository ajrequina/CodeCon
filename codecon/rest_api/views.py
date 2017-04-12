from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status, permissions, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from pages.models import User
# from pages.serializers import UserSerializer
from rest_framework.views import APIView
from rest_api.models import Account
from rest_api.serializers import AccountSerializer
from rest_api.permissions import IsAccountOwner 
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view


# @api_view(['GET', 'POST'])
# def users(request):
#     if request.method == "GET":
        

class AccountView(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsAccountOwner(),)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            Account.objects.create_user(**serializer.validated_data)
            return Response({'status' : 201, 'message' : 'Account Successfully Created!'})
        
        return Response({
            'status': 400,
            'message': serializer.errors
        })
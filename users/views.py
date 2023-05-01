from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.response import Response
from django.contrib.auth.models import User

class Login(APIView):
    authentication_classes = []
    permission_classes = []
    
    def post(self,request):
        email = request.data['email']
        password = request.data['password']
    
        user = authenticate(username=email,password=password)

        if user == None:
            return Response("User Not Found!",404)
        
        tokens = RefreshToken.for_user(user)
        
        data = {
            'refresh':str(tokens),
            'access':str(tokens.access_token),
        }
        return Response(data,200)
            
            
class Register(APIView):
    authentication_classes = []
    permission_classes = []
    
    def post(self,request):
        email = request.data['email']
        password = request.data['password']
    
        user = authenticate(username=email,password=password)

        if user == None:
            user = User.objects.create_user(username=email,password=password)
            tokens = RefreshToken.for_user(user)
        
            data = {
                'refresh':str(tokens),
                'access':str(tokens.access_token),
            }
            return Response(data,200)
    
        return Response("User Already Exist!",400)
        
        
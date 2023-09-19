
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from details_app.api.serializers import UserdetailSerializer as UD
from details_app.models import Userdetail
from rest_framework.views import APIView
# from details_app.api.permissions import UserOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# from rest_framework.authentication import JWTAuthentication

#from rest_framework.authtoken.models import Token
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
# from rest_framework_simplejwt.tokens import RefreshToken
# # Create your views here.




class User_list(APIView):
    def get(self,request):
        det=Userdetail.objects.all()
        serializer=UD(det, many=True,context={'request': request})
        return Response(serializer.data)
    
    def post(self,request):
        serializer= UD(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        else:
                return Response(serializer.errors, status =status.HTTP_400_BAD_REQUEST)

class User_Detail(APIView):
    permission_classes=[IsAuthenticatedOrReadOnly]
    # authentication_classes = [JWTAuthentication]
    def get(self,request,pk):
        try:
             det= Userdetail.objects.get(pk=pk)
        except Userdetail.DoesNotExist:
            return Response({'Error':'Platform not found'},status=status.HTTP_404_NOT_FOUND)
             
        serializer=UD(det)
        return Response(serializer.data)
    
    def put(self,request,pk):
        
        
        dets=Userdetail.objects.get(pk=pk)        
        serializer=UD(dets, data=request.data)
        
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data)
        
        else:
            return Response(serializer.errors)

    def delete(self,request,pk):
         
        platforms=Userdetail.objects.get(pk=pk)    
        platforms.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
                
    
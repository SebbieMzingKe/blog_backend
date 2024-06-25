from django.shortcuts import render
from django.contrib.auth import authenticate
from .serializers import  SignUpSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.request import Request
from .tokens import create_jwt_pair_for_user
from rest_framework.permissions import AllowAny, IsAuthenticated
from drf_yasg.utils import swagger_auto_schema


class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer
    permission_classes = [AllowAny]



    @swagger_auto_schema(
            operation_summary="Creates a user account",
            operation_description="This signs up a user"
    )
    def post(self, request:Request):
        data = request.data

        serializer = self.serializer_class(data = data)

        if serializer.is_valid():
            serializer.save()

            response = {
                "message": "User Created Successfully",
                "data":serializer.data
            }



            return Response(data = response, status=status.HTTP_201_CREATED)

        return Response(data = serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class LoginView(APIView):
    permission_classes = [AllowAny]


    @swagger_auto_schema(
            operation_summary="Generate JWT pair",
            operation_description="This logs in a user with email and password"
    )
    def post(self, request:Request):
        email = request.data.get('email')
        password = request.data.get('password')
        

        user = authenticate(email = email, password = password)
        if user is not None:
            tokens = create_jwt_pair_for_user(user)
            response = {
                "message":"Login was successful",
                "tokens":tokens,
            }

            return Response(data = response, status=status.HTTP_200_OK)
        else:
            return Response(data = {"message":"Invalid Username or Password"})


    @swagger_auto_schema(
            operation_summary="Get a request info",
            operation_description="This shows request info"
    )
    def get(self, request:Request):
        content = {
            "user":str(request.user),
            "auth":str(request.auth)
        }

        return Response(data = content, status=status.HTTP_200_OK)
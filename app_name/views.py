from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .models import User, Product, Cart
from .serializers import UserSerializer, ProductSerializer, CartSerializer

class UserView(APIView):
	authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request, format=None):
    	users = User.objects.all()
    	serializer = UserSerializer(users, many=True)
    	return Response(serializer.data)

    def post(self, request, format=None):
    	serializer = UserSerializer(data=request.data)
    	if serializer.is_valid():
    		serializer.save()
    		return Response(serializer.data, status=status.HTTP_201_CREATED)
    	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductView(APIView):
	def get(self, request, format=None):
		products = Product.objects.all()
		serializer = ProductSerializer(products, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = ProductSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CartView(APIView):
	def get(self, request, format=None):
		carts = Cart.objects.all()
		serializer = CartSerializer(carts, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = CartSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
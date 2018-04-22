from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .models import User, Product, Cart

class CartView(APIView):
	#something happens

class UserView(APIView):
	authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request, format=None):

class ProductView(APIView):
	#something happens
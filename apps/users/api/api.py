from django.shortcuts import get_object_or_404
from apps.users.authentication_mixins import Authentication
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets

from apps.users.models import User
from apps.users.api.serializers import (
    CustomUserSerializer, UserListSerializer, UpdateUserSerializer,
    PasswordSerializer
)


class UserViewSet(viewsets.GenericViewSet):
    model = User
    serializer_class = CustomUserSerializer
    list_serializer_class = UserListSerializer
    queryset = None

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.model.objects\
                .filter(is_active=True)\
                .values('id', 'username', 'email', 'name')
        return self.queryset

    @action(detail=True, methods=['post'])
    def set_password(self, request, pk=None):
        user = self.get_object(pk)
        password_serializer = PasswordSerializer(data=request.data)
        if password_serializer.is_valid():
            user.set_password(password_serializer.validated_data['password'])
            user.save()
            return Response({
                'message': 'Password updated successfully'
            })
        return Response({
            'message': 'There are errors in the information received',
            'errors': password_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        users = self.get_queryset()
        users_serializer = self.list_serializer_class(users, many=True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        user_serializer = self.serializer_class(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({
                'message': 'Successfully registered user.'
            }, status=status.HTTP_201_CREATED)
        return Response({
            'message': 'There are errors in the registry',
            'errors': user_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        user = self.get_object(pk)
        user_serializer = self.serializer_class(user)
        return Response(user_serializer.data)

    def update(self, request, pk=None):
        user = self.get_object(pk)
        user_serializer = UpdateUserSerializer(user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({
                'message': 'Successfully registered user'
            }, status=status.HTTP_200_OK)
        return Response({
            'message': 'There are errors in the update',
            'errors': user_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        user_destroy = self.model.objects.filter(id=pk).update(is_active=False)
        if user_destroy == 1:
            return Response({
                'message': 'Successfully deleted user'
            })
        return Response({
            'message': 'The user you want to delete does not exist'
        }, status=status.HTTP_404_NOT_FOUND)

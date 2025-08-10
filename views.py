# from .serializers import *
# from .models import *
# from .permissions import UserEdit
# from .filters import HouseFilter
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.filters import SearchFilter, OrderingFilter
# from rest_framework import status, generics, permissions
# from rest_framework.response import Response
# from rest_framework_simplejwt.tokens import RefreshToken
# from django.db.models import Avg
#
#
# class RegisterView(generics.CreateAPIView):
#     serializer_class = UserProfileSerializer
#
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
# class CustomLoginView(generics.GenericAPIView):
#     serializer_class = CustomLoginSerializer
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
# class LogoutView(generics.GenericAPIView):
#     serializer_class = LogoutSerializer
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         try:
#             refresh_token = serializer.validated_data['refresh']
#             token = RefreshToken(refresh_token)
#             token.blacklist()
#             return Response(status=status.HTTP_205_RESET_CONTENT)
#         except Exception:
#             return Response({'detail': 'Невалидный токен'}, status=status.HTTP_400_BAD_REQUEST)

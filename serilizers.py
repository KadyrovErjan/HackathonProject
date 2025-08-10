# from rest_framework_simplejwt.tokens import RefreshToken
# from django.contrib.auth import get_user_model
#
# User = get_user_model()
#
# class UserProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('email', 'password')
#         extra_kwargs = {'password': {'write_only': True}}
#
#     def validate_email(self, value):
#         if User.objects.filter(email=value).exists():
#             raise serializers.ValidationError("Пользователь с таким email уже существует")
#         return value
#
#     def create(self, validated_data):
#         password = validated_data.pop('password')
#         email = validated_data.get('email')
#         user = User(username=email, **validated_data)
#         user.set_password(password)
#         user.save()
#         return user
#
#     def to_representation(self, instance):
#         refresh = RefreshToken.for_user(instance)
#
#         return {
#             'user': {
#                 'username': instance.username,
#                 'email': instance.email,
#             },
#             'access': str(refresh.access_token),
#             'refresh': str(refresh),
#         }
#
#
# class CustomLoginSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField(write_only=True)
#
#     def validate(self, data):
#         email = data.get('email')
#         password = data.get('password')
#
#         try:
#             user = User.objects.get(email=email)
#         except User.DoesNotExist:
#             raise serializers.ValidationError({"email": "Пользователь с таким email не найден"})
#
#         if not user.check_password(password):
#             raise serializers.ValidationError({"password": "Неверный пароль"})
#
#         if not user.is_active:
#             raise serializers.ValidationError("Пользователь не активен")
#
#         self.context['user'] = user
#         return data
#
#     def to_representation(self, instance):
#         user = self.context['user']
#         refresh = RefreshToken.for_user(user)
#
#         return {
#             'user': {
#                 'username': user.username,
#                 'email': user.email,
#             },
#             'access': str(refresh.access_token),
#             'refresh': str(refresh),
#         }
#
#
# class LogoutSerializer(serializers.Serializer):
#     refresh = serializers.CharField()
#
#     def validate(self, attrs):
#         token = attrs.get('refresh')
#         try:
#             RefreshToken(token)
#         except Exception:
#             raise serializers.ValidationError({"refresh": "Невалидный токен"})
#         return attrs
#
#
# class UserProfileListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserProfile
#         fields = ['id', 'username', 'avatar']

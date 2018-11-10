from django.contrib.auth import get_user_model
from rest_framework import serializers, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import APIException
from store.models.models import ExpiredToken
# from rest_framework.permissions import IsAuthenticated
# from django.core.mail import send_mail
# from settings.dev_settings import EMAIL_HOST_USER


User = get_user_model()


class BearerToken(TokenAuthentication):
    keyword = 'Bearer'
    model = ExpiredToken


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'phone', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, attrs):
        email = attrs.get('email')
        if not email or email == 'neo@gmail.com':
            raise APIException("this is error, Johny")
        return attrs

    def create(self, validated_data):
        password = validated_data['password']
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        # success register mail
        # subject = 'snowboard staff successful registration'
        # message = 'Than`x 4 register {}'.format(user.first_name)
        # send_mail(subject, message, EMAIL_HOST_USER, [user.email])
        return user


class UserViewSet(viewsets.ModelViewSet):
    # authentication_classes = (BearerToken, BasicAuthentication)
    # permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

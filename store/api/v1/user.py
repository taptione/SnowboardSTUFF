from django.contrib.auth.models import User
from rest_framework import serializers, viewsets
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class BearerToken(TokenAuthentication):
    keyword = 'Bearer'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'is_staff')

class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = (BearerToken, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

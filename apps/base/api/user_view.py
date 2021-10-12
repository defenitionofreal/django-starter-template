# core imports
from django.contrib.auth import get_user_model
from ..serializers import UserSerializer

# rest framework imports
from rest_framework import viewsets
# from rest_framework.decorators import action
# from rest_framework.response import Response

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """ Retrieve List Create Destroy User View """
    serializer_class = UserSerializer
    queryset = User.objects.all()

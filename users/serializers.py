
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, UserSerializer as BaseUserSerializer

class UserCreateSerializer( BaseUserCreateSerializer ):
    class Meta( BaseUserCreateSerializer.Meta ):
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'address', 'password']


class UserSerializer( BaseUserSerializer ):
    class Meta( BaseUserSerializer.Meta ):
        ref_name = 'CustomUser'
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'address', 'is_staff']
        read_only_fields = ['is_staff']
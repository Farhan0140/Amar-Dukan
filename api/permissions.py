
from rest_framework import permissions


class IsAdmin_Or_ReadOnly( permissions.BasePermission ):
    def has_permission(self, request, view):
        # if request.method == 'GET':
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return bool(request.user and request.user.is_staff)


class Custom_Django_Model_Permission( permissions.DjangoModelPermissions ):
    def __init__(self):
        self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']

        
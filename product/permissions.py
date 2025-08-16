
from rest_framework import permissions

class Is_ReviewAuthor_Or_ReadOnly( permissions.BasePermission ):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return bool( request.user and request.user.is_authenticated)
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if request.user.is_staff:
            return True
        
        return bool(request.user == obj.user)
from rest_framework import permissions

class ReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, object):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return object.author == request.user
from rest_framework import permissions, status
from rest_framework.response import Response
import requests

class IsStaffOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow staff members to edit objects.
    """
    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # For write operations, check if the user is staff.
        return self.is_user_staff(request)

    def is_user_staff(self, request):
        # Fetch user information from the userinfo endpoint.
        auth_header = request.headers.get('Authorization')
        response = requests.get('http://127.0.0.1:8001/api/userinfo/', headers={'Authorization': auth_header})

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            current_user = response.json()
            # Check if the user is staff.
            return current_user.get('is_staff', False)
        else:
            # If failed to fetch user information, deny access.
            return False

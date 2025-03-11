from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only admins to create, update, or delete apps.
    Normal users can only view apps.
    """

    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            # Admins can do anything
            if request.user.is_staff:
                return True
            # Normal users can only view (GET method)
            return request.method in permissions.SAFE_METHODS
        return False


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only normal users to manage UserPoints.
    Admins should not have access.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and not request.user.is_staff


# class CSRFExemptSessionAuthentication(permissions.BasePermission):
#     """
#     Custom permission to bypass CSRF verification.
#     """

#     def has_permission(self, request, view):
#         return True  # Allow all requests (Authentication still applies)

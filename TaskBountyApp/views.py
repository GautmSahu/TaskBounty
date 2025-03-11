from rest_framework import viewsets, permissions
from UserApp.models import UserPoints
from AdminApp.models import App
from .serializers import AppSerializer, UserPointsSerializer
from .custom_permissions import IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticated
from .serializers import AppSerializer, UserPointsSerializer
from .custom_permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .mixins import CsrfExemptMixin


class AppViewSet(CsrfExemptMixin, viewsets.ModelViewSet):
    """
    API endpoint for Apps.
    - Admin can Create, Update, Delete.
    - Normal users can only Read.
    """
    queryset = App.objects.all()
    serializer_class = AppSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]


class UserPointsViewSet(CsrfExemptMixin, viewsets.ModelViewSet):
    """
    API endpoint for UserPoints.
    - Normal users can Create, Update, Delete.
    - Admins cannot access this endpoint.
    """
    queryset = UserPoints.objects.all()
    serializer_class = UserPointsSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        """Ensure users only see their own points."""
        return UserPoints.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Automatically assign the authenticated user to the created record."""
        serializer.save(user=self.request.user)
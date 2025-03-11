from django.utils.deprecation import MiddlewareMixin
import re

class DisableCsrf(MiddlewareMixin):
    def process_request(self, request):
        if request.path.startswith("/auth/") or request.path.startswith("/bounty/apps/") or request.path.startswith("/bounty/points/"):  # Disable CSRF only for auth URLs and restful api's for App and Points
            request.csrf_processing_done = True
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class CsrfExemptMixin:
    """
    Mixin to disable CSRF protection for specific viewsets.
    """
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

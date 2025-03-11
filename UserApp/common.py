from django.apps import apps
from TaskBountyApp.common import ERROR_MESSAGE, handle_error_log

APP_NAME = apps.get_app_config('UserApp').name
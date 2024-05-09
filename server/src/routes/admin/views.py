from starlette_admin import EnumField
from starlette_admin.contrib.sqla import ModelView

from .view_configs import AVAILABLE_USER_TYPES, AVAILABLE_LANGUAGE


class UserView(ModelView):
    fields = [
        "id",
        "username",
        "email",
        "password",
        EnumField("role", choices=AVAILABLE_USER_TYPES, select2=False)
    ]


class TranslateView(ModelView):
    fields = [
        "id",
        "text",
        EnumField("language", choices=AVAILABLE_LANGUAGE, select2=False)
    ]


class SummeryView(ModelView):
    fields = [
        "id",
        "text",
        EnumField("language", choices=AVAILABLE_LANGUAGE, select2=False)
    ]

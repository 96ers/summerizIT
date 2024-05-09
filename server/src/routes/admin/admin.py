from starlette_admin.contrib.sqla import Admin
# from starlette_admin import DropDown
# from starlette_admin.views import Link
# from starlette.middleware.sessions import SessionMiddleware
# from fastapi.middleware import Middleware

from src.database import engine
from src.models import User, TranslationResult, SummaryResult
from .views import UserView, TranslateView, SummeryView


admin = Admin(
    engine=engine,
    title="Admin SummerizIT",
    base_url="/admin",
    route_name="admin",
)


# Add views
admin.add_view(UserView(User, icon="fa fa-user"))
admin.add_view(TranslateView(TranslationResult, icon="fa fa-language"))
admin.add_view(SummeryView(SummaryResult, icon="fa fa-book"))


def admin_page(app):
    admin.mount_to(app)

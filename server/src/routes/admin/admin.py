from starlette_admin.contrib.sqla import Admin
from starlette.middleware.sessions import SessionMiddleware
from starlette.middleware import Middleware
from fastapi.staticfiles import StaticFiles

from src.database import engine
from src.models import User, TranslationResult, SummaryResult, TranslationRequest, SummaryRequest
from .views import UserView, TranslateView, SummaryView
from .provider import MyAuthProvider
from .admin_config import create_admin_user

admin = Admin(
    engine=engine,
    title="Admin SummerizIT",
    base_url="/admin",
    route_name="admin",
    statics_dir="src/routes/admin/static",
    logo_url="https://preview.tabler.io/static/logo-white.svg",
    login_logo_url="/admin/statics/logo.svg",
    auth_provider=MyAuthProvider(),
    middlewares=[Middleware(SessionMiddleware, secret_key="123456")],
)


# Add views
admin.add_view(UserView(User, icon="fa fa-user"))
admin.add_view(TranslateView(TranslationRequest, icon="fa fa-language"))
admin.add_view(TranslateView(TranslationResult, icon="fa fa-language"))
admin.add_view(SummaryView(SummaryRequest, icon="fa fa-book"))
admin.add_view(SummaryView(SummaryResult, icon="fa fa-book"))


def admin_page(app):
    create_admin_user()
    app.mount(
        "/static",
        StaticFiles(directory="src/routes/admin/static"),
        name="static",
    )
    admin.mount_to(app)

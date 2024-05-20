from sqlalchemy.orm import Session

from src.database import engine
from src.models import User, UserRole
from src.utils import PasswordHandler
from src.configs import config



def create_admin_user():
    with Session(engine) as session:
        admin = session.query(User).filter(User.role == UserRole.ADMIN).first()
    if admin:
        return
   
    admin_user = config.admin.USERNAME
    admin_email = config.admin.EMAIL
    admin_password = PasswordHandler(config.admin.PASSWORD)
    with Session(engine) as session:
        session.add(
            User(
                username=admin_user,
                password=admin_password,
                email=admin_email,
                role=UserRole.ADMIN,
            )
        )
        session.commit()

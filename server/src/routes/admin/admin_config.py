from sqlalchemy.orm import Session

from src.database import engine
from src.models import User, UserRole
from src.utils import PasswordHandler


def create_admin_user():
    with Session(engine) as session:
        admin = session.query(User).filter(User.role == UserRole.ADMIN).first()
    if admin:
        return

    print("Create administrator for SummerizIT:")
    print("User: ")
    admin_user = input()
    print("Email:")
    admin_email = input()
    print("Password: ")
    admin_password = PasswordHandler.hash(input())
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

from faker import Faker

fake = Faker()


def create_fake_register_user():
    username = fake.user_name()
    password = fake.password(length=10)
    email = fake.email()
    return {
        "username": username,
        "email": email,
        "password": password
    }


def create_fake_login_user():
    email = fake.email()
    password = fake.password(length=10)
    return {
        "email": email,
        "password": password
    }

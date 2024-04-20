import re
from pydantic import BaseModel, EmailStr, constr, field_validator, Field, UUID4


class UserBase(BaseModel):
    email: EmailStr = Field(..., example="user@gmail.com")

    class Config:
        from_attributes = True


class UserLoginRequest(UserBase):
    password: str = Field(..., example="@123Abcdefgh")


class UserRegisterRequest(UserBase):

    password: constr(min_length=8, max_length=64) = Field(  # type: ignore
        ..., example="@123Abcdefgh"
    )
    username: constr(min_length=3, max_length=64)  # type: ignore

    @field_validator("password")
    def password_must_contain_special_characters(cls, v):
        if not re.search(r"[^a-zA-Z0-9]", v):
            raise ValueError("Password must contain special characters")
        return v

    @field_validator("password")
    def password_must_contain_numbers(cls, v):
        if not re.search(r"[0-9]", v):
            raise ValueError("Password must contain numbers")
        return v

    @field_validator("password")
    def password_must_contain_uppercase(cls, v):
        if not re.search(r"[A-Z]", v):
            raise ValueError("Password must contain uppercase characters")
        return v

    @field_validator("password")
    def password_must_contain_lowercase(cls, v):
        if not re.search(r"[a-z]", v):
            raise ValueError("Password must contain lowercase characters")
        return v

    @field_validator("username")
    def username_must_not_contain_special_characters(cls, v):
        if re.search(r"[^a-zA-Z0-9]", v):
            raise ValueError("Username must not contain special characters")
        return v


class UserResponse(BaseModel):
    userId: UUID4 = Field(..., example="a3b8f042-1e16-4f0a-a8f0-421e16df0a2f")
    email: str = Field(..., example="john.doe@example.com")
    username: str = Field(..., example="john.doe")

    class Config:
        from_attributes = True


class CurrentUser(BaseModel):
    id: int = Field(None, description="User ID")

    class Config:
        validate_assignment = True

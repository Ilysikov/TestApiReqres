import random
from typing import TypedDict, ForwardRef

from pydantic import BaseModel, Field, RootModel

from utils.random_data import constant_support, random_data, UserData, user_data


class ValidData(BaseModel):
    id: int = random.randint(30, 57)
    email: str = user_data.valid_email()
    first_name: str = user_data.valid_first_name()
    last_name: str = user_data.valid_last_name()
    avatar: str = user_data.valid_file()


class UpdateValidData(BaseModel):
    email: str | None = user_data.valid_email()
    first_name: str | None = user_data.valid_first_name()
    last_name: str | None = user_data.valid_last_name()
    avatar: str | None = user_data.valid_file()

    def new_data(cls):
        cls.email = user_data.valid_email()
        cls.first_name = user_data.valid_first_name()
        cls.last_name = user_data.valid_last_name()
        cls.avatar = user_data.valid_file()


class ValidUser(BaseModel):
    data: ValidData = None
    support: object = Field(
        alias='support',
        default_factory=constant_support)

#
# class UserDict(TypedDict):
#     data: object
#     support: object
#
#
# class UpdateUser(BaseModel):
#     data: UpdateValidData
#
#
# class DefaultUserList(RootModel):
#     root: list[ValidUser]

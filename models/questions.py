import random
import re
from re import Match
from typing import List

import requests
from pydantic import BaseModel, Field, field_validator
from utils.random_data import constant_support, user_data


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


class ValidFuturama(BaseModel):
    """
    The model for the /futurama/1 endpoint.
    """
    name: str
    url: str

    @field_validator('name')
    @classmethod
    def valid_name(cls, name: str) -> Match[str] | ValueError:
        """
        Validate name.

        The name must start with a capital letter and contain only letters
        and spaces. The name can contain multiple words, each starting with a capital letter.

        Args:
        name (str): The name to be validated.

        Returns:
        Match[str] | ValueError: The result of the validation or an error.
        """
        # The pattern must allow multiple words with capital letters
        pattern = r"^[A-Z][a-z]+(?: [A-Z][a-z]+)*(?: [A-Z]\.)?$"

        name_list = name.split()

        capitalized_words = [word for word in name_list if word[0].isupper()]

        # Validate the name with the pattern
        answer = re.match(pattern, name)

        answer = answer if len(capitalized_words) == 1 and bool(
            re.match(pattern=r"^[A-Z][a-z]?$", string=name_list[0])) else None

        return answer if answer else ValueError('Invalid name')

    @field_validator('url')
    @classmethod
    def valid_url(cls, url: str) -> Match[str] | ValueError:
        """
        Validate URL.

        The URL must start with https:// and follow valid URL structure.
        If the URL is valid, return the URL.
        If the URL is invalid, return a ValueError with a description of the error.

        Args:
        url (str): The URL to be validated.

        Returns:
        str | ValueError: The validated URL or an error if the validation fails.
        """
        # Регулярное выражение для проверки корректности URL
        pattern = r"^https://[a-zA-Z0-9.-]+(?:/[^\s<>#]*)?$"

        return url if re.match(pattern, url) else ValueError("Invalid URL")

    @field_validator('url')
    @classmethod
    def valid_url_2(cls, url: str) -> str | ValueError:
        """
        Validate url.

        The url must be a valid link.

        Tries to get the link. If the link is valid, returns the link.
        If the link returns a 404 error, returns a ValueError with a description of the error.
        If the link returns any other code, returns a ValueError with a description of the error.
        If any other error occurs (e.g. the link is unreachable), returns a ValueError with a description of the error.

        Args:
        url (str): The url to be validated.

        Returns:
        str | ValueError: The result of the validation.
        """
        try:

            # Try to get the link
            response = requests.get(url)
            if response.status_code == 200:

                # If the link is valid, return the link
                return url
            elif response.status_code == 404:

                # If the link returns a 404 error, return a ValueError with a description of the error
                return ValueError("Ссылка не найдена (код 404)")
            else:

                # If the link returns any other code, return a ValueError with a description of the error
                return ValueError(f"Ссылка вернула код {response.status_code}")
        except requests.exceptions.RequestException as e:

            # If any other error occurs (e.g. the link is unreachable), return a ValueError with a description of the error
            return ValueError(f"Ошибка при попытке доступа к ссылке: {e}")


class ModelItem(BaseModel):
    synopsis: str
    yearsAired: str
    creators: object = Field(alias='creators', default_factory=List[ValidFuturama])
    id: int

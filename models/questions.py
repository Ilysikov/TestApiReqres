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
        and spaces. The name must also contain only one word starting with a capital letter.

        Args:
        name (str): The name to be validated.

        Returns:
        Match[str] | ValueError: The result of the validation.
        """
        # The pattern
        name_list = name.split()
        capitalized_words = [word for word in name_list if word[0].isupper()]
        # The pattern must match the whole string
        pattern = r"^[A-Z][a-z]+( [A-Z][a-z]+)*( [A-Z][a-z]+)*( [A-Z]\.)?$"
        # Get the match
        answer = re.match(pattern, name) if len(capitalized_words) == 1 and bool(
            re.match(pattern=r"^[A-Z][a-z]?$", string=name_list[0])) else None
        if answer:
            # If the name is valid, return the match
            return answer
        else:
            # If the name is invalid, return a ValueError
            return ValueError('Invalid name')

    def valid_url(cls, url: str) -> Match[str] | ValueError:
        """
        Validate url.

        The url must start with https://.

        Args:
        url (str): The url to be validated.

        Returns:
        Match[str] | ValueError: The result of the validation.
        """
        pattern = r"^https://"
        # Try to match the pattern with the url
        answer = re.match(pattern, url)
        # If the pattern does not match the url, return a ValueError with a description of the error
        return answer if answer else ValueError('Invalid url')

    @field_validator('url')
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


INFO = {
    "synopsis": "Филипп Дж. Фрай - 25-летний курьер, живущий в Нью-Йорке, которого заморозили криогенным способом в Новый год 1999 года на 1000 лет, где он просыпается в Нью-Йорке 31 декабря 2999 года. Там он встречает Турангу Лилу, жесткую, но любящую, прекрасную одноглазую инопланетянку; и Бендера, работающего на алкоголе робота-сгибателя, который пристрастился к спиртному, сигарам, воровству и другим вещам. В конце концов, они все встречаются с Пра-Пра-Пра-Пра-Пра Фрая, Хьюбертом Дж. Фарнсвортом. Фарнсворт - очень старый человек, который является гением, но очень дряхлым и забывчивым. Фрай, Лила и Бендер в конечном итоге работают в службе доставки Фарнсворта Planet Express. Затем они встречают своих коллег; Эми Вонг, которая является марсианским стажером, которая происходит из богатой семьи, но все еще человек, который очень хипстер. Также есть Гермес Конрад, который управляет службой доставки и довольно строг. Гермес кажется ямайцем по голосу и внешности. И, наконец, есть доктор Джон Зойдберг, инопланетянин, похожий на лобстера, который является врачом команды. К сожалению, он ничего не знает о людях. Фрай, Лила, Бендер, а иногда Эми и доктор Зойдберг путешествуют по вселенной, рискуя жизнью и здоровьем, доставляя посылки и выполняя благотворительные задания для налоговых вычетов.",
    "yearsAired": "1999–2013", "creators": [{"name": "Дэвид Икс. Коэн", "url": "http://www.imdb.com/name/nm0169326"},
                                            {"name": "Мэтт Грёнинг", "url": "http://www.imdb.com/name/nm0004981"}],
    "id": 1}


class ModelItem(BaseModel):
    synopsis: str
    yearsAired: str
    creators: object = Field(alias='creators', default_factory=List[ValidFuturama])
    id: int


class ModelList(BaseModel):
    results: List[ModelItem]

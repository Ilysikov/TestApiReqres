from http import HTTPStatus

from jsonschema.validators import validate
from pydantic import ValidationError

from crud_request import CRUD
from models.questions import ValidFuturama, ModelItem
from utils.member import id


class TestFuturama:
    crud = CRUD("https://api.sampleapis.com/futurama/info")

    def test_get_futurama(self):
        """
        Tests the /futurama/1 endpoint with a GET method.

        The test sends a GET request to the /futurama/1 endpoint with a valid
        id in the query string. The test asserts that the response status code
        is 200 and that the response body contains the expected keys.

        """
        response = self.crud.get_none_params()
        response_json = response.json()
        response_json = response_json[0] if type(response_json) == list else response_json

        assert (response.status_code == HTTPStatus.OK)

        validate(response_json, ModelItem.model_json_schema())



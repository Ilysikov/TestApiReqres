from http import HTTPStatus

import pytest
from jsonschema.validators import validate
import allure


class TestFuturama:

    def test_get_futurama(self, crud_futurama, model_item):
        """
        Tests the /futurama/1 endpoint with a GET method.

        The test sends a GET request to the /futurama/1 endpoint with a valid
        id in the query string. The test asserts that the response status code
        is 200 and that the response body contains the expected keys.

        """
        response = crud_futurama.get_none_params()
        response_json = response.json()
        response_json = response_json[0] if type(response_json) == list else response_json

        assert (response.status_code == HTTPStatus.OK)

        validate(response_json, model_item.model_json_schema())

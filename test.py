import pytest
from http import HTTPStatus
from crud_request import CRUD
from models.questions import ValidUser, UpdateValidData
import pytest
from jsonschema import validate
from utils.member import id



class TestQuestions:
    crud = CRUD()

    def test_get_users(self):
        response = self.crud.get_users(params={"id": str(id.rid())})
        response_json = response.json()

        assert (response.status_code == HTTPStatus.OK)

        validate(response_json, ValidUser.model_json_schema())

    def test_post_users(self):
        user = UpdateValidData()
        check = user.model_dump()
        response = self.crud.post_users(data=check)
        response_json = response.json()
        id.remember(response_json["id"])

        assert (response.status_code == HTTPStatus.CREATED)

        validate(response_json, ValidUser.model_json_schema())

        for key in check:
            assert check[key] == response_json[key]

    def test_put_users(self):
        user = UpdateValidData()
        user.new_data()
        check = user.model_dump()
        response = self.crud.put_users(params={"id": str(id.rid())}, data=check)
        response_json = response.json()

        assert (response.status_code == HTTPStatus.OK)

        validate(response_json, ValidUser.model_json_schema())

        for key in check:
            assert check[key] == response_json[key]

    def test_patch_users(self):
        user = UpdateValidData()
        user.new_data()
        check = {"email":user.model_dump().get("email")}
        response = self.crud.patch_users(params={"id": str(id.rid())}, data=check)
        response_json = response.json()

        assert (response.status_code == HTTPStatus.OK)

        validate(response_json, ValidUser.model_json_schema())

        for key in check:
            assert check[key] == response_json[key]

    def test_delete_user(self):
        response = self.crud.delete_users(params={"id": str(id.rid())})

        assert (response.status_code == HTTPStatus.NO_CONTENT)

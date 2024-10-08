import pytest
from http import HTTPStatus
from jsonschema import validate

import allure


class TestQuestions:

    def test_get_users(self, crud_req, valid_user, rid):
        response = crud_req.get_users(params={"id": str(rid)})
        response_json = response.json()

        assert (response.status_code == HTTPStatus.OK)

        validate(response_json, valid_user.model_json_schema())

    def test_post_users(self, crud_req, valid_data, valid_user, remember_id):
        user = valid_data()
        check = user.model_dump()
        response = crud_req.post_users(data=check)
        response_json = response.json()
        remember_id(response_json["id"])

        assert (response.status_code == HTTPStatus.CREATED)

        validate(response_json, valid_user.model_json_schema())

        for key in check:
            assert check[key] == response_json[key]

    def test_put_users(self, crud_req, valid_data, valid_user, rid):
        user = valid_data()
        user.new_data()
        check = user.model_dump()
        response = crud_req.put_users(params={"id": str(rid)}, data=check)
        response_json = response.json()

        assert (response.status_code == HTTPStatus.OK)

        validate(response_json, valid_user.model_json_schema())

        for key in check:
            assert check[key] == response_json[key]

    def test_patch_users(self, crud_req, valid_data, valid_user, rid):
        user = valid_data()
        user.new_data()
        check = {"email": user.model_dump().get("email")}
        response = crud_req.patch_users(params={"id": str(rid)}, data=check)
        response_json = response.json()

        assert (response.status_code == HTTPStatus.OK)

        validate(response_json, valid_user.model_json_schema())

        for key in check:
            assert check[key] == response_json[key]

    def test_delete_user(self, crud_req, rid):
        response = crud_req.delete_users(params={"id": str(rid)})

        assert (response.status_code == HTTPStatus.NO_CONTENT)

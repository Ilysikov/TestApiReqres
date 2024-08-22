from http import HTTPStatus

import allure
import pytest

from client_questions import CRUD
from models.questions import (DefaultQuestion, DefaultQuestionsList,
                              QuestionDict, UpdateQuestion, Wines, WinesDict)
from utils.assertions.api.questions import (assert_question, assert_wines)
from utils.assertions.schema import validate_schema


@pytest.mark.questions
@allure.feature('Questions')
@allure.story('Questions API')
class TestQuestions:
    crud = CRUD()

    def test_get_users(self, params=2):
        response = self.crud.get_users(params={"id": str(params)})
        print(response)


class Ni:

    @allure.title('Get questions')
    def test_get_questions(self, class_questions_client: QuestionsClient):
        response = class_questions_client.get_reds_api()
        json_response: list[QuestionDict] = response.json()

        assert (response.status_code, HTTPStatus.OK)

        validate_schema(json_response, DefaultQuestionsList.model_json_schema())

    @allure.title('Create question')
    def test_create_question(self, class_questions_client: QuestionsClient):
        payload = DefaultQuestion()

        response = class_questions_client.create_reds_api(payload)
        json_response: QuestionDict = response.json()

        print(json_response, 'json')
        print(payload, 'pay')

        assert (response.status_code, HTTPStatus.CREATED)
        assert_wines(
            expected_question=json_response,
            actual_question=payload
        )

        validate_schema(json_response, DefaultQuestion.model_json_schema())

    @allure.title('Create reds wines')
    def test_create_wines(self, class_questions_client: QuestionsClient):
        payload = Wines()

        response = class_questions_client.create_reds_api(payload)
        json_response: WinesDict = response.json()

        print(json_response, 'json')
        print(payload, 'pay')
        assert (response.status_code, HTTPStatus.CREATED)
        assert_wines(
            expected_question=json_response,
            actual_question=payload
        )

        validate_schema(json_response, DefaultQuestion.model_json_schema())

    @allure.title('Get question')
    def test_get_question(
            self,
            function_question: DefaultQuestion,
            class_questions_client: QuestionsClient
    ):
        response = class_questions_client.get_question_api(
            function_question.id
        )
        json_response: QuestionDict = response.json()

        assert (response.status_code, HTTPStatus.OK)
        assert_question(
            expected_question=json_response,
            actual_question=function_question
        )

        validate_schema(json_response, DefaultQuestion.model_json_schema())

    @allure.title('Get question')
    def test_reds_api(
            self,
            function_question: DefaultQuestion,
            class_questions_client: QuestionsClient
    ):
        response = class_questions_client.get_red_api(
            function_question.id
        )
        json_response: QuestionDict = response.json()

        assert (response.status_code, HTTPStatus.OK)
        assert_question(
            expected_question=json_response,
            actual_question=function_question
        )

        validate_schema(json_response, DefaultQuestion.model_json_schema())

    @allure.title('Update question')
    def test_update_question(
            self,
            function_question: DefaultQuestion,
            class_questions_client: QuestionsClient
    ):
        payload = UpdateQuestion()

        response = class_questions_client.update_question_api(
            function_question.id, payload
        )
        json_response: QuestionDict = response.json()

        assert (response.status_code, HTTPStatus.OK)
        assert_question(
            expected_question=json_response,
            actual_question=payload
        )

        validate_schema(json_response, DefaultQuestion.model_json_schema())

    @allure.title('Delete question')
    def test_delete_question(
            self,
            function_question: DefaultQuestion,
            class_questions_client: QuestionsClient
    ):
        delete_question_response = class_questions_client.delete_question_api(
            function_question.id
        )
        get_question_response = class_questions_client.get_question_api(
            function_question.id
        )

        assert (delete_question_response.status_code, HTTPStatus.OK)
        assert (
            get_question_response.status_code, HTTPStatus.NOT_FOUND
        )

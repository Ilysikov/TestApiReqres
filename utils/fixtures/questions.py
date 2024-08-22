import pytest

from client_questions import CRUD
# from models.authentication import Authentication
# from models.questions import UserDict
from utils.clients.http.builder import get_http_client


#
# @pytest.fixture(scope="class")
# def class_questions_client():
#     client = get_http_client(auth=Authentication())
#
#     return CRUD(client=client)
#
#
# @pytest.fixture(scope='function')
# def function_question(class_questions_client: QuestionsClient) -> DefaultQuestion:
#     question = class_questions_client.create_question()
#     yield question
#
#     class_questions_client.delete_question_api(question.id)
from models.questions import ValidUser, DefaultUserList, UserDict, UpdateUser


# def assert_question(
#         expected_question: QuestionDict,
#         actual_question: DefaultQuestion | UpdateQuestion):
#     if isinstance(actual_question, DefaultQuestion):
#         assert (expected_question['id'])
#
#     assert expected_question['question']
#     assert expected_question['possibleAnswers']
#     assert expected_question['correctAnswer']
#
#
# def assert_wines(expected_question: WinesDict,
#                  actual_question: Wines):
#     if isinstance(actual_question, Wines):
#         assert (expected_question['id'])
#
#     assert expected_question['winery']
#     assert expected_question['wine']
#     assert expected_question['rating']
#     assert expected_question['location']
#     assert expected_question['image']

def assert_get(
        expected: UserDict,
        actual: DefaultUserList | UpdateUser):
    assert (expected['data'])
    assert (expected["support"])

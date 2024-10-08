from crud_request import CRUD
from models.questions import ValidFuturama, ValidUser, UpdateValidData, ModelItem
import pytest
from utils.member import id

@pytest.fixture
def crud_req():
    crud = CRUD("https://reqres.in")
    return crud


@pytest.fixture(scope="class")
def crud_futurama():
    crud = CRUD("https://api.sampleapis.com/futurama/info")
    return crud

@pytest.fixture
def valid_name():
    return ValidFuturama.valid_name

@pytest.fixture
def valid_url():
    return ValidFuturama.valid_url

@pytest.fixture
def valid_url_2():
    return ValidFuturama.valid_url_2

@pytest.fixture
def valid_user():
    return ValidUser

@pytest.fixture
def valid_data():
    return UpdateValidData

@pytest.fixture
def model_item():
    return ModelItem

@pytest.fixture
def rid():
    return id.rid()


@pytest.fixture
def remember_id():
    return id.remember
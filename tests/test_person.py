import pytest
from mock_examples.person import Person


@pytest.fixture
def person():
    return Person(name="Eric", age=25, address="123 Farmville Rd")


def test_person_properties(person):
    """
    Test individual properties of the Person class.
    """
    assert person.name == "Eric"
    assert person.age == 25
    assert person.address == "123 Farmville Rd"


def test_person_class_with_mock(mocker):
    """
    Test the Person class using a mock for the 'get_person_json' method to ensure it can be replaced with fake data.
    :param mocker: pytest-mock fixture
    """
    person = Person(name="Eric", age=25, address="123 Farmville Rd")
    mock_response = {"name": "FAKE_NAME", "age": "FAKE_AGE", "address": "FAKE_ADDRESS"}

    # Patch the method
    mocker.patch.object(person, "get_person_json", return_value=mock_response)

    assert person.get_person_json() == mock_response

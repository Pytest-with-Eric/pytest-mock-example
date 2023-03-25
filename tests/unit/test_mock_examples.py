import os
import time
import logging

import requests

from mock_examples.core import (
    area_of_circle,
    make_file,
    remove_file,
    sleep_for_a_bit,
    get_yo_mamma_jokes,
)

logging.basicConfig(level=logging.INFO)


def test_area_of_circle():
    assert area_of_circle(5) == 78.53975


def test_area_of_circle_with_mock(mocker):
    mocker.patch("mock_examples.core.PI", 3.0)
    assert area_of_circle(5) == 75.0


def test_make_file():
    make_file(filename="delete_me.txt")
    assert os.path.isfile("delete_me.txt")


def test_make_file_with_mock(mocker):
    filename = "delete_me.txt"

    # Mock the 'open' function call to return a file object.
    mock_file = mocker.mock_open()
    mocker.patch("builtins.open", mock_file)

    # Call the function that creates the file.
    make_file(filename)

    # Assert that the 'open' function was called with the expected arguments.
    mock_file.assert_called_once_with(filename, "w")

    # Assert that the file was written to with the expected text.
    mock_file().write.assert_called_once_with('hello')

    # In this example, we define a create_file function that takes a filename and creates a file with that name,
    # writing the string 'hello world' to the file. We then write a test function test_create_file that calls
    # create_file with a test filename and uses pytest-mock to mock the open function call within create_file.
    #
    # We use mocker.mock_open() to create a mock file object that we can use to assert that the open function was
    # called with the expected arguments and that the file was written to with the expected text. We then use
    # mocker.patch() to replace the open function call within create_file with our mock file object.
    #
    # Finally, we use assert_called_once_with to assert that the open function was called with the expected filename
    # and mode, and that the write method of the mock file object was called with the expected text.
    #
    # This approach allows us to test the behavior of code that creates files without actually creating files on disk.


def test_remove_file():
    make_file(filename="delete_me.txt")
    remove_file(filename="delete_me.txt")
    assert not os.path.isfile("delete_me.txt")


def test_sleep_for_a_bit_with_mock(mocker):
    mocker.patch("mock_examples.core.time.sleep")
    sleep_for_a_bit(duration=5)
    time.sleep.assert_called_once_with(5)  # check that time.sleep was called with the correct argument


def test_get_yo_mamma_jokes():
    response = get_yo_mamma_jokes()
    logging.info(response)


def test_get_yo_mamma_jokes_with_mock(mocker):
    mock_response = {"joke": "Yo mamma so ugly she made One Direction go another direction."}
    mocker.patch("mock_examples.core.requests.get").return_value.json.return_value = mock_response
    response = get_yo_mamma_jokes()
    requests.get.assert_called_once_with(
        "https://api.yomomma.info/")  # check that requests.get was called with the correct URL
    assert response == mock_response  # check that the result is the expected mock response
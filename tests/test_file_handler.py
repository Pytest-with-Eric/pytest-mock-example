import os
from mock_examples.file_handler import create_file, remove_file


def test_create_file():
    """
    Function to test make file
    """
    create_file(filename="delete_me.txt")
    assert os.path.isfile("delete_me.txt")


def test_create_file_with_mock(mocker):
    """
    Function to test make file with mock
    """
    filename = "delete_me.txt"

    # Mock the 'open' function call to return a file object.
    mock_file = mocker.mock_open()
    mocker.patch("builtins.open", mock_file)

    # Call the function that creates the file.
    create_file(filename)

    # Assert that the 'open' function was called with the expected arguments.
    mock_file.assert_called_once_with(filename, "w")

    # Assert that the file was written to with the expected text.
    mock_file().write.assert_called_once_with("hello")


def test_remove_file():
    """
    Function to test remove file
    """
    create_file(filename="delete_me.txt")
    remove_file(filename="delete_me.txt")
    assert not os.path.isfile("delete_me.txt")


def test_remove_file_with_mock(mocker):
    """
    Test the removal of a file using mocking to avoid actual file system operations.
    """
    filename = "delete_me.txt"

    # Mock os.remove to test file deletion without deleting anything
    mock_remove = mocker.patch("os.remove")

    # Mock os.path.isfile to control its return value
    mocker.patch("os.path.isfile", return_value=False)

    # Mock open for the create_file function
    mocker.patch("builtins.open", mocker.mock_open())

    # Simulate file creation and removal
    create_file(filename)
    remove_file(filename)

    # Assert that os.remove was called correctly
    mock_remove.assert_called_once_with(filename)

    # Assert that os.path.isfile returns False, simulating that the file does not exist
    assert not os.path.isfile(filename)

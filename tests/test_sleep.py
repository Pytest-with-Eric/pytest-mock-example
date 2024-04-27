import time
from mock_examples.sleep_function import sleep_for_a_bit


def test_sleep_for_a_bit_with_mock(mocker):
    """
    Function to test sleep for a bit with mock
    :param mocker: pytest-mock fixture
    :return: None
    """
    mocker.patch("mock_examples.sleep_function.time.sleep")
    sleep_for_a_bit(duration=5)
    time.sleep.assert_called_once_with(
        5
    )  # check that time.sleep was called with the correct argument

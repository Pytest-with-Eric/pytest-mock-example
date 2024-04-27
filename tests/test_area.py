from mock_examples.area import area_of_circle


def test_area_of_circle():
    """
    Function to test area of circle
    """
    assert area_of_circle(5) == 78.53975


def test_area_of_circle_with_mock(mocker):
    """
    Function to test area of circle with mocked PI value
    """
    mocker.patch("mock_examples.area.PI", 3.0)
    assert area_of_circle(5) == 75.0

import os


def create_file(filename: str) -> None:
    """
    Function to create a file
    :param filename: Name of the file to create
    :return: None
    """
    with open(f"{filename}", "w") as f:
        f.write("hello")


def remove_file(filename: str) -> None:
    """
    Function to remove a file
    :param filename: Name of the file to remove
    :return: None
    """
    os.remove(filename)

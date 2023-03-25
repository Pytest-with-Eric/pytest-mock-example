import os
import time
import logging
from typing import Any
import requests
import boto3

logging.basicConfig(level=logging.INFO)

PI = 3.14159


def area_of_circle(radius: float) -> float:
    """
    Function to calculate area of a cicle
    :param radius: Radius of the circle
    :return: Area of the circle
    """
    return PI * radius * radius


def make_file(filename: str) -> None:
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


def sleep_for_a_bit(duration: int) -> None:
    """
    Function to Sleep for a bit
    :param duration: Duration to sleep for
    :return: None
    """
    time.sleep(duration)


def get_yo_mamma_jokes() -> Any | None:
    """
    Function to get yo mamma jokes from an API
    :return: Response from the API
    """
    response = requests.get("https://api.yomomma.info/")
    return response.json()


class Person:
    def __init__(self, name: str, age: str | int = None, address: str = None) -> None:
        self.name = name
        self.age = age
        self.address = address

    @property
    def get_name(self) -> str:
        return self.name

    @property
    def get_age(self) -> str:
        return self.age

    @property
    def get_address(self) -> str:
        return self.address

    @property
    def get_person_json(self) -> dict[str, Any]:
        return {"name": self.name, "age": self.age, "address": self.address}


def get_my_object(bucket: str, key: str) -> Any | None:
    """
    Function to get an object from S3
    :param bucket: Bucket name
    :param key: Key name
    :return: Response from S3
    """
    s3_client = boto3.client("s3")
    response = s3_client.get_object(Bucket=bucket, Key=key)
    return response

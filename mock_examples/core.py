import os
import time
from typing import Any
import requests

PI = 3.14159


def area_of_circle(radius: float) -> float:
    return PI * radius * radius


def make_file(filename: str) -> None:
    with open(f"{filename}", "w") as f:
        f.write("hello")


def remove_file(filename: str) -> None:
    os.remove(filename)


def sleep_for_a_bit(duration: int) -> None:
    time.sleep(duration)


def get_yo_mamma_jokes() -> Any | None:
    response = requests.get("https://api.yomomma.info/")
    return response.json()

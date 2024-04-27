from typing import Dict


class Person:
    def __init__(self, name: str, age: int = None, address: str = None) -> None:
        self._name = name
        self._age = age
        self._address = address

    @property
    def name(self) -> str:
        return self._name

    @property
    def age(self) -> int:
        return self._age

    @property
    def address(self) -> str:
        return self._address

    def get_person_json(self) -> Dict[str, str]:
        return {"name": self._name, "age": self._age, "address": self._address}

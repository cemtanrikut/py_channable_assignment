import abc
import csv
from typing import Iterator, Any, Dict, Tuple
from enum import Enum, auto

class ProductStreamProcessor(metaclass=abc.ABCMeta):
    def __init__(self, path_to_before_csv: str, path_to_after_csv: str) -> None:
        self.path_to_before_csv = path_to_before_csv
        self.path_to_after_csv = path_to_after_csv

    @abc.abstractmethod
    def main(self) -> Iterator[Tuple[Operation, str, Dict[str, Any] | None]]:
        pass

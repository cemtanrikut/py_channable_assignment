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
        # The reason why I do not pass the main method and implement it in the 
        # ProductDiffer class is to ensure the correct use of abstract classes and methods.

class ProductDiffer(ProductStreamProcessor):
    def read_csv(self, path: str) -> Dict[str, Dict[str, Any]]:
        products = {}
        with open(path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                products[row['id']] = row
        return products
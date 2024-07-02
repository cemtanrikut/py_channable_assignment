import abc
import csv
from typing import Iterator, Any, Dict, Tuple
from enum import Enum, auto

class Operation(Enum):
    CREATE = auto()
    UPDATE = auto()
    DELETE = auto()

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
    def main(self) -> Iterator[Tuple[Operation, str, Dict[str, Any] | None]]:
        before_products = self.read_csv(self.path_to_before_csv)
        after_products = self.read_csv(self.path_to_after_csv)

        before_ids = set(before_products.keys())
        after_ids = set(after_products.keys())

        for product_id in after_ids - before_ids:
            yield (Operation.CREATE, product_id, after_products[product_id])

        for product_id in before_ids - after_ids:
            yield (Operation.DELETE, product_id, None)

        for product_id in before_ids & after_ids:
            if before_products[product_id] != after_products[product_id]:
                yield (Operation.UPDATE, product_id, after_products[product_id])
            
# Instantiate and run the ProductDiffer with provided CSV paths
if __name__ == '__main__':
    differ = ProductDiffer('data/product_inventory_before.csv', 'data/product_inventory_after.csv')
    for operation in differ.main():
        print(operation)
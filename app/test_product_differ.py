import unittest
from app.channable_assignment_python import Operation, ProductDiffer

class TestProductDiffer(unittest.TestCase):
    def setUp(self):
        self.before_csv = 'product_inventory_before.csv'
        self.after_csv = 'product_inventory_after.csv'
        self.before_data = """id,title,price
1,Product A,10
2,Product B,20
3,Product C,30
"""
        self.after_data = """id,title,price
1,Product A,10
2,Product B,25
4,Product D,40
"""

        with open(self.before_csv, 'w') as file:
            file.write(self.before_data)

        with open(self.after_csv, 'w') as file:
            file.write(self.after_data)

    def tearDown(self):
        import os
        os.remove(self.before_csv)
        os.remove(self.after_csv)

    def test_create_operation(self):
        differ = ProductDiffer(self.before_csv, self.after_csv)
        operations = list(differ.main())
        create_operations = [op for op in operations if op[0] == Operation.CREATE]
        self.assertEqual(len(create_operations), 1)
        self.assertEqual(create_operations[0], (Operation.CREATE, '4', {'id': '4', 'title': 'Product D', 'price': '40'}))

    def test_delete_operation(self):
        differ = ProductDiffer(self.before_csv, self.after_csv)
        operations = list(differ.main())
        delete_operations = [op for op in operations if op[0] == Operation.DELETE]
        self.assertEqual(len(delete_operations), 1)
        self.assertEqual(delete_operations[0], (Operation.DELETE, '3', None))

    def test_update_operation(self):
        differ = ProductDiffer(self.before_csv, self.after_csv)
        operations = list(differ.main())
        update_operations = [op for op in operations if op[0] == Operation.UPDATE]
        self.assertEqual(len(update_operations), 1)
        self.assertEqual(update_operations[0], (Operation.UPDATE, '2', {'id': '2', 'title': 'Product B', 'price': '25'}))

if __name__ == '__main__':
    unittest.main()

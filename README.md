# Product Differ Application

This Python application compares product data from two CSV files and generates operations (CREATE, UPDATE, DELETE) based on changes between them.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Product Differ application compares two CSV files containing product data (product_inventory_before.csv and product_inventory_after.csv). It identifies products that are new, updated, or deleted between the two datasets. This tool is useful for eCommerce platforms to synchronize product updates across marketing channels efficiently.

## Installation

- Clone the repository:
```bash
git clone https://github.com/cemtanrikut/py_channable_assignment.git
cd py_channable_assignment
```

## Usage

- Prepare CSV files:

Place your CSV files in the data/ directory:

data/product_inventory_before.csv: Contains product data from the previous day.

data/product_inventory_after.csv: Contains updated product data for the current day.

- Run the application:

```bash
python app/main.py
```

This command executes the main script of the application, comparing the two CSV files and generating operations based on changes.

- View the output:

The application will print or output operations (CREATE, UPDATE, DELETE) to the console or generate output files as specified.

## Testing

To run tests for the application, follow these steps:

- Navigate to the correct directory:

```bash
cd tests
```

- Run tests using unittests:

```bash
python3 -m unittest test_product_differ.py
```

This command automatically discovers and runs all test cases in files named test*.py in the current directory and its subdirectories.

## File Structure

The structure of the project is as follows:

```css
product-differ/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── channable_assignment_python.py
│   └── test_product_differ.py
│
└── data/
    ├── product_inventory_before.csv
    └── product_inventory_after.csv
```

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these guidelines:

- Fork the repository and create a new branch.
- Make your changes and ensure tests pass.
- Submit a pull request with a clear description of your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
# Template for Pipenv

- Pipenv environment
- unittest OK

# Directory Structure
```
.
├── .venv
├── lib
│   ├── __init__.py
│   └── mylib.py
├── tests
│   ├── __init__.py
│   └── test_mylib.py
├── main
│   ├── __init__.py
│   └── hello.py
├── .gitignore
├── Pipfile
└── README.md
```

# Usage

## RUN
```pipfile
[scripts]
commands = "python -m main.path.to.module"
```
```bash
$ pipenv run commands
```

## TEST
```py
from unittest import TestCase
from lib import mylib


class TestMyLib(TestCase):


    def test_mylib(self):
        self.assertEqual(mylib.mylib(), "This is My Test Library!")
```
```bash
$ pipenv run test tests.path.to.test # python -m unittest
```
or
```bash
$ pipenv run testall # python -m unittest discover
```

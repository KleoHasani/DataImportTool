<p align="center">
	<img src="docs/assets/logo.png" width="200" height="100">
</p>

---

# DataImport

## Description

Import data from CSV, and XLSX fiiles to MySQL database. 

---

## Table of Contents

- [Getting Started](#getting-started)
  - [Requirements](#requirements)
  - [Installation](#installation)
    - [Clone](#clone)
    - [Set-Up](#set-up)
      - [VENV](#venv)
      - [ENV](#env)
    - [Install](#install)
  - [Test](#test)
- [Authors](#authors)
- [Usage](#usage)

---

## Getting Started

- ## Requirements

  - [x] Python3 v3.9.5

- ## Installation

  - ### Clone

    ```shell
    git clone https://github.com/csdcti/DataImport.git
    ```

  - ### Set-Up

    - #### VENV
      ```shell
      python3 -m venv env
      ```

      __Set your shell to use the venv paths for Python by activating the virtual environment.__

      - macOS
        ```shell
        source env/bin/activate
        ```

      - Windows
        ```shell
        .\env\Scripts\activate
        ```

      - Linux
        ```shell
        source env/bin/activate
        ```
    - #### ENV
      ```env
      DB_HOST="localhost"
      DB_USER="rootforexample"
      DB_PASSWORD="yourrootpasswordforexample"
      DB_NAME="MalwareDesign"
      ```

  - ### Install
  ```python3
  pip install -r requirements.txt
  ```

  - ### Start
  ```python3
  python3 ./src/main.py <command> <path>
  ```

  - ### Stop
    __Write to Requirements.txt. (If new packages were installed).__
      ```python
      pip3 freeze > requirements.txt
      ```

    __Disable venv for the project.__
    ```shell
    deactivate
    ```
  
---

## Usage
__Read from CSV file__
```python3
python3 ./src/main.py -c <path>
```

```python3
python3 ./src/main.py --csv <path>
```

__Read from XLSX file__
```python3
python3 ./src/main.py -x <path>
```

```python3
python3 ./src/main.py --xslx <path>
```

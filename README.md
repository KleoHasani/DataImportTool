# DataImportTool

## Description

Python tool to import data from CSV and XLSX files to MySQL database.

---

## Table of Contents

- [Getting Started](#getting-started)
  - [Requirements](#requirements)
  - [Installation](#installation)
    - [Clone](#clone)
    - [Set-Up](#set-up)
      - [VENV](#venv)
    - [Install](#install)
    - [Stop](#stop)
- [Build](#build)
- [Usage](#usage)
- [Test](#test)
- [Create Executable](#create-executable)
- [Run Executable](#run-executable)

---

## Getting Started

- ## Requirements

  - [x] Python3 v3.9.5

- ## Installation

  - ### Clone

    ```shell
    git clone https://github.com/csdcti/DataImportTool.git
    ```

  - ### Set-Up

    - #### VENV

      ```shell
      python3 -m venv env
      ```

      **Set your shell to use the venv paths for Python by activating the virtual environment.**

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

  - ### Install

  ```python3
  pip install -r requirements.txt
  ```

  - ### Stop

    **Write to Requirements.txt. (If new packages were installed).**

    ```python
    pip3 freeze > requirements.txt
    ```

    **Disable venv for the project.**

    ```shell
    deactivate
    ```

---

## Build

```shell
pip install .
```

---

## Usage

Setup config file.

```shell
dit config
```

Run.

```shell
dit run <mock_file_path> <data_file_path>
```

---

## Test

```shell
pytest
```

| File         | Test             | Description | Status   |
| :----------- | :--------------- | :---------- | :------- |
| test_true.py | test_always_true | Mock test.  | &#10003; |

---

 ## Create Executable
 - Windows
 
 ```shell
 pyinstaller src\main.py
 ```
 
 check that it's working 
 
  ```shell
  cd dist
  ```
 
  ```shell 
  cd main
  ```
 
  ```shell
  main.exe
  ```
 ---
 
 ## Run Executable

- unzip folder
 
- run executable from inside folder
 
   ```shell
   cd path\to\folder
   ```
 
  ```shell
  main.exe
  ```
 

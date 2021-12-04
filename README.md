<p align="center">
	<img src="docs/assets/logo.png" width="200" height="100">
</p>

---

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
    - [Start](#start)
    - [Stop](#stop)
- [Build](#build)
- [Usage](#usage)
- [Test](#test)

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

  - ### Start

  \*Nix

  ```python3
  python3 src/main.py
  ```

  Windows

  ```python3
  python3 src\main.py
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

```shell
dit
```

---

## Test

| File         | Test             | Description | Status   |
| :----------- | :--------------- | :---------- | :------- |
| test_true.py | test_always_true | Mock test.  | &#10003; |

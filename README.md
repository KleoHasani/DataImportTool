<p align="center">
	<img src="docs/assets/logo.png" width="150" height="200">
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

    __Set-up venv__
    ```shell
    python3 -m venv env
    ```

    __Enable venv for the project.__

    Set your shell to use the venv paths for Python by activating the virtual environment.

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

    __Disable venv for the project.__
    ```
    deactivate
    ```

  - ### Install
  ```python3
  pip install -r requirements.txt
  ```

  - ### Start
  ```python3
  python3 ./src/main.py <command> <path>
  ```
  
---

## Usage


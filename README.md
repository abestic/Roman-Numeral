# Roman Numeral

BDD, TDD, and the Test Pyramid in practice

## Overview

### Purpose

Roman Numeral aims to provide a working example of the red-green-refactor cycle, in conjunction with the ideas of testing granularity found in the Test Pyramid.

It showcases how BDD (for functional tests) and TDD (for unit tests) practices can assist one-another to construct a quality solution, without over-engineering it.

## Contributing

Propose your change in an issue, or directly create a pull request with your improvements.

### Running the application locally

After cloning this repository, you can test-drive (and contribute to) the app locally assuming you have python3 installed.

* Setup a virtual environment for this project: `pthon -m venv venv`
* Enter the virtual environment: `source /venv/bin/activate`
* Install dependencies: `pip install -r requirement.txt`
* Start the application: `python roman.py`
* Run unit tests: `python test.py`
* Run functional tests: `behave` 
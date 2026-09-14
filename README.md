# Billing Utils

A small Python module for calculating account balances, including
support for late-payment fees.

## Installation

pip install -e .

## Usage

from billing import apply_late_fee
apply_late_fee(100.0, days_overdue=5)

## Running Tests

pytest -v

## License

Distributed under the MIT License. See LICENSE for details.

## Contributing

Contributors should create a feature branch and open a pull request.



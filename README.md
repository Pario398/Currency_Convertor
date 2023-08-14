# Currency Converter

This script is a Currency Exchange Rate Calculator that allows users to convert between different currencies using Yahoo Finance. It provides the ability to perform currency conversions, view a list of example currencies and their abbreviations, and exit the program.

## Table of Contents
- [How to Use](#how-to-use)
- [Functions](#functions)
- [Example Use](#example-use)

## How to Use

1. Install the required package by running the following command:
   ```bash
   pip install yfinance
   ```
2. Copy and paste the provided code into a Python script (e.g., Converter.py).
3. The program will display a menu with the following options:
    * Convert two currencies
    * Show example currencies
    * Exit
Select an option by entering the corresponding number.
4. Follow the prompts to perform currency conversions or view example currencies.

## Functions

**exchange(fromcurrency, tocurrency, quantity):**
This function converts a given quantity of one currency to another using the latest exchange rate retrieved from Yahoo Finance.

**show_currencies():**

This function displays a list of example currencies with their abbreviations and full names.

## Example Use
```bash
Currency Exchange Rate Calculator:
1. Convert two currencies
2. Help (Show example currencies)
3. Exit
Enter your choice: 1
Enter the base currency: GBP
Enter the target currency: INR
Enter the quantity of the base currency: 2.2
[*********************100%%**********************]  1 of 1 completed
2.2 GBP = 232.05 INR

```

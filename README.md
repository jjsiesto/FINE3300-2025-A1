FINE3300-2025-A1: MortgagePayment & ExchangeRates
This repository contains the solution for Assignment #1 in FINE 3300 (Fall 2025). It includes two Python modules: a mortgage payment calculator (MortgagePayment.py) and a currency converter for USD/CAD exchange rates (ExchangeRates.py).

Project Overview
This project consists of two main components:

Mortgage Payment Calculator (MortgagePayment.py): A MortgagePayment class that calculates various mortgage payment schedules (monthly, semi-monthly, bi-weekly, weekly, and accelerated options) for Canadian fixed-rate mortgages. The calculations are based on user-provided principal, quoted interest rate, and amortization period.

Currency Converter (ExchangeRates.py): An ExchangeRates class that reads the latest USD/CAD exchange rate from a Bank of Canada CSV file to perform currency conversions. The class is designed to read the data file only once for efficiency.

How to Run the Scripts
Ensure you have Python 3 installed. You can run each script from your terminal. You will also need the BankOfCanadaExchangeRates.csv file in the same directory or provide a valid path to it when prompted.

Mortgage Calculator
To run the mortgage calculator, execute the following command:

python mortgage.py

The script will prompt you to enter the principal amount, the quoted annual interest rate (e.g., 5.5), and the amortization period in years.

Example Output: ($500,000 principal at 5.5% interest for 25 years)

Monthly Payment: 3051.96
Semi-Monthly Payment: 1524.25
Bi-Weekly Payment: 1406.88
Accelerated Bi-Weekly Payment: 1525.98
Weekly Payment: 703.07
Accelerated Weekly Payment: 762.99

Currency Converter
To run the currency converter, execute the following command:

python Converter.py

The script will prompt you for the path to the CSV file, the amount to convert, the source currency (USD or CAD), and the target currency.

Note: The converter only accpets USD and CAD values and will reject other currency codes. 
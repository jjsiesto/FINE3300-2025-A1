<h1>FINE3300-2025-A1: Mortgage Payment & Exchange Rates</h1>

This repository contains the solution for Assignment #1 in FINE 3300 (Fall 2025). It includes two Python modules: a mortgage payment calculator (MortgagePayment.py) and a currency converter for USD/CAD exchange rates (ExchangeRates.py).

<h2>Project Overview</h2>

__This project consists of two main components:__

Mortgage Payment Calculator (MortgagePayment.py): A MortgagePayment class that calculates various mortgage payment schedules (monthly, semi-monthly, bi-weekly, weekly, and accelerated options) for Canadian fixed-rate mortgages. The calculations are based on user-provided principal, quoted interest rate, and amortization period.

Currency Converter (ExchangeRates.py): An ExchangeRates class that reads the latest USD/CAD exchange rate from a Bank of Canada CSV file to perform currency conversions. The class is designed to read the data file only once for efficiency.

<h2>How to Run the Scripts</h3  >

Ensure you have Python 3 installed. You can run each script from your terminal. You will also need the BankOfCanadaExchangeRates.csv file in the same directory or provide a valid path to it when prompted.

<h4>Mortgage Calculator</h4>

To run the mortgage calculator, execute the following command:

python MortgagePayment.py

The script will prompt you to enter the principal amount, the quoted annual interest rate (e.g., 5.5), and the amortization period in years.

Example Output: ($500,000 principal at 5.5% interest for 25 years)

Monthly Payment: 3051.96 <br>
Semi-Monthly Payment: 1524.25 <br>
Bi-Weekly Payment: 1406.88 <br>
Accelerated Bi-Weekly Payment: 1525.98 <br>
Weekly Payment: 703.07 <br>
Accelerated Weekly Payment: 762.99 <br>

__Currency Converter__

To run the currency converter, execute the following command:

python ExchangeRates.py

The script will prompt you for the path to the CSV file, the amount to convert, the source currency (USD or CAD), and the target currency.

Example Output: ($100,000 CAD to USD and vice versa)

100000.00 CAD is approximatly 73003.36 USD <br>
100000.00 USD is approximatly 136980.00 CAD

Note: The converter only accpets USD and CAD values and will reject other currency types. 
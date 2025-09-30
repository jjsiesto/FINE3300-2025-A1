import csv
import sys

class ExchangeRates: 
    """
    Reads Bank of Canada exchange rates from a CSV file to perform 
    currency conversions between CAD and USD

    The Class is designed to read and parse the file only once upon 
    instantiation, storing the latest echange rate for efficient reuse. 
    """
    def __init__(self, file_path: str):
        """
        Initializes the converter by reading the specified CSV file
        
        Arguments: 
            file_path : The path to the BankOfCanadaExchangeRates.csv file

        Raises: 
            FileNotFoundError : If the specified file does not exist
            ValueError : If the file format is incorrect or data is invalid  
        """
        self.usd_cad_rate = None
        try: 
            with open(file_path, mode='r') as file:
                reader = csv.reader(file)

                # Read the header row to identify columns
                headers = next(reader)
                try: 
                    #Find the index for the USD to CAD exchange rate
                    # The specific column name in the provided file is "USDCAD"
                    usd_cad_index = headers.index("USD/CAD")
                except ValueError:
                    raise ValueError("The required 'USDCAD' column is missing in the CSV file.")
                
                # Read the last row to get the latest exchange rate
                last_row = None
                for row in reader:
                    if row: #Ensure the row is not empty
                        last_row = row
                if last_row: 
                    self.usd_cad_rate = float(last_row[usd_cad_index])
                else:
                    raise ValueError("The CSV file is empty or does not contain valid data.")
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.", file=sys.stderr)
            raise   

    def convert(self, amount: float, from_currency: str, to_currency: str) -> float:
        """
        Converts an amount from one currency to another
        
        Arguments:
            amount : The amount of money to convert
            from_currency : The currency code of the original amount ('CAD' or 'USD')
            to_currency : The currency code to convert to ('CAD' or 'USD')
        
        Returns:
            The converted amount in the target currency
        Raises:
            ValueError : If an unsupported currency code is provided
        """
        #Normalize currency codes to uppercase
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        if from_currency not in ['CAD', 'USD'] or to_currency not in ['CAD', 'USD']:
            raise ValueError("Unsupported currency code. Use 'CAD' or 'USD'.")
        if from_currency == to_currency:
            return amount #No conversion needed
        if from_currency == 'USD' and to_currency == 'CAD':
            return amount * self.usd_cad_rate
        if from_currency == 'CAD' and to_currency == 'USD':
            return amount / self.usd_cad_rate

def run_exchange_rate_conversion():
    # Path to the CSV file
    file_path = input("Enter the path to the BankOfCanadaExchangeRates.csv file: ")
    try:
        converter = ExchangeRates(file_path=file_path)
        amount = float(input("Enter the amount to convert: "))
        from_currency = input("Enter the currency to convert from (CAD or USD): ")
        to_currency = input("Enter the currency to convert to (CAD or USD): ")
        result = converter.convert(amount, from_currency, to_currency) 
        print(f"\n {amount} {from_currency} is approximatly {result:.2f} {to_currency}")
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: Could not perform conversion. {e}", file=sys.stderr)


if __name__ == "__main__":
    run_exchange_rate_conversion()
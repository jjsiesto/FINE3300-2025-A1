#==========================================================================================
# FINE 3300 (Fall 2025): Assignment 1 - Mortgage Payments 
#
# This Script defines a Python Class, 'Mortgage Payment', designed to model and calulate 
# various payment schemes for a Canadian fixed-rate mortgage.
#==========================================================================================


class MortgagePayment: 

    """
    Calculates various mortgage payment schedules based on a quoted interest rate
    and amortization period.

    The class pre-calculates periodic interest rates upon initialization for
    efficiently computing payment schedules for any given principal amount.
    """
    def __init__(self, quoted_interest_rate, amortization_years):
        """
        Initializes the mortgage calulator with it's fixed parameters.
        Arguments:
            quoted_interest_rate (float): The annual interest rate as a decimal (e.g., 5.5 for 5.5%).
            amortization_years (int): The total amortization period in years.
        """
        # Per Canadain Mortage rules, the quoted rate is compounded semi-annually
        self.quoted_interest_rate = quoted_interest_rate/100 # /100 to convert percentage to decimal
        self.amortization_years = amortization_years

        # Pre-calculate periodic interest rates and assign pre-calculated rates to instance variables for easy access
        # Created as a private method since they are not intended to be accessed directly outside the class
        
        def _period_rate(quoted_interest_rate, periods_per_year):
            r = ((1+(quoted_interest_rate/2))**(2/periods_per_year))-1
            return r
        self.monthly_rate = _period_rate(self.quoted_interest_rate, 12)
        self.semi_monthly_rate = _period_rate(self.quoted_interest_rate, 24)
        self.bi_weekly_rate = _period_rate(self.quoted_interest_rate, 26)
        self.weekly_rate = _period_rate(self.quoted_interest_rate, 52)
       
        # Accelerated payments are simply fractions of the monthly payment
        # (i.e. half for bi-weekly, quarter for weekly) and do not need separate rates
  
    # Method to calculate payment based on principal, periodic interest rate, and payments per year

    def calculate_payment(self, principal, rate, m):
        n = self.amortization_years * m
        if rate == 0:
            return principal/n
        payment = (principal * rate)/(1-(1+rate)**-n)
        return payment

    # Method to compute all payment schemes for a given principal, returning them as a tuple

    def payments (self, principal):
        monthly = self.calculate_payment(principal, self.monthly_rate, 12)
        semi_monthly = self.calculate_payment(principal, self.semi_monthly_rate, 24)
        bi_weekly = self.calculate_payment(principal, self.bi_weekly_rate, 26)
        accelerated_bi_weekly = monthly/2  
        weekly = self.calculate_payment(principal, self.weekly_rate, 52)
        accelerated_weekly = monthly/4
        return (monthly, semi_monthly, bi_weekly, accelerated_bi_weekly, weekly, accelerated_weekly )


#==========================================================================================
# Main Execution Block
#==========================================================================================
if __name__ == "__main__":
    # This block serves as the entry point for the script when executed directly.
    # It prompts the user for mortgage parameters and displays the calculated payment schemes.


    # 1. Gather user input for principal, interest rate, and amortization term 
    principal_amount = float(input("Enter principal amount:"))
    quoted_interest_rate = float(input("Enter quoted interest rate (as a decimal ie: 5.5 for 5.5%):"))
    amortization_years = int(input("Enter ammortization term (in years):"))

    # 2. Create an instance of MortgagePayment and compute payments
    mortgage_secario = MortgagePayment(quoted_interest_rate=quoted_interest_rate, amortization_years=amortization_years)
    payment_values = mortgage_secario.payments(principal=principal_amount)


    # 3. Display the formatted results to the user, accurate to two decimal places
    print(f"Monthly Payment: {payment_values[0]:.2f}")
    print(f"Semi-Monthly Payment: {payment_values[1]:.2f}")
    print(f"Bi-Weekly Payment: {payment_values[2]:.2f}")
    print(f"Accelerated Bi-Weekly Payment: {payment_values[3]:.2f}")
    print(f"Weekly Payment: {payment_values[4]:.2f}")
    print(f"Accelerated Weekly Payment: {payment_values[5]:.2f}")
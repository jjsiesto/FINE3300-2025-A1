#==========================================================================================
# FINE 3300 (Fall 2025): Assignment 1 - Mortgage Payments 
#
# This Script defines a Python Class, 'Mortgage Payment', designed to model and calulate 
# various payment schemes for a Canadian fixed-rate mortgage.
#==========================================================================================


class MortgagePayment: 

    """
    Represents a mortgage calculator defined by its interest rate and amortization period.
    For efficiency , all periodic interest rates are pre-calculated upon instantiation.
    The instance can then compute payment schedules for any principal.
    """
    def __init__(self, quoted_interest_rate, ammortization_years):

        """
        Initializes the mortgage calulator with it's fixed parameters.
        Arguments:
            quoted_interest_rate (float): The annual interest rate as a decimal (e.g., 5.5 for 5.5%).
            ammortization_years (int): The total amortization period in years.
        """

        self.quoted_interest_rate = quoted_interest_rate/100 # /100 to convert percentage to decimal
        self.ammortization_years = ammortization_years

        # Pre-calculate periodic interest rates
        def r_period(quoted_interest_rate, periods_per_year):
            r = ((1+(quoted_interest_rate/2))**(2/periods_per_year))-1
            return r
        self.r_monthlly = r_period(self.quoted_interest_rate, 12)
        self.r_semi_monthly = r_period(self.quoted_interest_rate, 24)
        self.r_bi_weekly = r_period(self.quoted_interest_rate, 26)
        self.r_accelerated_bi_weekly = self.r_monthlly/2
        self.r_weekly = r_period(self.quoted_interest_rate, 52)
        self.r_accelerated_weekly = self.r_monthlly/4

    # Method to calculate payment based on principal, periodic interest rate, and payments per year

    def calulate_payment(self, principal, r, m):
        n = self.ammortization_years * m
        if r==0:
            return principal/n
        payment = (principal * r)/(1-(1+r)**-n)
        return payment

    # Method to compute all payment schemes for a given principal, returning them as a tuple

    def _payments (self, principal):
        monthly = self.calulate_payment(principal, self.r_monthlly, 12)
        semi_monthly = self.calulate_payment(principal, self.r_semi_monthly, 24)
        bi_weekly = self.calulate_payment(principal, self.r_bi_weekly, 26)
        accelerated_bi_weekly = monthly/2  
        weekly = self.calulate_payment(principal, self.r_weekly, 52)
        accelerated_weekly = monthly/4
        return (monthly, semi_monthly, bi_weekly, accelerated_bi_weekly, weekly, accelerated_weekly )


#==========================================================================================
# Main Execution Block
#==========================================================================================
if __name__ == "__main__":
    # This block serves as the entry point for the script when executed directly.
    # It prompts the user for mortgage parameters and displays the calculated payment schemes.


    # 1. Gather user input for principal, interest rate, and amortization term 
    p = float(input("Enter principal amount:"))
    i = float(input("Enter quoted interest rate (as a decimal ie: 5.5 for 5.5%):"))
    t = int(input("Enter ammortization term (in years):"))

    # 2. Create an instance of MortgagePayment and compute payments
    mortgage_secario = MortgagePayment(quoted_interest_rate=i, ammortization_years=t)
    payment_values = mortgage_secario.payments(principal=p)

    # 3. Display the formatted results to the user, accurate to two decimal places
    print(f"Monthly Payment: {payment_values[0]:.2f}")
    print(f"Semi-Monthly Payment: {payment_values[1]:.2f}")
    print(f"Bi-Weekly Payment: {payment_values[2]:.2f}")
    print(f"Accelerated Bi-Weekly Payment: {payment_values[3]:.2f}")
    print(f"Weekly Payment: {payment_values[4]:.2f}")
    print(f"Accelerated Weekly Payment: {payment_values[5]:.2f}")
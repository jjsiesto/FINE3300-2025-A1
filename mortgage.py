def PVA(rate: float, periods: int) -> float: 
    """monthly payment for a present value annuity"""
    if periods == 0: 
        return 0
    if rate == 0: 
        return float(periods) 
    return (1-(1+rate) ** (-periods)) / rate
def 
class mortgage:

    def __init__(self,home_cost,down_payment_fraction,annual_interest_rate):
        self.home_cost = home_cost
        self.down_payment_fraction = down_payment_fraction
        self.annual_interest_rate = annual_interest_rate
        #self.principle= home_cost - loan_amount

    def calcDownPayment(self):
        return self.home_cost*self.down_payment_fraction
    
    def calcLoanAmount(self):
        return self.home_cost*(1-self.down_payment_fraction)
    
    def calcMonthlyInterestRate(self):
        return self.annual_interest_rate/12
    
    

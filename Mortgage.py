class mortgage:

    def __init__(self,home_cost,down_payment_fraction,interest_rate):
        self.home_cost = home_cost
        self.down_payment_fraction = down_payment_fraction
        self.interest_rate = interest_rate
        #self.principle= home_cost - loan_amount

    def calcDownPayment(self):
        return self.home_cost*self.down_payment_fraction
    

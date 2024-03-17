import numpy as np
import matplotlib.pyplot as plt
from Mortgage import mortgage
import PySimpleGUI as sg

### Input Parameters
homeValue = 1e6 # Home price in dollars
downPaymentFraction = 0.25 # 
interestRate = 0.03
n_years = 50
monthly_payment = 3600
annual_increase = 1.03
annual_property_tax = 0.02
### Define a mortgage instance from the Mortgage class
house_1 = mortgage(homeValue,downPaymentFraction,interestRate)
downPayment = house_1.calcDownPayment()#homeValue*downPaymentFraction
loanAmount = house_1.calcLoanAmount()#homeValue - downPayment
interestRate_Month = house_1.calcMonthlyInterestRate()
t = np.arange(0,n_years,1) # Time years
t_months = np.arange(0,n_years*12)#t*12
###
monthly_property_tax_payment = homeValue*annual_property_tax/12
house_1 = mortgage(homeValue,downPaymentFraction,interestRate)
downPayment = house_1.calcDownPayment()#homeValue*downPaymentFraction
loanAmount = house_1.calcLoanAmount()#homeValue - downPayment
t = np.arange(0,n_years,1) # Time years
t_months = np.arange(0,n_years*12)#t*12
loanAmount_Growth=loanAmount*np.ones(len(t))
loanAmount_Growth_Month=loanAmount*np.ones(len(t_months))
interest = np.zeros(len(t))
interest_Month = np.zeros(len(t_months))
net_Remaining = np.zeros((len(t_months)))
total_payment = np.zeros((len(t_months)))
mortgage_paidOff = 'True' 
#print(loanAmount)

## Annual Interest Rate and Loan Amount Growth
# for i in range(1,len(t)):
#     interest += (interestRate)*loanAmount
#     #print(interest[i])
#     loanAmount_Growth[i] += interest[i-1]

## Monthly Interest Rate and Loan Amount Growth

#payment = (interestRate_Month)*loanAmount*(1+monthly_extra_factor)

#print(payment)
principle = loanAmount

#for i in range(1,len(t_months)):
i=0
while principle>=0:
    interest_Month[i] = (interestRate_Month)*principle

    monthly_remainder = monthly_payment-interest_Month[i]-monthly_property_tax_payment
    #print(monthly_remainder)
    if i//12 == 1:
        monthly_payment *= annual_increase
        #print(payment)
    #print(monthly_remainder)
    if monthly_remainder>0:
        principle-=monthly_remainder
        total_payment[i] = monthly_payment
    else:
        principle+=0
        total_payment[i] = monthly_payment
        #print(principle)
    if principle<=0:
        principle=0
        print(monthly_payment)
        break
    if i >= len(t_months)-1:
        mortgage_paidOff = 'False'
        break
    i+=1
    #net_Remaining[] = 
    #print(interest_Month[i])
    #loanAmount_Growth_Month+= interest_Month[i]
    

# plt.plot(t,loanAmount_Growth/1e6,marker='o',color='b',markersize=10, label='Total Amount Owed')
# plt.plot(t,(loanAmount_Growth-loanAmount_Growth[0])/1e6,marker='o',color='r',markersize=10,  label='Interest Growth')
t_finish_payment = np.min(np.argwhere(np.diff(total_payment[1:]<=0.1))) # Number of years to pay off the mortgage
plt.plot(t_months[1:1+t_finish_payment]/12,np.cumsum(interest_Month)[1:1+t_finish_payment]/1e6,marker='o',color='b',markersize=10, label='Interest Growth')
plt.plot(t_months[1:1+t_finish_payment]/12,downPayment/1e6+np.cumsum(total_payment)[1:1+t_finish_payment]/1e6,marker='o',color='r',markersize=10,  label='Total Paid, Monthly Payment: $'+str(round(monthly_payment,0)))


plt.xlabel('Time (Years)',fontsize=34)
plt.ylabel('Total Payment ($M)',fontsize=34)
plt.xticks(fontsize=26)
plt.yticks(fontsize=26)
plt.axhline(y=0, c='k')
if mortgage_paidOff == 'True':
    plt.axvline(x=t_months[np.min(np.argwhere(np.diff(total_payment[1:]<=0.1)))]/12, label=str(round(t_months[np.min(np.argwhere(np.diff(total_payment[1:]<=0.1)))]/12, 1)) + ' years')
#print(np.argwhere(np.diff(total_payment[1:]<=0.1)))
# plt.axhline(y=2*homeValue/1e6, c='k')
# plt.axhline(y=3*homeValue/1e6, c='k')
plt.legend(loc='best',fontsize=24)
plt.title('Home value:$'+str(int(homeValue))+', Loan Value:\$'+str(int(loanAmount_Growth[0]))+', Interest Rate: ' + str(round(100*interestRate,1))+'%' + ', Annual Increase: '+str(round((annual_increase-1.0)*100,1))+'%, '+'Mortgage Paid?: '+str(mortgage_paidOff), fontsize=20)
plt.grid(True)
plt.show()

## Do something 
## Add monthly payment
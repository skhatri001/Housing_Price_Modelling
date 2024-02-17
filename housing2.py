import numpy as np
import matplotlib.pyplot as plt
from Mortgage import mortgage
import PySimpleGUI as sg

### Input Parameters
homeValue = 1e6 # Home price in dollars
downPaymentFraction = 0.50 # 
interestRate = 0.07
interestRate_Month = interestRate/12
n_years = 50
monthly_extra_factor = 0.6
annual_increase = 1.01
annual_property_tax = 0.02
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
#print(loanAmount)

## Annual Interest Rate and Loan Amount Growth
# for i in range(1,len(t)):
#     interest += (interestRate)*loanAmount
#     #print(interest[i])
#     loanAmount_Growth[i] += interest[i-1]

## Monthly Interest Rate and Loan Amount Growth

payment = (interestRate_Month)*loanAmount*(1+monthly_extra_factor)

#print(payment)
principle = loanAmount

for i in range(1,len(t_months)):
    interest_Month[i] = (interestRate_Month)*principle

    monthly_remainder = payment-interest_Month[i]-monthly_property_tax_payment
    print(monthly_remainder)
    if i//12 == 1:
        payment *= annual_increase
        #print(payment)
    #print(monthly_remainder)
    if monthly_remainder>0:
        principle-=monthly_remainder
        total_payment[i] = payment
        #print(principle)
    if principle<=0:
        principle=0
        break
    #net_Remaining[] = 
    #print(interest_Month[i])
    #loanAmount_Growth_Month+= interest_Month[i]
    

# plt.plot(t,loanAmount_Growth/1e6,marker='o',color='b',markersize=10, label='Total Amount Owed')
# plt.plot(t,(loanAmount_Growth-loanAmount_Growth[0])/1e6,marker='o',color='r',markersize=10,  label='Interest Growth')

#plt.plot(t_months/12,interest_Month,marker='o',color='b',markersize=10, label='Total Amount Remaining')
plt.plot(t_months[1:]/12,np.cumsum(total_payment)[1:]/1e6,marker='o',color='r',markersize=10,  label='Final Monthly Payment is $'+str(round(payment,1)) + ', '+str(int(monthly_extra_factor*100))+'%')


plt.xlabel('Time (Years)',fontsize=40)
plt.ylabel('Mortgage Payment ($M)',fontsize=40)
plt.xticks(fontsize=30)
plt.yticks(fontsize=30)
plt.axhline(y=0, c='k')
# plt.axhline(y=2*homeValue/1e6, c='k')
# plt.axhline(y=3*homeValue/1e6, c='k')
plt.legend(loc='best',fontsize=24)
plt.title('Home value:$'+str(int(homeValue))+', Loan Value:\$'+str(int(loanAmount_Growth[0]))+', Interest Rate: ' + str(100*interestRate)+'%' + ', Annual Payment Increase: '+str(int((annual_increase-1)*100))+'%', fontsize=30)
plt.grid(True)
plt.show()

## Do something 
## Add monthly payment
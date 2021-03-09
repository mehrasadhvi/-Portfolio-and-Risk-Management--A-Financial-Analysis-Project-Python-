#Q2.Calculate standard deviation for all securities. Determine security with lowest standard deviation

import pandas as pd
import numpy as np
df1=pd.read_excel(r'C:\Users\DELL\Desktop\project k\Data for Assignment_2.xlsx', sheet_name='Worksheet',index_col='Date')
df=df1.loc['2014-04-01':'2019-04-01']
dailyreturns=df.diff()*(-1)
dailyreturns=dailyreturns/df
s=dailyreturns.std()
print("The Standard Deviation of all securities is \n",s,"\n")
print("The lowest standard deviation is of SBI FOCUSSED EQUITY FUND :0.007828")

#Q3.Calculate standard deviation of portfolio

dailyreturns1=dailyreturns*(0.090909)
df['portfolioreturns']=dailyreturns1.sum(axis=1)
j=df.loc[:,"portfolioreturns"].std()
print("The Standard deviation of portfolio is \n",j)

#Q4.Calculate beta and adjusted beta of all securities. Consider NIFTY50 as benchmark(market indicator)

Market1=pd.read_excel(r'C:\Users\DELL\Desktop\project k\Data for Assignment_2.xlsx', sheet_name='NIFTY50',index_col='Date')
Market=Market1.loc['2014-04-01':'2019-04-01']
Marketreturns=Market.diff()*(-1)
Marketreturns=Marketreturns/Market
Sd=Marketreturns.std()
Variance=Sd*Sd
MR=Marketreturns.iloc[:,0]
for i in range(0,11):
    Assetreturns=dailyreturns.iloc[:,i]
    Cov=Assetreturns.cov(MR)
    Beta=Cov/(Variance)
    ABeta=(0.33)+(0.67*Beta)
    print("Beta",(i+1),":", Beta,"/n")
    print("AdjustedBeta",(i+1),":",ABeta,"/n")
    

#Q5Calculate 5% daily VAR of this portfolio
#Using Analytical method
    
Meanreturn=df.loc[:,"portfolioreturns"].mean()
VAR=Meanreturn-(1.65*j)
print("\n The 5% Daily VAR of this portfolio is",VAR)

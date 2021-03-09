# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Q1
#Find Yearly Returns of all securites for years  2014-2018
import smtplib
import pandas as pd
import numpy as np
df = pd.read_excel (r'C:\Users\DELL\Desktop\projectkaiedeloscope\1592217538490_Data for Assignment.xlsx', sheet_name='Worksheet',index_col='Date')      
start=df.loc[pd.DatetimeIndex(['2019-04-01', '2018-04-02','2017-04-03','2016-04-01','2015-04-01','2014-04-01'])]
r=(start.diff()*(-1))/start
r.index.names = ['Returns']
r=r.dropna(how='all')
r= r.loc[:, ~r.columns.str.contains('^Unnamed')]
r.reset_index(drop=True, inplace=True) 
print("The annual returns for the year 2018-19,2017-18,2016-17,2015-16,2014-15 are \n",r)





#Q2
#Determine securities with highest and least correlation between them.
import pandas as pd
import numpy as np
df = pd.read_excel (r'C:\Users\DELL\Desktop\projectkaiedeloscope\1592217538490_Data for Assignment.xlsx', sheet_name='Worksheet')
data =df.loc[:, df.columns != 'Date']
df =df.loc[:, df.columns != 'Date']
data=data.diff()*(-1)
data=data/df
data = data.loc[:, ~data.columns.str.contains('^Unnamed')]
print("The Correlation between securities :\n")
print(data.corr())
#Weakest Correlation :MIRAE LARGE ASSET MIDCAP And U_T_I
#Highest correlation :MIRAE LARGE ASSET MIDCAP And SBI BLUECHIP FUND

#Q3
#Show graphical comparison of securities with the benchmark. Also comment upon your results obtained (Consider NIFTY50 as benchmark)

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df = pd.read_excel (r'C:\Users\DELL\Desktop\projectkaiedeloscope\1592217538490_Data for Assignment.xlsx', sheet_name='Worksheet',index_col='Date')      
start=df.loc[pd.DatetimeIndex(['2019-04-01', '2018-04-02','2017-04-03','2016-04-01','2015-04-01','2014-04-01'])]
r=(start.diff()*(-1))/start
r.index.names = ['Returns']
r=r.dropna(how='all')
x1=[2018,2017,2016,2015,2014]
df1 = pd.read_excel (r'C:\Users\DELL\Desktop\projectkaiedeloscope\1592217538490_Data for Assignment.xlsx', sheet_name='NIFTY50',index_col='Date')      
start1=df1.loc[pd.DatetimeIndex(['2019-04-01', '2018-04-02','2017-04-03','2016-04-01','2015-04-01','2014-04-01'])]
r1=(start1.diff()*(-1))/start1
r1=r1.dropna()
r1.index.names = ['Returns']
y1=r1['NIFTY50']
x2=[2018,2017,2016,2015,2014]
label=list(r)
for i in range(0,11):
    y=r.iloc[:,i]
    plt.plot(x2,y1,label='NIFTY50')
    plt.plot(x1,y,label=label[i])
    plt.xlabel('Years')
    plt.ylabel('Yearly Returns')
    plt.legend()
    plt.show()
    
#Q4
#Calculate Diversification Ratio for all securities. Comment upon the results obtained
import pandas as pd
import numpy as np
df = pd.read_excel (r'C:\Users\DELL\Desktop\projectkaiedeloscope\1592217538490_Data for Assignment.xlsx', sheet_name='Worksheet',index_col='Date')  
data=df.diff()*(-1)
data=data/df
data=data.dropna(how='all')
data = data.loc[:, ~data.columns.str.contains('^Unnamed')]
data.index.names = ['Returns']
r=data*(0.09090909)
data['Portfolio']=r.sum(axis=1)
k=data.std(axis = 0, skipna = True)
print("The diversification ratios are as follows:")
for i in range(0,11):
    k.iloc[i]=k.iloc[11]/k.iloc[i]
k=k.drop(k.index[11])
print(k)
print("The security with lowest diversification ratio gives the highest diversification benifit i.e.NIPPON INDIA LARGECAP FUND")

#Q5
#Consider a portfolio with securities - SBI Magnum, Kotak Standard , SBI Bluchip Fund with given quantities. Determine security which can be added to this portfolio to get more effective returns. (Take 2.91% as risk free rate of return)

import pandas as pd
import numpy as np
df=pd.read_excel(r'C:\Users\DELL\Desktop\projectkaiedeloscope\1592217538490_Data for Assignment.xlsx', sheet_name='Worksheet',index_col='Date')
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
z=df.loc[:,['SBI MAGNUM MIDCAP','KOTAK STANDARD MULTICAP FUND','SBI BLUECHIP FUND']]
dreturns=(z.diff()*(-1))/z
dreturns=dreturns.dropna()
y=(dreturns.iloc[:,0]*0.194061151)+(dreturns.iloc[:,1]*0.39993092)+(dreturns.iloc[:,2]*0.406007929)
print("The portfolio returns are \n",y)
k=y.std(axis=0,skipna=True)
k=k*15.5563491861
start=z.loc[pd.DatetimeIndex(['2015-04-01','2014-04-01'])]
yreturns=(start.diff()*(-1))/start
yreturns=yreturns.dropna()
l=(yreturns.iloc[:,0]*0.194061151)+(yreturns.iloc[:,1]*0.39993092)+(yreturns.iloc[:,2]*0.406007929)
s1=l.iloc[0]
s1=(s1-0.0291)/k
print("The SHARPE RATIO OF PORTFOLIO IS:")
print(s1)
k1=df.iloc[:,[0,3,4,5,7,8,9,10]]
dresec=(k1.diff()*(-1))/k1
rt1=k1.loc[pd.DatetimeIndex(['2015-04-01','2014-04-01'])]
yresec=(rt1.diff()*(-1))/rt1
s=yresec.iloc[1]
print("The annual returns of securities are: \n",s)
dailystd=dresec.std(axis=0,skipna=True)
annualstd=dailystd*15.5563491861
print("The annual Standart Deviation of Securities are:\n",annualstd)
SRS=(s-0.0291)/annualstd
print("The Sharpe Ratio of securities are:\n",SRS)
corr=dresec.corrwith(y,axis=0)
a=corr*4.136960935289707
print("Product of correlation and Sharp ratio of portfolio \n",a)
print("Any security whose sharpe ratio is greater than that product of sharpe ratio of portfolio correlation of security with portfolio must be added to the portfolioas U_T_I,LNT MIDC_A_P FUND,MIRAE LARGE ASSET MIDCAP,SBI FOCUSSED EQUITY FUND,INVESCO INDIA MULTICAP FUND,IDFC MULTICAP FUNDAmongst all these securities LNT MIDC_A_P FUND has highest sharpe ratio hence it must be added to theportfolio")

#Q6
#Make 3 portfolios consisting of 3 securities each randomly and compare each of these portfolios to analyse the best out of them

import pandas as pd
import numpy as np
df=pd.read_excel(r'C:\Users\DELL\Desktop\projectkaiedeloscope\1592217538490_Data for Assignment.xlsx', sheet_name='Worksheet',index_col='Date')
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
for i in range(1,4):
    z=df.sample(3, axis=1)
    print("PORTFOLIO\n", i)
    for col_name in z.columns: 
        print(col_name)
    dreturns=(z.diff()*(-1))/z
    dreturns=dreturns.dropna()
    y=(dreturns.iloc[:,0]*0.3333)+(dreturns.iloc[:,1]*0.33333)+(dreturns.iloc[:,2]*0.33333)
    k=y.std(axis=0,skipna=True)
    k=k*15.5563491861
    print("\nThe portfolio AnnualStandard Deviation is :",k)
    start=z.loc[pd.DatetimeIndex(['2015-04-01','2014-04-01'])]
    yreturns=(start.diff()*(-1))/start
    yreturns=yreturns.dropna()
    l=(yreturns.iloc[:,0]*0.33333)+(yreturns.iloc[:,1]*0.333333)+(yreturns.iloc[:,2]*0.333333)
    l.reset_index(drop=True, inplace=True) 
    print("\nThe portfolio Annual return is :",l)
    s1=l.iloc[0]
    s1=(s1-0.0291)/k
    print("The SHARP RATIO OF PORTFOLIO IS:")
    print(s1)
print("Since the sharp Ratio is maximum of Third portfolio ,hence it is the best.")
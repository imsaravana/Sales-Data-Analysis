# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 16:44:54 2018

@author: Saravana and Sudharsana
"""
import pandas as pd
import numpy as np
import matplotlib as plt
df = pd.read_csv("data-2.csv", parse_dates = ["InvoiceDate"])

#Calculating new columns Sales
df['Sales'] = round( (df.Quantity * df.UnitPrice),2)

#Total Revenue in Millions
Total_Revenue = round(np.sum(df.Sales)/1000000,2)
print("Total Revenue in Euro: " + str(Total_Revenue) + " Million")

#Total Revenue for each country
Country_Revenue = round((pd.pivot_table(df, index=['Country'],values=['Sales'],aggfunc=np.sum)),2)
Country_Revenue = Country_Revenue.reset_index()
Country_Revenue = Country_Revenue.sort_values(by=['Sales'],ascending=False)

#Removed UK for visualisation
temp = Country_Revenue[Country_Revenue.Country !="United Kingdom"]
temp.plot(kind="bar",x="Country", y= "Sales")

#Most Valuable customers
Cust= round((pd.pivot_table(df, index=['CustomerID','Country'],values=['Sales'],aggfunc=np.sum)),2)
Cust=Cust.reset_index()
Cust = Cust.sort_values(by=['Sales'],ascending= False)

#Dateframe with only returned items
r_df = df[df.Quantity < 0]
#Most returned items
r_df = r_df.groupby('StockCode',as_index=False)['Quantity'].count()
r_df = r_df.sort_values(by=['Quantity'], ascending= False)

#Most and least sold products by Quantity and Revenue
m_df = df.groupby(['StockCode','Description'],as_index=False)['Quantity','Sales'].sum()
m_df = m_df.sort_values(by=['Quantity'], ascending= False)

#Extract month and create a new column
df['month'] = pd.DatetimeIndex(df['InvoiceDate']).month

#Sales by month in millions
s_df = df.groupby('month',as_index=False)['Sales'].sum()
s_df['Sales'] = (s_df['Sales']/1000000)

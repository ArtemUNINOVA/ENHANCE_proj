#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#print('hello world')
#acquire data from excel
data_prod = pd.read_excel("dataset/POF2018_A.xlsx",header=0)

#leave only date without time
data_prod['Date'] = pd.to_datetime(data_prod["Date_1"]).dt.date
del data_prod['Date_1']

#values parameter defines the column to which the function is applied, in this case the number of products 
#beloning to certain categorie A, B or C is calculated, which is defined by the paremeter "column"
modelcols = data_prod.pivot_table(values='Serial_Number', index='Date', columns='Product_Type', aggfunc=len)

#calculating the amount of batteries used in accordance with date
ds_prod = data_prod.pivot_table(values='Serial_Number', index='Date', columns='Part_Type', aggfunc=len)
#the empty cells are filled with zeros
ds_prod = ds_prod.fillna(0)
ds_prod.reset_index(inplace=True)

ds_prod["day"] = pd.to_datetime(ds_prod["Date"]).dt.day_name()
ds_prod["Month"] = pd.to_datetime(ds_prod["Date"]).dt.month
ds_prod["Year"] = pd.to_datetime(ds_prod["Date"]).dt.year
ds_prod["Week"] = pd.to_datetime(ds_prod["Date"]).dt.isocalendar().week#dt.week

ds_prod = ds_prod.set_index("Date")
#add to the dataset Product columns with calculated amount of products
ds_prod['Product_C'] = modelcols['Product_C']
ds_prod['Product_B'] = modelcols['Product_B']
ds_prod['Product_A'] = modelcols['Product_A']

ds_prod = ds_prod.fillna(0)

#acquire data from the production dataset
data_stock = pd.read_excel("C:/Users/Artem/Desktop/Python/UNINOVA/enhance/forecasting_batteries/dataset/stock2018_A.xlsx",header=0)
data_stock = data_stock.iloc[1:]

#covert to datetime
data_stock['Datetime'] = pd.to_datetime(data_stock['Datetime'], format= "%d/%m/%Y %H-%M")#, utc = True)
#adjust date and time data with the production data set
data_stock = data_stock.loc[(data_stock['Datetime'] >= '2018-01-01 23:00:00') & (data_stock['Datetime'] <= '2018-12-21 23:00:00')]

#get the stock state at the end of the day at 23pm
filtered_stock_data = data_stock.loc[data_stock['Datetime'].dt.hour == 1]
filtered_stock_data["day"] = filtered_stock_data["Datetime"].dt.day_name()
filtered_stock_data["Month"] = filtered_stock_data["Datetime"].dt.month
filtered_stock_data["Year"] = filtered_stock_data["Datetime"].dt.year
filtered_stock_data["Week"] = filtered_stock_data["Datetime"].dt.isocalendar().week

#merge production and stock data, adjust based on date from prod data
ds_full = pd.merge(filtered_stock_data, ds_prod, how='left', left_on=['day','Week', 'Month', 'Year'], right_on = ['day','Week', 'Month', 'Year'])

ds_full['sum'] = ds_full['Type_A_y'] + ds_full['Type_B_y'] + ds_full['Type_C_y'] + ds_full['Type_D_y'] + ds_full['Type_E_y']
#remove columns with less than 10 batteries used, i.e. days when less than 10 batteries were used
ds_full = ds_full[ds_full['sum'] >= 10.0]

#rename columns
ds_full = ds_full.rename(columns = {'Type_A_x': 'Type_A_stock'})
ds_full = ds_full.rename(columns = {'Type_B_x': 'Type_B_stock'})
ds_full = ds_full.rename(columns = {'Type_C_x': 'Type_C_stock'})
ds_full = ds_full.rename(columns = {'Type_D_x': 'Type_D_stock'})
ds_full = ds_full.rename(columns = {'Type_E_x': 'Type_E_stock'})

ds_full = ds_full.rename(columns = {'Type_A_y': 'Type_A_used'})
ds_full = ds_full.rename(columns = {'Type_B_y': 'Type_B_used'})
ds_full = ds_full.rename(columns = {'Type_C_y': 'Type_C_used'})
ds_full = ds_full.rename(columns = {'Type_D_y': 'Type_D_used'})
ds_full = ds_full.rename(columns = {'Type_E_y': 'Type_E_used'})

#get new indexing starting from 1 till the the last row
ds_full.index = np.arange(1, len(ds_full)+1)

path_to_csv = 'C:/Users/Artem/Desktop/Python/UNINOVA/enhance/forecasting_batteries/python_files/'

ds_full.to_csv(path_to_csv+'updated_df', sep='\t')
print('successfully created')




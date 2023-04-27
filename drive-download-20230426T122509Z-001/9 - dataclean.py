#Load libraries
import pandas as pd
import numpy as np

fds0 = pd.read_csv("9 - FashionDataset.csv")
print(fds0.head())
print()
print(fds0.isnull().sum())

#A)Imputing Missing Values
#Mean Method
fds1 = pd.read_csv("9 - FashionDataset.csv")
fds1.head()

fds1.isnull().sum()

missing_col = ['SellPrice']
#Using mean to impute the missing values
for i in missing_col:
    fds1.loc[fds1.loc[:,i].isnull(),i]=fds1.loc[:,i].mean()

print(fds1.isnull().sum())
print()
#Median Method
fds2 = pd.read_csv("9 - FashionDataset.csv")
fds2.head()

fds2.isnull().sum()

missing_col_1 = ['SellPrice']
#Using mean to impute the missing values
for i in missing_col_1:
    fds2.loc[fds2.loc[:,i].isnull(),i]=fds2.loc[:,i].median()

print(fds2.isnull().sum())

#Filling with a new category
fds2['BrandName'] = fds2['BrandName'].fillna('No Brand')
fds2['Deatils'] = fds2['Deatils'].fillna('No Details')
fds2['Sizes'] = fds2['Sizes'].fillna('No Size')
fds2['MRP'] = fds2['MRP'].fillna('No MRP')
fds2['Discount'] = fds2['Discount'].fillna('No Discount')

print(fds2.isnull().sum())

#B)Removing Rows
#Duplicate Values
print()
print(len(fds1))
print()
fds1= fds1.drop_duplicates()
print(len(fds1))
print()

#Missing Values
len(fds1)

fds1 = fds1.dropna()
print(len(fds1))
print()

#Unnecessary Column
fds1.head()

fds1 = fds1.drop(columns=["Unnamed: 0"])
print(fds1.head())

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

mtcars = pd.read_csv("7 - mtcars.csv")
print(mtcars)

del mtcars['Unnamed: 0']

print(mtcars.head())
print()

print(mtcars.mean())
print()
print(mtcars.median())
print()
print(mtcars.mode())
print()
print(max(mtcars["mpg"]) - min(mtcars["mpg"])) #Range of mpg
print()
five_num = [mtcars["mpg"].quantile(0),   
            mtcars["mpg"].quantile(0.25),
            mtcars["mpg"].quantile(0.50),
            mtcars["mpg"].quantile(0.75),
            mtcars["mpg"].quantile(1)]
print(five_num)
print()
print(mtcars["mpg"].describe())
print()
print(mtcars["mpg"].quantile(0.75) - mtcars["mpg"].quantile(0.25)) #Interquartile (IQR) range
print()
print(mtcars["mpg"].var()) #variance
print()
print(mtcars["mpg"].std()) #standard deviation
print()

#skewness and kurtosis
print(mtcars.skew())
print()
print(mtcars.kurt())
print()

from numpy import absolute
A = 20
sum = 0  # Initialize sum to 0
# Absolute deviation calculation
for i in range(len(mtcars)):
    av = absolute(mtcars["mpg"][i] - A)
    # Absolute value of the differences of each data point and A
    # Summing all those absolute values
    sum = sum + av               

# finding the absolute deviation
print(sum / len(mtcars))   

from scipy.stats import skew,kurtosis

def calculate_skewness(x):
    sk = skew(x)
    return sk

def calculate_kurtosis(x):
    kurt = kurtosis(x)
    return kurt

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Plot between -10 and 10 with .001 steps.
x = np.array([1,2,3,4,5,6,7,8,9,10])

# Calculate mean and standard deviation
mean = np.mean(x)
sd = np.std(x)

plt.plot(x,norm.pdf(x, mean, sd))
plt.show()

sk = calculate_skewness(x)
kurt = calculate_kurtosis(x)

print("Skewness: ", sk)
print("Kurtosis: ",kurt)

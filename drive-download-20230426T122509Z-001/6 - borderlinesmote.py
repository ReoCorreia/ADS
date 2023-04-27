# import necessary libraries
import pandas as pd
from imblearn.over_sampling import BorderlineSMOTE

# read in the data
data = pd.read_csv('6 - borderlinesmote.csv')

# split the data into features and target
X = data.drop('target', axis=1)
y = data['target']

# initialize the Borderline-SMOTE algorithm
sm = BorderlineSMOTE()

# generate synthetic data using Borderline-SMOTE
X_resampled, y_resampled = sm.fit_resample(X, y)

# print the number of samples in each class before and after resampling
print("Before resampling:\n", y.value_counts())
print("\nAfter resampling:\n", y_resampled.value_counts())

import matplotlib.pyplot as plt

# define a list of colors for each point based on a categorical variable
colors = ['blue' if y_resampled[i] == 0 else 'orange' for i in range(len(y_resampled))]

# define x and y coordinates of the points
# plot the points
plt.scatter(X_resampled['feature1'],X_resampled['feature3'],c=colors)

# add axis labels and a title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter plot of points')

# show the plot
plt.show()

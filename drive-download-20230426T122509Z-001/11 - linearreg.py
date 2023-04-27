import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import pandas as pd

df = pd.read_csv('11 - tips.csv')

print(df)
# Create sample data
#X = np.array([[1], [2], [3], [4], [5]])
#y = np.array([3, 5, 7, 9, 11])

X = df[['total_bill','size']]
y = df['tip']

# Create linear regression object
reg = LinearRegression()

# Train the model using the training sets
reg.fit(X, y)

# Make predictions using the testing set
y_pred = reg.predict(X)

# Print model coefficients
print('Coefficients: ', reg.coef_)

# Calculate RMSE
rmse = np.sqrt(mean_squared_error(y, y_pred))

# Calculate MSE
mse = mean_squared_error(y, y_pred)

# Calculate MAE
mae = mean_absolute_error(y, y_pred)

# Calculate MAPE
mape = np.mean(np.abs((y - y_pred) / y)) * 100

# Print the results
print('RMSE:', rmse)
print('MSE:', mse)
print('MAE:', mae)
print('MAPE:', mape)

# Print coefficient of determination (R^2)
print('Coefficient of determination (R^2): ',r2_score(y, y_pred))

# Plot outputs
plt.scatter(y, y_pred)
plt.xlabel('Y Actual')
plt.ylabel('Y Predict')

plt.show()

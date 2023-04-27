import numpy as np

def karl_correlation(x,y):
    #calculate means and standard deviation
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    x_std = np.std(x)
    y_std = np.std(y)

    #calculate covariance
    covariance = np.sum((x-x_mean)*(y-y_mean))/len(x)

    #calculate karl-pearson correlation coefficent
    r = covariance / (x_std * y_std)

    return r

x = np.array([1,2,3,4,5])
y = np.array([2,4,6,8,10])

r = karl_correlation(x,y)

print("Karl Pearson correlation coefficent :",r)

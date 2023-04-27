import numpy as np

def pearson_skewness(data):
    mean = np.mean(data)
    median = np.median(data)
    std_dev = np.std(data)
    skewness = 3 * (mean-median)/std_dev
    return skewness

x = np.array([1,2,3,4,5,6,7,8,9,10])
sk = pearson_skewness(x)
print("Pearson's coefficient of skewness: ",sk)

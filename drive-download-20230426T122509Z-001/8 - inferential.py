import numpy as np
import pandas as pd
import scipy.stats as stats
from statsmodels.stats.weightstats import ztest

crops = pd.read_csv("8 - Crop_recommendation.csv")
del crops["label"]
print(crops.head())
print()

print(ztest(crops["N"],crops["P"],value=0))
print()
print(stats.ttest_1samp(crops["N"], popmean=10))
print()

def f_test(group1, group2):
    f = np.var(group1)/np.var(group2)
    nun = group1.size-1
    dun = group2.size-1
    p_value = 1-stats.f.cdf(f, nun, dun)
    return f, p_value

# perform F-test
x = crops["temperature"][:1100]
y = crops["temperature"][1100:]
print(f_test(x, y))

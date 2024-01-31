import pandas as pd
import numpy as np
import scipy.stats as st

df = pd.read_csv('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/wikipedia/Kolmogorov-Smirnov_test/Kolmogorov-Smirnov_test_data.csv')
df.replace(['#N/A', '#VALUE!'], pd.NA, inplace=True)


x = df['Time Complexity Class']
x.dropna(inplace=True)



y = df[['Wikipedia Problem','Time Complexity Class']]
y.dropna(inplace=True)
y = y['Time Complexity Class']




# y = 

# statistic, p_value = st.kstest(y,x)
# print(D)
# print(p)

# if p_value < 0.05:
#     print("The two samples are likely drawn from different distributions.")
# else:
#     print("The two samples are likely drawn from the same distribution.")
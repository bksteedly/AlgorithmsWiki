import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/wikipedia/Sheet1_categorizations.csv')
df = df[['Has dedicated page?', 'Part of another page?', 'One of them', 'Time Complexity Class', 'Space Complexity Class']]

# Filtering rows where 'Has dedicated page' is equal to 1
filtered_df1 = df[df['Has dedicated page?'] == 1]
filtered_df2 = df[df['Part of another page?'] == 1]
filtered_df3 = df[df['One of them'] == 0]


# Calculating the average value of 'Time Complexity Class'
# average_time_complexity1 = filtered_df1['Time Complexity Class'].mean()
# average_time_complexity2 = filtered_df2['Time Complexity Class'].mean()
# average_time_complexity3 = filtered_df3['Time Complexity Class'].mean()

# print("Average Time Complexity Class dedicated page:", average_time_complexity1)
# print("Average Time Complexity Class part of page:", average_time_complexity2)
# print("Average Time Complexity Class not on wikipedia:", average_time_complexity3)

average_space_complexity1 = filtered_df1['Space Complexity Class'].mean()
average_space_complexity2 = filtered_df2['Space Complexity Class'].mean()
average_space_complexity3 = filtered_df3['Space Complexity Class'].mean()

print("Average Space Complexity Class dedicated page:", average_space_complexity1)
print("Average Space Complexity Class part of page:", average_space_complexity2)
print("Average Space Complexity Class not on wikipedia:", average_space_complexity3)




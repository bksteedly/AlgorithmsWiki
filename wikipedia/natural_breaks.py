import jenkspy
from pandas import read_csv

sheet = read_csv("/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/wikipedia/histogram_data.csv")
data = sheet['2023'].tolist()
print(data)

# Calculate the Jenks Natural Breaks
print(jenkspy.jenks_breaks(data, n_classes=2))
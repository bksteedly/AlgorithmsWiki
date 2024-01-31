import csv
import pandas as pd
import jenkspy
from pandas import read_csv
from matplotlib import pyplot as plt
import numpy as np

data = read_csv("/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/wikipedia/histogram_data.csv")

for year in ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', 'Overall']:
    print(f'starting figure {year}')
    views = np.log(data[year].tolist())
    print(views)
    breaks = jenkspy.jenks_breaks(views, n_classes=4)
    print(breaks)
    
    fig, ax = plt.subplots(figsize =(10, 7)) #set figure size
    ax.hist(views, bins = 100) #create a histogram of views with 100 bins
    ax.set_xlim([0, max(views)]) #graph goes from low to high

    ax.set_xlabel('Number of Views') #set the x axis label
    ax.set_ylabel('Number of Articles') #set the y axis label
    ax.set_title(f'Views for Wikipedia pages on algorithms ({year})') #set the title
    plt.axvline(x=breaks[0], color='red', linestyle='--')
    plt.axvline(x=breaks[1], color='red', linestyle='--')
    plt.axvline(x=breaks[2], color='red', linestyle='--')
    plt.axvline(x=breaks[3], color='red', linestyle='--')
    plt.axvline(x=breaks[4], color='red', linestyle='--')
    plt.savefig(f'/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/wikipedia/{year}.jpg') #save plot
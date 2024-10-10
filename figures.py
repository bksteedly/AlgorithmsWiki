from cmath import inf
import math
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from scipy.stats import powerlaw
import matplotlib.ticker as mticker
import warnings
warnings.filterwarnings("ignore")

def figure1():
    #merge the reads csv file with the original
    df = pd.read_csv('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/Wellesley/AlgorithmsWiki/wikipedia/sheet1_output_views.csv')
    df = df.fillna('')

    dict = df.to_dict(orient='records')

    min_time_complexities = {}

    # Iterate through the list of dictionaries and find min time complexity class for each family
    for entry in dict:
        family_name = entry['Family Name']
        time_complexity_class = entry['Time Complexity Class']
        
        if family_name not in min_time_complexities:
            min_time_complexities[family_name] = time_complexity_class
        else:
            min_time_complexities[family_name] = min(min_time_complexities[family_name], time_complexity_class)

    # Iterate through the list of dictionaries and add the min_time_complexity_class to each entry
    for entry in dict:
        family_name = entry['Family Name']
        entry['min_time_complexity_class'] = min_time_complexities[family_name]
        if entry['min_time_complexity_class'] == entry['Time Complexity Class']:
            entry['is_optimal'] = True
        else:
            entry['is_optimal'] = False

    df = pd.df(dict)
    df.to_csv('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/Wellesley/AlgorithmsWiki/wikipedia/merged.csv', index=False)
    
    df = pd.read_csv('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/Wellesley/AlgorithmsWiki/wikipedia/merged.csv')
    df = df.fillna('')
    dict = df.to_dict(orient='records')

    reads_all = []
    reads_optimal = []
    reads_not_optimal = []
    total_optimal = 0
    wiki_optimal = 0
    total_algos = 0
    for algo in dict:
        total_algos += 1
        if algo['2015070100'] != '':
            reads_all.append(float(algo['2015070100'] + algo['2015080100'] + algo['2015090100'] + algo['2015100100'] + algo['2015110100'] + algo['2015120100'] + algo['2016010100'] + algo['2016020100'] + algo['2016030100'] + algo['2016040100'] + algo['2016050100'] + algo['2016060100'] + algo['2016070100'] + algo['2016080100'] + algo['2016090100'] + algo['2016100100'] + algo['2016110100'] + algo['2016120100'] + algo['2017010100'] + algo['2017020100'] + algo['2017030100'] + algo['2017040100'] + algo['2017050100'] + algo['2017060100'] + algo['2017070100'] + algo['2017080100'] + algo['2017090100'] + algo['2017100100'] + algo['2017110100'] + algo['2017120100'] + algo['2018010100'] + algo['2018020100'] + algo['2018030100'] + algo['2018040100'] + algo['2018050100'] + algo['2018060100'] + algo['2018070100'] + algo['2018080100'] + algo['2018090100'] + algo['2018100100'] + algo['2018110100'] + algo['2018120100'] + algo['2019010100'] + algo['2019020100'] + algo['2019030100'] + algo['2019040100'] + algo['2019050100'] + algo['2019060100'] + algo['2019070100'] + algo['2019080100'] + algo['2019090100'] + algo['2019100100'] + algo['2019110100'] + algo['2019120100'] + algo['2020010100'] + algo['2020020100'] + algo['2020030100'] + algo['2020040100'] + algo['2020050100'] + algo['2020060100'] + algo['2020070100'] + algo['2020080100'] + algo['2020090100'] + algo['2020100100'] + algo['2020110100'] + algo['2020120100'] + algo['2021010100'] + algo['2021020100'] + algo['2021030100'] + algo['2021040100'] + algo['2021050100'] + algo['2021060100'] + algo['2021070100'] + algo['2021080100'] + algo['2021090100'] + algo['2021100100'] + algo['2021110100'] + algo['2021120100'] + algo['2022010100'] + algo['2022020100'] + algo['2022030100'] + algo['2022040100'] + algo['2022050100'] + algo['2022060100'] + algo['2022070100'] + algo['2022080100'] + algo['2022090100'] + algo['2022100100'] + algo['2022110100'] + algo['2022120100'] + algo['2023010100'] + algo['2023020100'] + algo['2023030100'] + algo['2023040100'] + algo['2023050100'] + algo['2023060100'] + algo['2023070100'])/97)
            if algo['is_optimal'] == True:
                wiki_optimal += 1
                reads_optimal.append(float(algo['2015070100'] + algo['2015080100'] + algo['2015090100'] + algo['2015100100'] + algo['2015110100'] + algo['2015120100'] + algo['2016010100'] + algo['2016020100'] + algo['2016030100'] + algo['2016040100'] + algo['2016050100'] + algo['2016060100'] + algo['2016070100'] + algo['2016080100'] + algo['2016090100'] + algo['2016100100'] + algo['2016110100'] + algo['2016120100'] + algo['2017010100'] + algo['2017020100'] + algo['2017030100'] + algo['2017040100'] + algo['2017050100'] + algo['2017060100'] + algo['2017070100'] + algo['2017080100'] + algo['2017090100'] + algo['2017100100'] + algo['2017110100'] + algo['2017120100'] + algo['2018010100'] + algo['2018020100'] + algo['2018030100'] + algo['2018040100'] + algo['2018050100'] + algo['2018060100'] + algo['2018070100'] + algo['2018080100'] + algo['2018090100'] + algo['2018100100'] + algo['2018110100'] + algo['2018120100'] + algo['2019010100'] + algo['2019020100'] + algo['2019030100'] + algo['2019040100'] + algo['2019050100'] + algo['2019060100'] + algo['2019070100'] + algo['2019080100'] + algo['2019090100'] + algo['2019100100'] + algo['2019110100'] + algo['2019120100'] + algo['2020010100'] + algo['2020020100'] + algo['2020030100'] + algo['2020040100'] + algo['2020050100'] + algo['2020060100'] + algo['2020070100'] + algo['2020080100'] + algo['2020090100'] + algo['2020100100'] + algo['2020110100'] + algo['2020120100'] + algo['2021010100'] + algo['2021020100'] + algo['2021030100'] + algo['2021040100'] + algo['2021050100'] + algo['2021060100'] + algo['2021070100'] + algo['2021080100'] + algo['2021090100'] + algo['2021100100'] + algo['2021110100'] + algo['2021120100'] + algo['2022010100'] + algo['2022020100'] + algo['2022030100'] + algo['2022040100'] + algo['2022050100'] + algo['2022060100'] + algo['2022070100'] + algo['2022080100'] + algo['2022090100'] + algo['2022100100'] + algo['2022110100'] + algo['2022120100'] + algo['2023010100'] + algo['2023020100'] + algo['2023030100'] + algo['2023040100'] + algo['2023050100'] + algo['2023060100'] + algo['2023070100'])/97)
            elif algo['is_optimal'] == False:
                reads_not_optimal.append(float(algo['2015070100'] + algo['2015080100'] + algo['2015090100'] + algo['2015100100'] + algo['2015110100'] + algo['2015120100'] + algo['2016010100'] + algo['2016020100'] + algo['2016030100'] + algo['2016040100'] + algo['2016050100'] + algo['2016060100'] + algo['2016070100'] + algo['2016080100'] + algo['2016090100'] + algo['2016100100'] + algo['2016110100'] + algo['2016120100'] + algo['2017010100'] + algo['2017020100'] + algo['2017030100'] + algo['2017040100'] + algo['2017050100'] + algo['2017060100'] + algo['2017070100'] + algo['2017080100'] + algo['2017090100'] + algo['2017100100'] + algo['2017110100'] + algo['2017120100'] + algo['2018010100'] + algo['2018020100'] + algo['2018030100'] + algo['2018040100'] + algo['2018050100'] + algo['2018060100'] + algo['2018070100'] + algo['2018080100'] + algo['2018090100'] + algo['2018100100'] + algo['2018110100'] + algo['2018120100'] + algo['2019010100'] + algo['2019020100'] + algo['2019030100'] + algo['2019040100'] + algo['2019050100'] + algo['2019060100'] + algo['2019070100'] + algo['2019080100'] + algo['2019090100'] + algo['2019100100'] + algo['2019110100'] + algo['2019120100'] + algo['2020010100'] + algo['2020020100'] + algo['2020030100'] + algo['2020040100'] + algo['2020050100'] + algo['2020060100'] + algo['2020070100'] + algo['2020080100'] + algo['2020090100'] + algo['2020100100'] + algo['2020110100'] + algo['2020120100'] + algo['2021010100'] + algo['2021020100'] + algo['2021030100'] + algo['2021040100'] + algo['2021050100'] + algo['2021060100'] + algo['2021070100'] + algo['2021080100'] + algo['2021090100'] + algo['2021100100'] + algo['2021110100'] + algo['2021120100'] + algo['2022010100'] + algo['2022020100'] + algo['2022030100'] + algo['2022040100'] + algo['2022050100'] + algo['2022060100'] + algo['2022070100'] + algo['2022080100'] + algo['2022090100'] + algo['2022100100'] + algo['2022110100'] + algo['2022120100'] + algo['2023010100'] + algo['2023020100'] + algo['2023030100'] + algo['2023040100'] + algo['2023050100'] + algo['2023060100'] + algo['2023070100'])/97)
        if algo['is_optimal'] == True:
                total_optimal += 1

    # get max reads value
    max_reads = math.ceil(max(max(reads_optimal), max(reads_not_optimal)) / 5000) * 5000
    num_bins = int(max_reads/5000)
    bins = []
    for i in range(num_bins):
        bins.append((i*5)+5)

    optimal_counts = []
    non_optimal_counts = []
    for i in range(num_bins):
        optimal_counts.append(0)
        non_optimal_counts.append(0)
    print(reads_optimal)
    for reads in reads_optimal:
        if reads < (bins[0]*1000):
            optimal_counts[0]+=1
        elif reads >= (bins[0]*1000) and (reads < (bins[1]*1000)):
            optimal_counts[1]+=1
        elif reads >= (bins[1]*1000) and (reads < (bins[2]*1000)):
            optimal_counts[2]+=1
        elif reads >= (bins[2]*1000) and (reads < (bins[3]*1000)):
            optimal_counts[3]+=1
        elif reads >= (bins[3]*1000) and (reads < (bins[4]*1000)):
            optimal_counts[4]+=1
        elif reads >= (bins[4]*1000) and (reads < (bins[5]*1000)):
            optimal_counts[5]+=1
        elif reads >= (bins[5]*1000) and (reads < (bins[6]*1000)):
            optimal_counts[6]+=1
        elif reads >= (bins[6]*1000) and (reads < (bins[7]*1000)):
            optimal_counts[7]+=1
        elif reads >= (bins[7]*1000) and (reads < (bins[8]*1000)):
            optimal_counts[8]+=1
        elif reads >= (bins[8]*1000) and (reads < (bins[9]*1000)):
            optimal_counts[9]+=1
        elif reads >= (bins[9]*1000) and (reads < (bins[10]*1000)):
            optimal_counts[10]+=1
        elif reads >= (bins[10]*1000) and (reads < (bins[11]*1000)):
            optimal_counts[11]+=1
        elif reads >= (bins[11]*1000) and (reads < (bins[12]*1000)):
            optimal_counts[12]+=1
        elif reads >= (bins[12]*1000) and (reads < (bins[13]*1000)):
            optimal_counts[13]+=1


    for reads in reads_not_optimal:
        if reads < (bins[0]*1000):
            non_optimal_counts[0]+=1
        elif reads >= (bins[0]*1000) and (reads < (bins[1]*1000)):
            non_optimal_counts[1]+=1
        elif reads >= (bins[1]*1000) and (reads < (bins[2]*1000)):
            non_optimal_counts[2]+=1
        elif reads >= (bins[2]*1000) and (reads < (bins[3]*1000)):
            non_optimal_counts[3]+=1
        elif reads >= (bins[3]*1000) and (reads < (bins[4]*1000)):
            non_optimal_counts[4]+=1
        elif reads >= (bins[4]*1000) and (reads < (bins[5]*1000)):
            non_optimal_counts[5]+=1
        elif reads >= (bins[5]*1000) and (reads < (bins[6]*1000)):
            non_optimal_counts[6]+=1
        elif reads >= (bins[6]*1000) and (reads < (bins[7]*1000)):
            non_optimal_counts[7]+=1
        elif reads >= (bins[7]*1000) and (reads < (bins[8]*1000)):
            non_optimal_counts[8]+=1
        elif reads >= (bins[8]*1000) and (reads < (bins[9]*1000)):
            non_optimal_counts[9]+=1
        elif reads >= (bins[9]*1000) and (reads < (bins[10]*1000)):
            non_optimal_counts[10]+=1
        elif reads >= (bins[10]*1000) and (reads < (bins[11]*1000)):
            non_optimal_counts[11]+=1
        elif reads >= (bins[11]*1000) and (reads < (bins[12]*1000)):
            non_optimal_counts[12]+=1
        elif reads >= (bins[12]*1000) and (reads < (bins[13]*1000)):
            non_optimal_counts[13]+=1

    optimal_percent = []
    non_optimal_percent = []
    for i in range(num_bins):
        optimal_percent.append(optimal_counts[i]/len(reads_optimal)*100)
        non_optimal_percent.append(non_optimal_counts[i]/len(reads_not_optimal)*100)

    x = np.array(bins)
    y1 = np.array(optimal_percent)
    y2 = np.array(non_optimal_percent)



    # Fit power law curve
    def power_law(x, a, b):
        return a * np.power(x, b)

    popt1, _ = curve_fit(power_law, x, optimal_percent)
    popt2, _ = curve_fit(power_law, x, non_optimal_percent)


    # Plot the data points
    fig, ax = plt.subplots(figsize=(6.4, 4.8))

    x_smooth_fit = np.linspace(min(x), max(x), 100)
    ax.plot(x_smooth_fit, power_law(x_smooth_fit, *popt1), '-', label='Power Law Fit (Optimal)', color="royalblue")
    ax.plot(x_smooth_fit, power_law(x_smooth_fit, *popt2), '-', label='Power Law Fit (Non-Optimal)', color="orange")

    ax.scatter(x, y1, color='royalblue', label='Optimal Algos')
    ax.scatter(x, y2, color='orange', label='Non-Optimal Algos')

    ax.set_title('Wikipedia Binned Page Views of Optimal vs Non-Optimal Algos', fontsize=14)
    ax.set_xlabel('Monthly Page Views (in thousands)', fontsize=14)
    ax.set_ylabel('Percentage of Algorithms', fontsize=14)
    ax.legend()

    xticklabels = [f"{i-5}-{i}" for i in bins]
    # print(xticklabels)
    ax.set_xticks(bins)
    ax.set_xticklabels(xticklabels, rotation=-45, horizontalalignment='left')
    # for i, label in enumerate(ax.xaxis.get_ticklabels()):
    #     if i % 2 == 0:
    #         ax.xaxis.get_major_ticks()[i].set_visible(False)

    ax.set_yscale('log')  # Set y-axis to log scale
    ax = plt.gca()
    ax.yaxis.set_major_formatter(mticker.ScalarFormatter())
    ax.yaxis.get_major_formatter().set_scientific(False)

    # Set the y-axis ticks to integers instead of decimals
    def integer_formatter(x, pos):
        return f'{int(x)}'
    
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(integer_formatter))
    plt.yticks([1, 10, 50]) 

    plt.tight_layout()
    plt.savefig('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/Wellesley/AlgorithmsWiki/Paper/fig1.pdf')
    plt.savefig('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/Wellesley/AlgorithmsWiki/Paper/fig1.png')
    plt.show()

# def figure1():
#     #merge the reads csv file with the original
#     df = pd.read_csv('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/wikipedia/sheet1_output_views.csv')
#     df = df.fillna('')

#     dict = df.to_dict(orient='records')

#     min_time_complexities = {}

#     # Iterate through the list of dictionaries and find min time complexity class for each family
#     for entry in dict:
#         family_name = entry['Family Name']
#         time_complexity_class = entry['Time Complexity Class']
        
#         if family_name not in min_time_complexities:
#             min_time_complexities[family_name] = time_complexity_class
#         else:
#             min_time_complexities[family_name] = min(min_time_complexities[family_name], time_complexity_class)

#     # Iterate through the list of dictionaries and add the min_time_complexity_class to each entry
#     for entry in dict:
#         family_name = entry['Family Name']
#         entry['min_time_complexity_class'] = min_time_complexities[family_name]
#         if entry['min_time_complexity_class'] == entry['Time Complexity Class']:
#             entry['is_optimal'] = True
#         else:
#             entry['is_optimal'] = False

#     df = pd.df(dict)
#     df.to_csv('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/wikipedia/merged.csv', index=False)

#     reads_all = []
#     reads_optimal = []
#     reads_not_optimal = []
#     total_optimal = 0
#     wiki_optimal = 0
#     total_algos = 0
#     for algo in dict:
#         total_algos += 1
#         if algo['2015070100'] != '':
#             reads_all.append(float(algo['2015070100'] + algo['2015080100'] + algo['2015090100'] + algo['2015100100'] + algo['2015110100'] + algo['2015120100'] + algo['2016010100'] + algo['2016020100'] + algo['2016030100'] + algo['2016040100'] + algo['2016050100'] + algo['2016060100'] + algo['2016070100'] + algo['2016080100'] + algo['2016090100'] + algo['2016100100'] + algo['2016110100'] + algo['2016120100'] + algo['2017010100'] + algo['2017020100'] + algo['2017030100'] + algo['2017040100'] + algo['2017050100'] + algo['2017060100'] + algo['2017070100'] + algo['2017080100'] + algo['2017090100'] + algo['2017100100'] + algo['2017110100'] + algo['2017120100'] + algo['2018010100'] + algo['2018020100'] + algo['2018030100'] + algo['2018040100'] + algo['2018050100'] + algo['2018060100'] + algo['2018070100'] + algo['2018080100'] + algo['2018090100'] + algo['2018100100'] + algo['2018110100'] + algo['2018120100'] + algo['2019010100'] + algo['2019020100'] + algo['2019030100'] + algo['2019040100'] + algo['2019050100'] + algo['2019060100'] + algo['2019070100'] + algo['2019080100'] + algo['2019090100'] + algo['2019100100'] + algo['2019110100'] + algo['2019120100'] + algo['2020010100'] + algo['2020020100'] + algo['2020030100'] + algo['2020040100'] + algo['2020050100'] + algo['2020060100'] + algo['2020070100'] + algo['2020080100'] + algo['2020090100'] + algo['2020100100'] + algo['2020110100'] + algo['2020120100'] + algo['2021010100'] + algo['2021020100'] + algo['2021030100'] + algo['2021040100'] + algo['2021050100'] + algo['2021060100'] + algo['2021070100'] + algo['2021080100'] + algo['2021090100'] + algo['2021100100'] + algo['2021110100'] + algo['2021120100'] + algo['2022010100'] + algo['2022020100'] + algo['2022030100'] + algo['2022040100'] + algo['2022050100'] + algo['2022060100'] + algo['2022070100'] + algo['2022080100'] + algo['2022090100'] + algo['2022100100'] + algo['2022110100'] + algo['2022120100'] + algo['2023010100'] + algo['2023020100'] + algo['2023030100'] + algo['2023040100'] + algo['2023050100'] + algo['2023060100'] + algo['2023070100'])/97)
#             if algo['is_optimal'] == True:
#                 wiki_optimal += 1
#                 reads_optimal.append(float(algo['2015070100'] + algo['2015080100'] + algo['2015090100'] + algo['2015100100'] + algo['2015110100'] + algo['2015120100'] + algo['2016010100'] + algo['2016020100'] + algo['2016030100'] + algo['2016040100'] + algo['2016050100'] + algo['2016060100'] + algo['2016070100'] + algo['2016080100'] + algo['2016090100'] + algo['2016100100'] + algo['2016110100'] + algo['2016120100'] + algo['2017010100'] + algo['2017020100'] + algo['2017030100'] + algo['2017040100'] + algo['2017050100'] + algo['2017060100'] + algo['2017070100'] + algo['2017080100'] + algo['2017090100'] + algo['2017100100'] + algo['2017110100'] + algo['2017120100'] + algo['2018010100'] + algo['2018020100'] + algo['2018030100'] + algo['2018040100'] + algo['2018050100'] + algo['2018060100'] + algo['2018070100'] + algo['2018080100'] + algo['2018090100'] + algo['2018100100'] + algo['2018110100'] + algo['2018120100'] + algo['2019010100'] + algo['2019020100'] + algo['2019030100'] + algo['2019040100'] + algo['2019050100'] + algo['2019060100'] + algo['2019070100'] + algo['2019080100'] + algo['2019090100'] + algo['2019100100'] + algo['2019110100'] + algo['2019120100'] + algo['2020010100'] + algo['2020020100'] + algo['2020030100'] + algo['2020040100'] + algo['2020050100'] + algo['2020060100'] + algo['2020070100'] + algo['2020080100'] + algo['2020090100'] + algo['2020100100'] + algo['2020110100'] + algo['2020120100'] + algo['2021010100'] + algo['2021020100'] + algo['2021030100'] + algo['2021040100'] + algo['2021050100'] + algo['2021060100'] + algo['2021070100'] + algo['2021080100'] + algo['2021090100'] + algo['2021100100'] + algo['2021110100'] + algo['2021120100'] + algo['2022010100'] + algo['2022020100'] + algo['2022030100'] + algo['2022040100'] + algo['2022050100'] + algo['2022060100'] + algo['2022070100'] + algo['2022080100'] + algo['2022090100'] + algo['2022100100'] + algo['2022110100'] + algo['2022120100'] + algo['2023010100'] + algo['2023020100'] + algo['2023030100'] + algo['2023040100'] + algo['2023050100'] + algo['2023060100'] + algo['2023070100'])/97)
#             elif algo['is_optimal'] == False:
#                 reads_not_optimal.append(float(algo['2015070100'] + algo['2015080100'] + algo['2015090100'] + algo['2015100100'] + algo['2015110100'] + algo['2015120100'] + algo['2016010100'] + algo['2016020100'] + algo['2016030100'] + algo['2016040100'] + algo['2016050100'] + algo['2016060100'] + algo['2016070100'] + algo['2016080100'] + algo['2016090100'] + algo['2016100100'] + algo['2016110100'] + algo['2016120100'] + algo['2017010100'] + algo['2017020100'] + algo['2017030100'] + algo['2017040100'] + algo['2017050100'] + algo['2017060100'] + algo['2017070100'] + algo['2017080100'] + algo['2017090100'] + algo['2017100100'] + algo['2017110100'] + algo['2017120100'] + algo['2018010100'] + algo['2018020100'] + algo['2018030100'] + algo['2018040100'] + algo['2018050100'] + algo['2018060100'] + algo['2018070100'] + algo['2018080100'] + algo['2018090100'] + algo['2018100100'] + algo['2018110100'] + algo['2018120100'] + algo['2019010100'] + algo['2019020100'] + algo['2019030100'] + algo['2019040100'] + algo['2019050100'] + algo['2019060100'] + algo['2019070100'] + algo['2019080100'] + algo['2019090100'] + algo['2019100100'] + algo['2019110100'] + algo['2019120100'] + algo['2020010100'] + algo['2020020100'] + algo['2020030100'] + algo['2020040100'] + algo['2020050100'] + algo['2020060100'] + algo['2020070100'] + algo['2020080100'] + algo['2020090100'] + algo['2020100100'] + algo['2020110100'] + algo['2020120100'] + algo['2021010100'] + algo['2021020100'] + algo['2021030100'] + algo['2021040100'] + algo['2021050100'] + algo['2021060100'] + algo['2021070100'] + algo['2021080100'] + algo['2021090100'] + algo['2021100100'] + algo['2021110100'] + algo['2021120100'] + algo['2022010100'] + algo['2022020100'] + algo['2022030100'] + algo['2022040100'] + algo['2022050100'] + algo['2022060100'] + algo['2022070100'] + algo['2022080100'] + algo['2022090100'] + algo['2022100100'] + algo['2022110100'] + algo['2022120100'] + algo['2023010100'] + algo['2023020100'] + algo['2023030100'] + algo['2023040100'] + algo['2023050100'] + algo['2023060100'] + algo['2023070100'])/97)
#         if algo['is_optimal'] == True:
#                 total_optimal += 1

#     # get max reads value
#     max_reads = math.ceil(max(max(reads_optimal), max(reads_not_optimal)) / 5000) * 5000
#     num_bins = int(max_reads/5000)
#     bins = []
#     for i in range(num_bins):
#         bins.append((i*5)+5)

#     optimal_counts = []
#     non_optimal_counts = []
#     for i in range(num_bins):
#         optimal_counts.append(0)
#         non_optimal_counts.append(0)

#     for reads in reads_optimal:
#         if reads < (bins[0]*1000):
#             optimal_counts[0]+=1
#         elif reads >= (bins[0]*1000) and (reads < (bins[1]*1000)):
#             optimal_counts[1]+=1
#         elif reads >= (bins[1]*1000) and (reads < (bins[2]*1000)):
#             optimal_counts[2]+=1
#         elif reads >= (bins[2]*1000) and (reads < (bins[3]*1000)):
#             optimal_counts[3]+=1
#         elif reads >= (bins[3]*1000) and (reads < (bins[4]*1000)):
#             optimal_counts[4]+=1
#         elif reads >= (bins[4]*1000) and (reads < (bins[5]*1000)):
#             optimal_counts[5]+=1
#         elif reads >= (bins[5]*1000) and (reads < (bins[6]*1000)):
#             optimal_counts[6]+=1
#         elif reads >= (bins[6]*1000) and (reads < (bins[7]*1000)):
#             optimal_counts[7]+=1
#         elif reads >= (bins[7]*1000) and (reads < (bins[8]*1000)):
#             optimal_counts[8]+=1
#         elif reads >= (bins[8]*1000) and (reads < (bins[9]*1000)):
#             optimal_counts[9]+=1
#         elif reads >= (bins[9]*1000) and (reads < (bins[10]*1000)):
#             optimal_counts[10]+=1
#         elif reads >= (bins[10]*1000) and (reads < (bins[11]*1000)):
#             optimal_counts[11]+=1
#         elif reads >= (bins[11]*1000) and (reads < (bins[12]*1000)):
#             optimal_counts[12]+=1
#         elif reads >= (bins[12]*1000) and (reads < (bins[13]*1000)):
#             optimal_counts[13]+=1


#     for reads in reads_not_optimal:
#         if reads < (bins[0]*1000):
#             non_optimal_counts[0]+=1
#         elif reads >= (bins[0]*1000) and (reads < (bins[1]*1000)):
#             non_optimal_counts[1]+=1
#         elif reads >= (bins[1]*1000) and (reads < (bins[2]*1000)):
#             non_optimal_counts[2]+=1
#         elif reads >= (bins[2]*1000) and (reads < (bins[3]*1000)):
#             non_optimal_counts[3]+=1
#         elif reads >= (bins[3]*1000) and (reads < (bins[4]*1000)):
#             non_optimal_counts[4]+=1
#         elif reads >= (bins[4]*1000) and (reads < (bins[5]*1000)):
#             non_optimal_counts[5]+=1
#         elif reads >= (bins[5]*1000) and (reads < (bins[6]*1000)):
#             non_optimal_counts[6]+=1
#         elif reads >= (bins[6]*1000) and (reads < (bins[7]*1000)):
#             non_optimal_counts[7]+=1
#         elif reads >= (bins[7]*1000) and (reads < (bins[8]*1000)):
#             non_optimal_counts[8]+=1
#         elif reads >= (bins[8]*1000) and (reads < (bins[9]*1000)):
#             non_optimal_counts[9]+=1
#         elif reads >= (bins[9]*1000) and (reads < (bins[10]*1000)):
#             non_optimal_counts[10]+=1
#         elif reads >= (bins[10]*1000) and (reads < (bins[11]*1000)):
#             non_optimal_counts[11]+=1
#         elif reads >= (bins[11]*1000) and (reads < (bins[12]*1000)):
#             non_optimal_counts[12]+=1
#         elif reads >= (bins[12]*1000) and (reads < (bins[13]*1000)):
#             non_optimal_counts[13]+=1

#     optimal_percent = []
#     non_optimal_percent = []
#     for i in range(num_bins):
#         optimal_percent.append(optimal_counts[i]/len(reads_optimal)*100)
#         non_optimal_percent.append(non_optimal_counts[i]/len(reads_not_optimal)*100)

#     x = np.array(bins)
#     y1 = np.array(optimal_percent)
#     y2 = np.array(non_optimal_percent)



#     # Fit power law curve
#     def power_law(x, a, b):
#         return a * np.power(x, b)

#     popt1, _ = curve_fit(power_law, x, optimal_percent)
#     popt2, _ = curve_fit(power_law, x, non_optimal_percent)


#     # Plot the data points
#     fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

#     x_smooth_fit = np.linspace(min(x), max(x), 100)
#     axes[0].plot(x_smooth_fit, power_law(x_smooth_fit, *popt1), '-', label='Power Law Fit', color="royalblue")
#     axes[1].plot(x_smooth_fit, power_law(x_smooth_fit, *popt2), '-', label='Power Law Fit', color="royalblue")


#     axes[0].scatter(x, y1, color='royalblue', label='Data')
#     axes[1].scatter(x, y2, color='royalblue', label='Data')

#     axes[0].set_title('Optimal Algos', fontsize=14)
#     axes[0].set_xlabel('Monthly Views (in thousands)', fontsize=14)
#     axes[0].set_ylabel('Percent', fontsize=14)

#     axes[1].set_title('Non-Optimal Algos', fontsize=14)
#     axes[1].set_xlabel('Monthly Views (in thousands)', fontsize=14)
#     axes[1].set_ylabel('Percent', fontsize=14)

#     fig.suptitle('Wikipedia Page Views:', fontsize=16)

#     plt.tight_layout()
#     plt.savefig('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/Paper/fig1.pdf')
#     plt.savefig('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/Paper/fig1.png')
#     plt.show()

def figure2():
    df = pd.read_csv('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/wikipedia/merged.csv')
    df = df[['One of them','Family Name', 'is_optimal', 'average_monthly_reads']]
    df = df.replace('#VALUE!', pd.NA).dropna()
    merged_dict = df.to_dict(orient='records')

    # Sample data
    optimal_dict = {}
    non_optimal_dict = {}
    for algo in merged_dict:
        optimal_dict[algo['Family Name']] = 0
        non_optimal_dict[algo['Family Name']] = 0


    for algo in merged_dict:
        if algo["is_optimal"]:
            optimal_dict[algo['Family Name']] += 1
        else:
            non_optimal_dict[algo['Family Name']] += 1


    named_percent_optimal = []
    named_percent_non_optimal = []

    for key, value in optimal_dict.items():
        named_percent_optimal.append((key, value/(value + non_optimal_dict[key])))
        named_percent_non_optimal.append((key, non_optimal_dict[key]/(value + non_optimal_dict[key])))

    named_percent_optimal = sorted(named_percent_optimal, key=lambda x: (x[1], x[0]))
    named_percent_non_optimal = sorted(named_percent_non_optimal, key=lambda x: (-x[1], x[0]))

    categories = []
    percent_optimal = []
    percent_non_optimal = []

    for i in range(len(named_percent_optimal)):
        percent_optimal.append(named_percent_optimal[i][1] * 100)
        percent_non_optimal.append(named_percent_non_optimal[i][1] * 100)
        categories.append(named_percent_optimal[i][0])

    no_optimal = 0
    all_optimal = 0
    for family in percent_optimal:
        if family == 0:
            no_optimal += 1
        elif family == 100:
            all_optimal += 1
    print("percent of families with no optimal algorithm:", no_optimal/len(percent_optimal))
    print("percent of families with all optimal algorithms:", all_optimal/len(percent_optimal))
    # Create stacked bar plot
    plt.figure(figsize = (6.4, 4.8), dpi= 800)
    plt.bar(categories, percent_optimal, color='royalblue')
    plt.bar(categories, percent_non_optimal, bottom = percent_optimal, color='lightsteelblue')

    # Add labels and legend
    plt.xticks([])
    plt.legend(["optimal", "non-optimal"])
    plt.axhline(20, linestyle='--', color='dimgray')
    plt.axhline(40, linestyle='--', color='dimgray')
    plt.axhline(60, linestyle='--', color='dimgray')
    plt.axhline(80, linestyle='--', color='dimgray')
    plt.xlabel('Algorithmic Problems')
    plt.ylabel('Percent')
    plt.title('Fraction of Optimal Algorithms in Each Problem Family on Wikipedia')
    plt.savefig("/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/Paper/fig2.pdf")
    plt.savefig("/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/Paper/fig2.png")
    # Show plot
    plt.show()

def figure2appendix():
    df = pd.read_csv('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/wikipedia/merged.csv')
    df = df[['One of them','Family Name', 'is_optimal', 'average_monthly_reads']]
    df = df.replace('#VALUE!', pd.NA).dropna()
    merged_dict = df.to_dict(orient='records')

    # Sample data
    optimal_dict = {}
    non_optimal_dict = {}
    for algo in merged_dict:
        optimal_dict[algo['Family Name']] = 0
        non_optimal_dict[algo['Family Name']] = 0


    for algo in merged_dict:
        if algo["is_optimal"]:
            optimal_dict[algo['Family Name']] += 1
        else:
            non_optimal_dict[algo['Family Name']] += 1

    named_percent_optimal = []
    named_percent_non_optimal = []

    for key, value in optimal_dict.items():
        named_percent_optimal.append((key, value/(value + non_optimal_dict[key])))
        named_percent_non_optimal.append((key, non_optimal_dict[key]/(value + non_optimal_dict[key])))

    named_percent_optimal = sorted(named_percent_optimal, key=lambda x: (x[1], x[0]))
    named_percent_non_optimal = sorted(named_percent_non_optimal, key=lambda x: (-x[1], x[0]))

    categories = []
    percent_optimal = []
    percent_non_optimal = []

    for i in range(len(named_percent_optimal)):
        percent_optimal.append(named_percent_optimal[i][1]*100)
        percent_non_optimal.append(named_percent_non_optimal[i][1]*100)
        categories.append(named_percent_optimal[i][0])

    # Create stacked bar plot
    plt.figure(figsize=(6, 30))
    plt.barh(categories, percent_optimal, label='Optimal', color='royalblue')
    plt.barh(categories, percent_non_optimal, left=percent_optimal, label='Non-Optimal', color='lightsteelblue')

    # Add labels and legend
    plt.xlabel('Percent')
    plt.ylabel('Problem Family')
    plt.title('Fraction of Optimal Algorithms by Problem Family')
    plt.legend()
    plt.ylim(-0.5, len(categories)-0.5)
    plt.savefig("/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/Paper/fig2_appendix.png", dpi=300, bbox_inches = "tight")
    plt.savefig("/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/Paper/fig2_appendix.pdf", dpi=300, bbox_inches = "tight")
    # Show plot
    # plt.show()

def figure3A():
    df = pd.read_csv('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/wikipedia/sheet1_output_views.csv')
    df = df[['One of them','Time Complexity Class']]
    df = df.replace('#VALUE!', pd.NA).dropna()
    df['Time Complexity Class'] = df['Time Complexity Class'].astype(float)
    merged_dict = df.to_dict(orient='records')
    for algo in merged_dict:
        if algo['Time Complexity Class'] >= 2 and algo['Time Complexity Class'] < 3:
            algo['Time Complexity Bin'] = 2
        elif algo['Time Complexity Class'] < 4:
            algo['Time Complexity Bin'] = 3
        elif algo['Time Complexity Class'] < 5:
            algo['Time Complexity Bin'] = 4
        elif algo['Time Complexity Class'] < 6:
            algo['Time Complexity Bin'] = 5
        elif algo['Time Complexity Class'] < 7:
            algo['Time Complexity Bin'] = 6
        elif algo['Time Complexity Class'] < 8:
            algo['Time Complexity Bin'] = 7
        elif algo['Time Complexity Class'] < 9:
            algo['Time Complexity Bin'] = 8
        if algo['One of them'] == 1:
            algo['Not on Wikipedia'] = 0
        elif algo['One of them'] == 0:
            algo['Not on Wikipedia'] = 1

    df = pd.df(merged_dict)

    crosstb_prop = pd.crosstab(df["Time Complexity Bin"], df['Not on Wikipedia'], normalize="index")
    crosstb_prop *= 100
    crosstb = pd.crosstab(df["Time Complexity Bin"], df['Not on Wikipedia'])

    crosstb.to_csv('/Users/bellasteedly/Desktop/results.csv')


    crosstb_prop.plot(kind='bar', stacked=True, color=['royalblue', 'white'], edgecolor = "black", figsize=(10, 8), width=0.7)

    #legend
    plt.legend(["On Wikipedia", "Not on Wikipedia"], loc="lower left", ncol=2)

    #title and axes
    plt.xlabel("")
    plt.title('Time complexity for algorithms on Wikipedia')
    plt.ylabel("")

    bin_labels = ["\nlogarithmic", "linear", "\nquasilinear (nlogn)", "quadratic", "\ncubic", "polynomial (>3)", "\nexponential/factorial"]

    # # Set the x-ticks and x-tick labels
    ax = plt.gca()
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=100))
    ax.set_xticks(range(len(bin_labels)))
    ax.set_xticklabels(bin_labels, rotation=0, ha='center')
    plt.tick_params(top=False, labeltop=False, bottom=True, labelbottom=True)

    for n, x in enumerate([*crosstb_prop.index.values]):
        for (proportion, count, y_loc) in zip(crosstb_prop.loc[x],
                                            crosstb.loc[x],
                                            crosstb_prop.loc[x].cumsum()):
                    
            plt.text(x=n,
                    y=(y_loc - proportion) + (proportion / 2),
                    s=f'{count}\n({int(round(proportion, 0))}%)', 
                    color="black",
                    ha='center',
                    fontsize=10,
                    fontweight="bold")
    plt.tight_layout()
    plt.savefig('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/Paper/fig3A.pdf')
    plt.savefig('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/Paper/fig3A.png')
    plt.show()

def figure3B():
    df = pd.read_csv('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/wikipedia/merged.csv')
    df = df[['average_monthly_reads','Time Complexity Class']]
    df = df.replace('#VALUE!', pd.NA).dropna()

    num_bins = 4
    df = df.astype(float)
    merged_dict = df.to_dict(orient='records')
    for algo in merged_dict:
        if algo['Time Complexity Class'] >=2 and algo['Time Complexity Class'] < 3:
            algo['Time Complexity Bin'] = 2
        elif algo['Time Complexity Class'] < 4:
            algo['Time Complexity Bin'] = 3
        elif algo['Time Complexity Class'] < 5:
            algo['Time Complexity Bin'] = 4
        elif algo['Time Complexity Class'] < 6:
            algo['Time Complexity Bin'] = 5
        elif algo['Time Complexity Class'] < 7:
            algo['Time Complexity Bin'] = 6
        elif algo['Time Complexity Class'] < 8:
            algo['Time Complexity Bin'] = 7
        elif algo['Time Complexity Class'] < 9:
            algo['Time Complexity Bin'] = 8
        
        if (algo['average_monthly_reads'] == 0):
            merged_dict.remove(algo)
        elif (algo['average_monthly_reads'] <100):
            algo['reads_bin'] = 3
        elif algo['average_monthly_reads'] <1000:
            algo['reads_bin'] = 2
        elif algo['average_monthly_reads'] <10000:
            algo['reads_bin'] = 1
        elif algo['average_monthly_reads'] >=10000:
            algo['reads_bin'] = 0
        else:
            merged_dict.remove(algo)

    df = pd.df(merged_dict)

    crosstb_prop = pd.crosstab(df["Time Complexity Bin"], df['reads_bin'], normalize="index")
    crosstb_prop *= 100
    crosstb = pd.crosstab(df["Time Complexity Bin"], df['reads_bin'])

    # Define the desired order of rows
    # new_bin_order = [3, 4, 5, 8, 6, 7, 2, 1]

    bin_labels = ["\nlogarithmic", "linear", "\nquasilinear (nlogn)", "quadratic", "\ncubic", "polynomial (>3)", "\nexponential/factorial"]

    # Reindex the df
    # crosstb_prop_reindexed = crosstb_prop.reindex(new_bin_order)
    # crosstb_reindexed = crosstb.reindex(new_bin_order)

    crosstb_prop.plot(kind='bar', stacked=True, color=['royalblue', 'cornflowerblue', 'lightsteelblue', 'aliceblue'], edgecolor='black', figsize=(10, 8), width=0.7)

    #title and axes
    plt.xlabel("Time Complexity")
    plt.title('Wikipedia Views by Time Complexity')

    # # Set the x-ticks and x-tick labels
    ax = plt.gca()
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=100))
    ax.set_xlabel('')

    ax.set_xticks(range(len(bin_labels)))
    ax.set_xticklabels(bin_labels, rotation=0, ha='center')
    ax.tick_params(axis='x', labelsize=8)
    ax.get_legend().remove()

    for n, x in enumerate([*crosstb_prop.index.values]):
        sum = 0
        for (proportion, count, y_loc) in zip(crosstb_prop.loc[x],
                                            crosstb.loc[x],
                                            crosstb_prop.loc[x].cumsum()):
            sum += count
        plt.text(x=n,
                    y=(y_loc) + 2,
                    s="n=" + str(sum), 
                    color="black",
                    ha='center',
                    va='bottom',
                    fontsize=8,
                    fontweight="bold")


    y = 0
    for n, x in enumerate([*crosstb_prop.index.values]):
        total = 0
        for (proportion, count, y_loc) in zip(crosstb_prop.loc[x],
                                            crosstb.loc[x],
                                            crosstb_prop.loc[x].cumsum()):
            if (proportion != 0) & ((y % num_bins == num_bins-1)):
                if (proportion < 5): 
                    plt.text(x=n,
                    y=(y_loc),
                    s='1-99', 
                    color="black",
                    ha='center',
                    va='bottom',
                    fontsize=6,
                    fontweight="bold")
                else:
                    plt.text(x=n,
                        y=(y_loc - proportion) + (proportion / 2),
                        s='1-99', 
                        color="black",
                        ha='center',
                        va='center',
                        fontsize=6,
                        fontweight="bold")
            elif (proportion != 0) & ((y % num_bins == num_bins-2)):
                plt.text(x=n,
                    y=(y_loc - proportion) + (proportion / 2),
                    s='100-999', 
                    color="black",
                    ha='center',
                    va='center',
                    fontsize=6,
                    fontweight="bold")
            elif (proportion != 0) & ((y % num_bins == num_bins-3)):
                plt.text(x=n,
                    y=(y_loc - proportion) + (proportion / 2),
                    s='1,000-9,999', 
                    color="white",
                    ha='center',
                    va='center',
                    fontsize=6,
                    fontweight="bold")
            elif (proportion != 0) & ((y % num_bins == num_bins-4)):
                plt.text(x=n,
                    y=(y_loc - proportion) + (proportion / 2),
                    s='10,000+', 
                    color="white",
                    ha='center',
                    va='center',
                    fontsize=6,
                    fontweight="bold")
            y+=1
    plt.tick_params(top=False, labeltop=False, bottom=True, labelbottom=True)

    plt.savefig('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/Paper/fig3B.pdf')
    plt.savefig('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/Paper/fig3B.png')
    plt.show()

def figure4A():
    df = pd.read_csv('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/wikipedia/sheet1_output_views.csv')
    df = df[['One of them','Domains']]
    df = df.replace('#VALUE!', pd.NA).dropna()
    merged_dict = df.to_dict(orient='records')
    for algo in merged_dict:
        if algo['One of them'] == 1:
            algo['Wikipedia?'] = 'On Wikipedia'
        elif algo['One of them'] == 0:
            algo['Wikipedia?'] = 'Not on Wikipedia'

    df = pd.df(merged_dict)

    cross_tab = pd.crosstab(index=df['Domains'], columns=df['Wikipedia?'])
    cross_tab.to_csv('/Users/bellasteedly/Desktop/results.csv')

    cross_tab_prop = pd.crosstab(index=df['Domains'], columns=df['Wikipedia?'], normalize="index")

    cross_tab_prop = cross_tab_prop[['On Wikipedia', 'Not on Wikipedia']]
    cross_tab = cross_tab[['On Wikipedia', 'Not on Wikipedia']]

    cross_tab_prop *= 100

    cross_tab_prop = cross_tab_prop.reindex(["Cryptography", "Statistics", "Operating Systems", "Numerical Analysis", "Combinatorics", "Image Processing", "Robotics", "Bioinformatics", "Signal Processing", "Databases"])
    cross_tab = cross_tab.reindex(["Cryptography", "Statistics", "Operating Systems", "Numerical Analysis", "Combinatorics", "Image Processing", "Robotics", "Bioinformatics", "Signal Processing", "Databases"])

    cross_tab_prop.plot(kind='bar', stacked=True, color=['royalblue', 'white'], edgecolor = "black", figsize=(10, 8), width=0.7)

    plt.legend(loc="lower left", ncol=2)
    plt.xlabel("")
    plt.title("Domain for algorithms on Wikipedia and not on Wikipedia")
    plt.ylabel("")

    bin_labels = ["Cryptography", "\nStatistics", "Operating Systems", "\nNumerical Analysis", "Combinatorics", "\nImage Processing", "Robotics", "\nBioinformatics", "Signal Processing", "\nDatabases"]

    # Set the x-ticks and x-tick labels
    ax = plt.gca()
    # ax.set_xticks(range(len(bin_labels)))
    ax.set_xticklabels(bin_labels, rotation=0, ha='center')

    legend_labels = ['On Wikipedia', 'Not on Wikipedia']
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles, legend_labels, loc="lower left", ncol=2)

    for n, x in enumerate([*cross_tab_prop.index.values]):
        for (proportion, count, y_loc) in zip(cross_tab_prop.loc[x],
                                            cross_tab.loc[x],
                                            cross_tab_prop.loc[x].cumsum()): 
            if proportion != 0:
                plt.text(x=n,
                        y=(y_loc - proportion) + (proportion / 2),
                        s=f'{count}\n({int(round(proportion, 1))}%)', 
                        color="black",
                        fontsize=8,
                        ha='center',
                        fontweight="bold")
    plt.tick_params(top=False, labeltop=False, bottom=True, labelbottom=True)
    plt.savefig('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/Paper/fig4A.png')
    plt.savefig('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/Paper/fig4A.pdf')
    # plt.show()

def figure4B():
    df = pd.read_csv('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/wikipedia/merged.csv')
    df = df[['average_monthly_reads','Domains']]
    df['Domains'] = df['Domains'].replace('#VALUE!', pd.NA)
    df['average_monthly_reads'] = df['average_monthly_reads'].fillna(0)
    df = df.dropna()
    num_bins = 4
    merged_dict = df.to_dict(orient='records')
    for algo in merged_dict: 
        if algo['average_monthly_reads'] != 0:
            if algo['average_monthly_reads'] <100:
                algo['reads_bin'] = 3
            elif algo['average_monthly_reads'] <1000:
                algo['reads_bin'] = 2
            elif algo['average_monthly_reads'] <10000:
                algo['reads_bin'] = 1
            elif algo['average_monthly_reads'] >=10000:
                algo['reads_bin'] = 0

    df = pd.df(merged_dict)

    crosstb_prop = pd.crosstab(df["Domains"], df['reads_bin'], normalize="index")
    crosstb_prop *= 100
    crosstb = pd.crosstab(df["Domains"], df['reads_bin'])

    crosstb_prop = crosstb_prop.reindex(["Cryptography", "Statistics", "Operating Systems", "Numerical Analysis", "Combinatorics", "Image Processing", "Robotics", "Bioinformatics", "Signal Processing", "Databases"])
    crosstb = crosstb.reindex(["Cryptography", "Statistics", "Operating Systems", "Numerical Analysis", "Combinatorics", "Image Processing", "Robotics", "Bioinformatics", "Signal Processing", "Databases"])

    crosstb_prop.plot(kind='bar', stacked=True, color=['royalblue', 'cornflowerblue', 'lightsteelblue', 'aliceblue'], edgecolor='black', figsize=(10, 6), width=0.7)

    #title
    plt.title('Wikipedia Views by Domain')

    # # Set the x-ticks and x-tick labels
    ax = plt.gca()
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=100))
    ax.set_xlabel('')

    bin_labels = ["Cryptography", "\nStatistics", "Operating Systems", "\nNumerical Analysis", "Combinatorics", "\nImage Processing", "Robotics", "\nBioinformatics", "Signal Processing", "\nDatabases"]
    ax.set_xticklabels(bin_labels, rotation=0, ha='center')
    ax.tick_params(axis='x', labelsize=8)
    ax.get_legend().remove()

    for n, x in enumerate([*crosstb_prop.index.values]):
        sum = 0
        for (proportion, count, y_loc) in zip(crosstb_prop.loc[x],
                                            crosstb.loc[x],
                                            crosstb_prop.loc[x].cumsum()):
            sum += count
        plt.text(x=n,
                    y=(y_loc) + 2,
                    s="n=" + str(sum), 
                    color="black",
                    ha='center',
                    va='bottom',
                    fontsize=8,
                    fontweight="bold")


    y = 0
    for n, x in enumerate([*crosstb_prop.index.values]):
        total = 0
        for (proportion, count, y_loc) in zip(crosstb_prop.loc[x],
                                            crosstb.loc[x],
                                            crosstb_prop.loc[x].cumsum()):
            if (proportion < 3) & (proportion != 0) & ((y % num_bins == num_bins-1)):
                plt.text(x=n,
                    y=(y_loc),
                    s='1-99', 
                    color="black",
                    ha='center',
                    va='bottom',
                    fontsize=6,
                    fontweight="bold")
            elif (proportion != 0) & ((y % num_bins == num_bins-1)):
                plt.text(x=n,
                    y=(y_loc - proportion) + (proportion / 2),
                    s='1-99', 
                    color="black",
                    ha='center',
                    va='center',
                    fontsize=6,
                    fontweight="bold")
            elif (proportion != 0) & ((y % num_bins == num_bins-2)):
                plt.text(x=n,
                    y=(y_loc - proportion) + (proportion / 2),
                    s='100-999', 
                    color="black",
                    ha='center',
                    va='center',
                    fontsize=6,
                    fontweight="bold")
            elif (proportion != 0) & ((y % num_bins == num_bins-3)):
                plt.text(x=n,
                    y=(y_loc - proportion) + (proportion / 2),
                    s='1,000-9,999', 
                    color="white",
                    ha='center',
                    va='center',
                    fontsize=6,
                    fontweight="bold")
            elif (proportion != 0) & ((y % num_bins == num_bins-4)):
                plt.text(x=n,
                    y=(y_loc - proportion) + (proportion / 2),
                    s='10,000+', 
                    color="white",
                    ha='center',
                    va='center',
                    fontsize=6,
                    fontweight="bold")
            y+=1

    plt.savefig('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/Paper/fig4B.png')
    plt.savefig('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/Paper/fig4B.pdf')
    plt.show()

def figure5():
    df = pd.read_csv('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/wikipedia/merged1.csv')
    df = df[['is_optimal', 'is_optimal_space', 'One of them', 'Family Name']]
    data = df.to_dict(orient='records')
    families = {}
    for algo in data:
        if algo['One of them'] == 1:
            if algo['Family Name'] not in families.keys():
                families[algo['Family Name']] = [algo['is_optimal'], algo['is_optimal_space']]
            else:
                if algo['is_optimal']:
                    families[algo['Family Name']][0] = True
                if algo['is_optimal_space']:
                    families[algo['Family Name']][1] = True

    total = 0
    opt_time_space = 0
    opt_time = 0
    opt_space = 0
    none = 0

    for key, value in families.items():
        total += 1
        if value[0] and value[1]:
            opt_time_space += 1
        elif value[0]:
            opt_time += 1
        elif value[1]:
            opt_space += 1
        else: 
            none += 1

    opt_time_space = opt_time_space/total
    opt_time = opt_time/total
    opt_space = opt_space/total
    none = none/total

    x = np.array([-10, 10, -10, 10])
    y = np.array([10,10, -10, -10])
    n = [str(round(opt_time_space*100, 2)) + '%', str(round(opt_space*100, 2)) + '%', str(round(opt_time*100, 2)) + '%', str(round(none*100, 2)) + '%']
    plt.xlim(-20, 20)
    plt.ylim(-20, 20)

    plt.scatter(x, y, alpha=0)
    for i, txt in enumerate(n):
        plt.annotate(txt, (x[i], y[i]), ha='center', va='center', fontsize=20)
    plt.axhline(y = 0, color = 'black', linestyle = '-', linewidth = 1)
    plt.axvline(x = 0, color = 'black', linestyle = '-', linewidth = 1) 
    plt.title('Fraction of Problem Families where Optimal Algorithm is on Wikipedia')
    plt.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False, length = 0)
    plt.xticks([-10, 10], labels=['Optimal Time', 'Non-Optimal Time'])
    plt.yticks([-10, 10], labels=['Non-Optimal\nSpace', 'Optimal\nSpace'])

    plt.savefig('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/Paper/fig5.png', bbox_inches='tight')
    plt.savefig('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/Paper/fig5.pdf', bbox_inches='tight')
    # plt.show()

def figure6():
    #Import CSV file
    df = pd.read_csv('merged.csv')
    df['Parallel?'] = df['Parallel?'].str.replace(r'\D', '', regex=True)
    df['Parallel?'] = df['Parallel?'].astype('Int64')
    df['Approximate?'] = df['Approximate?'].str.replace(r'\D', '', regex=True)
    df['Approximate?'] = df['Approximate?'].astype('Int64')
    df = df.loc[(df['Quantum?'] == 0) & (df['Parallel?'] == 0) & (df['Exact algorithm?'] == 1) & (df['Exact Problem Statement?'] == 1) & (df['Randomized?'] == 0) & (df['Approximate?'] == 0) & (df['GPU-based?'] == 0)]
    algorithm_families = df['Family Name'].unique()

    family_names_wiki = []
    # iterate through each row in the df and add the family name to a list of family names if one of them is 1
    for index, row in df.iterrows():
        if row['One of them'] == 1:
            family_names_wiki.append(row['Family Name'])
    # convert the list to a set then back to a list to remove duplicates. This is the list of families on wiki
    family_names = list(set(family_names_wiki))
    # iterate through each row in the df and check to see if the family name is in the list of families. If it is, keep it. Otherwise remove. 
    df_wiki = df[df['Family Name'].isin(family_names_wiki)]
    algorithm_families_wiki = df_wiki['Family Name'].unique()

    families_improving_per_decade = [0,0,0,0,0,0,0,0]
    for name in algorithm_families:
        algorithms = df.loc[df['Family Name'] == name]
        time_complexity_improvement_algorithms = algorithms.loc[algorithms['Time Complexity Improvement?']==1]
        time_complexity_improvement_algorithms_years = time_complexity_improvement_algorithms['Year'].tolist()
        time_complexity_improvement_algorithms_years.sort()
        time_complexity_improvement_algorithms_years.pop(0)
        temp_decades = [0,0,0,0,0,0,0,0]
        for q in time_complexity_improvement_algorithms_years:
            #Adjust the publication year to now divide them by 10 and then subtract 194 to bring them to a scale from 0 - 7.
            temp_i = int(math.floor(q / 10.0)) - 194
            #If there is an improvement in a decade, make that decade store 1 for this family. 
            if temp_i < 0:
                temp_i = 0
            if temp_decades[temp_i] !=1:
                temp_decades[temp_i] = 1 

        #From this family, store this temp_decades to the aggregator Decade_families_with_improvements.
        for w in range(8):
            if temp_decades[w] == 1:
                families_improving_per_decade[w] = families_improving_per_decade[w] + 1

    origin_years = []
    origin_years_floor = []
    for name in algorithm_families:
        algorithms = df.loc[df['Family Name'] == name]
        origin_years.append(algorithms['Year'].min())
        origin_years_floor.append(int(math.floor(algorithms['Year'].min() / 10.0)) * 10)
    group_origin_decades = [0,0,0,0,0,0,0,0]
    for decade in range(8):
        group_origin_decades[decade] = origin_years_floor.count(1940+decade*10)

    #Cumulative sum of families
    cumulative = []
    cumulative_all = []
    s = 0
    for i in group_origin_decades:
        s = s + i
        cumulative.append(s)

    #Find % of families improving in a decade
    for i in range(8):
        cumulative_all.append((families_improving_per_decade[i]/(1.0*cumulative[i]))*100)
        

    algorithm_families_wiki = []
    for family in algorithm_families:
        constraint1 = df['Family Name'] == family
        constraint2 = df['One of them'] == True
        combined_constraints = constraint1 & constraint2
        if combined_constraints.any():
            algorithm_families_wiki.append(family)
    algorithm_families_wiki = np.array(algorithm_families_wiki)
    
    families_improving_per_decade_wiki = [0,0,0,0,0,0,0,0]
    for name in algorithm_families_wiki:
        algorithms = df.loc[df['Family Name'] == name]
        time_complexity_improvement_algorithms = algorithms.loc[algorithms['Time Complexity Improvement?']==1]
        time_complexity_improvement_algorithms_years = time_complexity_improvement_algorithms['Year'].tolist()
        time_complexity_improvement_algorithms_years.sort()
        time_complexity_improvement_algorithms_years.pop(0)
        temp_decades = [0,0,0,0,0,0,0,0]
        for q in time_complexity_improvement_algorithms_years:
            #Adjust the publication year to now divide them by 10 and then subtract 194 to bring them to a scale from 0 - 7.
            temp_i = int(math.floor(q / 10.0)) - 194
            #If there is an improvement in a decade, make that decade store 1 for this family. 
            if temp_i < 0:
                temp_i = 0
            if temp_decades[temp_i] !=1:
                temp_decades[temp_i] = 1 
        #From this family, store this temp_decades to the aggregator Decade_families_with_improvements.
        for w in range(8):
            if temp_decades[w] == 1:
                families_improving_per_decade_wiki[w] = families_improving_per_decade_wiki[w] + 1
    #Find % of families improving in a decade
    cumulative_wiki = []
    for i in range(8):
        cumulative_wiki.append((families_improving_per_decade_wiki[i]/(1.0*cumulative[i]))*100)
    
    decades = ('1940s and earlier','1950s','1960s','1970s','1980s','1990s','2000s','2010s')
    x = np.arange(len(decades))
    width = 0.35
    fig=plt.figure(figsize=(14, 6))
    plt.bar(x - width/2, cumulative_all, width, align='center', label='All', alpha=0.5)
    plt.bar(x + width/2, cumulative_wiki, width, align='center', label='Wikipedia', alpha=0.5)
    plt.xticks(np.arange(len(decades)), decades)
    for i in range(len(cumulative_all)):
            plt.text(x[i] - width/2,cumulative_all[i],str(round(cumulative_all[i])) + '%',ha = 'center')
            plt.text(x[i] + width/2,cumulative_wiki[i],str(round(cumulative_wiki[i])) + '%',ha = 'center')
    plt.legend()
    plt.ylabel('Percentage of Families')
    plt.title('Percentage of Algorithm Families Improved Each Decade')
    plt.savefig("/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/Wellesley/AlgorithmsWiki/Paper/fig6.pdf")
    plt.savefig("/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/Wellesley/AlgorithmsWiki/Paper/fig6.png")
    plt.show()

# def fig_7_helper(problem_size, algorithm_families, df):
#     improvement_rate_percentages = []
#     improvement_rate_percentages_classes = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]  #Within this function, use the default function.
#     for name in algorithm_families:
#         print("----------------------")
#         print(name)
#         algorithms = df.loc[df['Family Name'] == name] #Use another dataframe on the family level - record the improvement %. Use it separately and call it as a parameter.
#         time_complexity_improvement_algorithms = algorithms.loc[algorithms['Time Complexity Improvement?']==1]
#         print("og algos:", time_complexity_improvement_algorithms)
#         time_complexity_improvement_algorithms = time_complexity_improvement_algorithms[~time_complexity_improvement_algorithms[problem_size].str.contains('#VALUE!', na=False)]
#         time_complexity_improvement_algorithms = time_complexity_improvement_algorithms[~time_complexity_improvement_algorithms[problem_size].str.contains('#DIV/0!', na=False)]
#         time_complexity_improvement_algorithms[problem_size] = time_complexity_improvement_algorithms[problem_size].astype(float)
#         time_complexity_improvement_algorithms = time_complexity_improvement_algorithms.dropna(subset=[problem_size])
#         # deal with inf condition
#         if 'inf' in time_complexity_improvement_algorithms[problem_size]:
#             print("found infinity")
#             break
#         print("new algos:", time_complexity_improvement_algorithms[problem_size])
#         if len(time_complexity_improvement_algorithms[problem_size]) > 0:
#             improvement_val = time_complexity_improvement_algorithms[problem_size].max()/time_complexity_improvement_algorithms[problem_size].min()
#             print("improvement", improvement_val)
#             print(time_complexity_improvement_algorithms[problem_size])
#             print("improvement_val:", improvement_val)
#             year_difference = 2018-time_complexity_improvement_algorithms['Year'].min()
#             print("year difference:", year_difference)
#             inv_year_difference = 1/(year_difference*1.0)
#             print("inv_year_difference:", inv_year_difference)
#             improvement_rate_percentage = (math.pow(improvement_val,inv_year_difference) - 1)*100
#             print("improvement_rate_percentage:", improvement_rate_percentage)
#             improvement_rate_percentages.append(improvement_rate_percentage)
#             improvement_rate_percentages_classes[int(min((improvement_rate_percentage/5),14))] = improvement_rate_percentages_classes[int(min((improvement_rate_percentage/5),14))] + 1
#     return improvement_rate_percentages_classes
    
def fig_7_helper(problem_size, algorithm_families, df):
    improvement_rate_percentages = []
    improvement_rate_percentages_classes = [0,0,0,0,0,0,0,0,0,0,0,0]  #Within this function, use the default function.
    for name in algorithm_families:
        print("----------------------")
        print(name)
        algorithms = df.loc[df['Family Name'] == name] #Use another dataframe on the family level - record the improvement %. Use it separately and call it as a parameter.
        time_complexity_improvement_algorithms = algorithms.loc[algorithms['Time Complexity Improvement?']==1]
        print("og algos:", time_complexity_improvement_algorithms)
        time_complexity_improvement_algorithms = time_complexity_improvement_algorithms[~time_complexity_improvement_algorithms[problem_size].str.contains('#VALUE!', na=False)]
        time_complexity_improvement_algorithms = time_complexity_improvement_algorithms[~time_complexity_improvement_algorithms[problem_size].str.contains('#DIV/0!', na=False)]
        time_complexity_improvement_algorithms[problem_size] = time_complexity_improvement_algorithms[problem_size].astype(float)
        time_complexity_improvement_algorithms = time_complexity_improvement_algorithms.dropna(subset=[problem_size])
        # deal with inf condition
        if 'inf' in time_complexity_improvement_algorithms[problem_size]:
            print("found infinity")
            break
        print("new algos:", time_complexity_improvement_algorithms[problem_size])
        if len(time_complexity_improvement_algorithms[problem_size]) > 0:
            if time_complexity_improvement_algorithms[problem_size].min() == 0:
                improvement_val = inf
            else:
                improvement_val = time_complexity_improvement_algorithms[problem_size].max()/time_complexity_improvement_algorithms[problem_size].min()
            print("improvement", improvement_val)
            print(time_complexity_improvement_algorithms[problem_size])
            print("improvement_val:", improvement_val)
            year_difference = 2018-time_complexity_improvement_algorithms['Year'].min()
            print("year difference:", year_difference)
            inv_year_difference = 1/(year_difference*1.0)
            print("inv_year_difference:", inv_year_difference)
            improvement_rate_percentage = (math.pow(improvement_val,inv_year_difference) - 1)*100
            print("improvement_rate_percentage:", improvement_rate_percentage)
            improvement_rate_percentages.append(improvement_rate_percentage)
            print("improvement_rate_percentages_classes", improvement_rate_percentages_classes)
            print("int(min((improvement_rate_percentage/10),11))", int(min((improvement_rate_percentage/10),11)))
            if improvement_rate_percentage <= 100:
                improvement_rate_percentages_classes[int(improvement_rate_percentage/10)] = improvement_rate_percentages_classes[int(improvement_rate_percentage/10)] + 1
            elif (improvement_rate_percentage > 100) and (improvement_rate_percentage <= 1000):
                improvement_rate_percentages_classes[10] = improvement_rate_percentages_classes[10] + 1
            elif improvement_rate_percentage > 1000:
                improvement_rate_percentages_classes[11] = improvement_rate_percentages_classes[11] + 1
    for i in range(len(improvement_rate_percentages_classes)):
        improvement_rate_percentages_classes[i] = improvement_rate_percentages_classes[i]/len(algorithm_families)
    return improvement_rate_percentages_classes

def figure7():
    #Import CSV file
    df = pd.read_csv('merged.csv')
    df['Parallel?'] = df['Parallel?'].str.replace(r'\D', '', regex=True)
    df['Parallel?'] = df['Parallel?'].astype('Int64')
    df['Approximate?'] = df['Approximate?'].str.replace(r'\D', '', regex=True)
    df['Approximate?'] = df['Approximate?'].astype('Int64')
    df = df.loc[(df['Quantum?'] == 0) & (df['Parallel?'] == 0) & (df['Exact algorithm?'] == 1) & (df['Exact Problem Statement?'] == 1) & (df['Randomized?'] == 0) & (df['Approximate?'] == 0) & (df['GPU-based?'] == 0)]
    algorithm_families = df['Family Name'].unique()

    family_names_wiki = []
    # iterate through each row in the df and add the family name to a list of family names if one of them is 1
    for index, row in df.iterrows():
        if row['One of them'] == 1:
            family_names_wiki.append(row['Family Name'])
    # convert the list to a set then back to a list to remove duplicates. This is the list of families on wiki
    family_names = list(set(family_names_wiki))
    # iterate through each row in the df and check to see if the family name is in the list of families. If it is, keep it. Otherwise remove. 
    df_wiki = df[df['Family Name'].isin(family_names_wiki)]
    algorithm_families_wiki = df_wiki['Family Name'].unique()

    thousand_all = fig_7_helper('n = 1000 scale', algorithm_families, df)
    million_all = fig_7_helper('n = 10^6 scale', algorithm_families, df)
    billion_all = fig_7_helper('n = 10^9 scale', algorithm_families, df)

    thousand_wiki = fig_7_helper('n = 1000 scale', algorithm_families_wiki, df_wiki)
    million_wiki = fig_7_helper('n = 10^6 scale', algorithm_families_wiki, df_wiki)
    billion_wiki = fig_7_helper('n = 10^9 scale', algorithm_families_wiki, df_wiki)

    fig, axs = plt.subplots(3, 1, figsize=(14, 18))

    #Thousand figure
    bins = ['0-10%', '10-20%', '20-30%','30-40%','40-50%','50-60%','60-70%','70-80%','80-90%','90-100%','100-1000%','>1000%']
    x = np.arange(len(bins))
    a1 = thousand_all
    a2 = thousand_wiki
    # fig=plt.figure(figsize=(14, 6))
    width = 0.4
    bars1 = axs[0].bar(x - width/2, a1, width, align='center', label='All Families', alpha=0.5)
    bars2 = axs[0].bar(x + width/2, a2, width, align='center', label='Wikipedia Families', alpha=0.5)
    axs[0].set_title('Problem Size: n = 1 thousand')
    axs[0].set_xticks(np.arange(len(bins)), bins)
    axs[0].yaxis.set_major_formatter(mticker.PercentFormatter(1))
    axs[0].set_xlabel('Average Percentage Improvement Per Year')
    axs[0].set_ylabel('Percentage of Algorithm Families')
    axs[0].legend()

    for a in bars1:
        height = a.get_height()
        axs[0].text(a.get_x() + a.get_width()/2.0, height, f'{height*100:.0f}%', ha='center', va='bottom')

    for a in bars2:
        height = a.get_height()
        axs[0].text(a.get_x() + a.get_width()/2.0, height, f'{height*100:.0f}%', ha='center', va='bottom')


    # plt.savefig("/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/Wellesley/AlgorithmsWiki/Paper/fig7a.pdf")
    # plt.savefig("/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/Wellesley/AlgorithmsWiki/Paper/fig7a.png")

    #Million figure
    b1 = million_all
    b2 = million_wiki
    # fig=plt.figure(figsize=(14, 6))
    bars1 = axs[1].bar(x - width/2, b1, width, align='center', label='All Families', alpha=0.5)
    bars2 = axs[1].bar(x + width/2, b2, width, align='center', label='Wikipedia Families', alpha=0.5)
    axs[1].set_title('Problem Size: n = 1 million')
    axs[1].set_xticks(np.arange(len(bins)), bins)
    axs[1].yaxis.set_major_formatter(mticker.PercentFormatter(1))
    axs[1].set_xlabel('Average Percentage Improvement Per Year')
    axs[1].set_ylabel('Percentage of Algorithm Families')
    axs[1].legend()

    for a in bars1:
        height = a.get_height()
        axs[1].text(a.get_x() + a.get_width()/2.0, height, f'{height*100:.0f}%', ha='center', va='bottom')

    for a in bars2:
        height = a.get_height()
        axs[1].text(a.get_x() + a.get_width()/2.0, height, f'{height*100:.0f}%', ha='center', va='bottom')

    # plt.savefig("/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/Wellesley/AlgorithmsWiki/Paper/fig7b.pdf")
    # plt.savefig("/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/Wellesley/AlgorithmsWiki/Paper/fig7b.png")

    #Billion figure
    c1 = billion_all
    c2 = billion_wiki
    # fig=plt.figure(figsize=(14, 6))
    bars1 = axs[2].bar(x - width/2, c1, width, align='center', label='All Families', alpha=0.5)
    bars2 = axs[2].bar(x + width/2, c2, width, align='center', label='Wikipedia Families', alpha=0.5)
    axs[2].set_title('Problem Size: n = 1 billion')
    axs[2].set_xticks(np.arange(len(bins)), bins)
    axs[2].yaxis.set_major_formatter(mticker.PercentFormatter(1))
    axs[2].set_xlabel('Average Percentage Improvement Per Year')
    axs[2].set_ylabel('Percentage of Algorithm Families')
    axs[2].legend()

    for a in bars1:
        height = a.get_height()
        axs[2].text(a.get_x() + a.get_width()/2.0, height, f'{height*100:.0f}%', ha='center', va='bottom')

    for a in bars2:
        height = a.get_height()
        axs[2].text(a.get_x() + a.get_width()/2.0, height, f'{height*100:.0f}%', ha='center', va='bottom')

    # plt.savefig("/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/Wellesley/AlgorithmsWiki/Paper/fig7c.pdf")
    # plt.savefig("/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/Wellesley/AlgorithmsWiki/Paper/fig7c.png")

    plt.savefig("/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/Wellesley/AlgorithmsWiki/Paper/fig7.pdf")
    plt.savefig("/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/Wellesley/AlgorithmsWiki/Paper/fig7.png")

def mentions_stat():
    df = pd.read_csv('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/Wellesley/AlgorithmsWiki/wikipedia/merged.csv')
    df = df[['is_optimal', 'Has dedicated page?', 'Part of another page?', 'One of them', 'Family Name']]
    data = df.to_dict(orient='records')
    optimal_page = 0
    optimal_no_page = 0
    optimal_mentioned = 0
    optimal_not_mentioned = 0
    one_of_them = 0
    none_of_them = 0
    total = 0
    optimal = 0
    problems = []
    for algo in data:
        total += 1
        # print(algo)
        if algo['One of them'] == 1:
            one_of_them += 1
            problems.append(algo['Family Name'])
        else:
            none_of_them += 1
        if algo['is_optimal'] == True:
            optimal += 1
            if algo['Has dedicated page?'] == 1:
                optimal_page += 1
            elif algo['Has dedicated page?'] == 0:
                optimal_no_page += 1
            if algo['One of them'] == 1:
                optimal_mentioned += 1
            elif algo['One of them'] == 0:
                optimal_not_mentioned += 1
    fraction_optimal_own_page = optimal_page/(optimal_page + optimal_no_page)
    fraction_optimal_mentioned = optimal_mentioned/(optimal_mentioned + optimal_not_mentioned)
    problems = list(set(problems))
    problems_formatted = {}
    for problem in problems:
        problems_formatted[problem] = 0
    for algo in data:
        if algo['is_optimal'] == True and algo['One of them'] == 1:
            problems_formatted[algo['Family Name']] += 1
    problems_no_opt = 0
    problems_opt = 0
    for value in problems_formatted.values():
        if value > 0:
            problems_opt += 1
        elif value == 0:
            problems_no_opt += 1
    print(problems_formatted)
    print("fraction of wikipedia problems with no optimal algorithm:", problems_no_opt/(problems_opt+problems_no_opt))
    print("fraction of optimal algorithms with a dedicated page:", fraction_optimal_own_page)
    print("fraction of optimal algorithms mentioned or with dedicated page:", fraction_optimal_mentioned)
    print(optimal_page)
    print(optimal_no_page)
    print(optimal_mentioned)
    print(optimal_not_mentioned)
    print(one_of_them)
    print(none_of_them)
    print(one_of_them/(one_of_them+none_of_them))
    print(total)
    print("optimal fraction:", optimal/1040)
    

            # if algo['Part of another page?'] == 1:
            #     optimal_mentioned += 1
            # else if algo['Part of another page?'] == 0:
            #     optimal_not_mentioned += 1
            # if algo['One of them'] == 1:
            # else if algo['One of them'] == 0:

# figure1()
# figure2()
# figure2appendix()
# figure3A()
# figure3B()
# figure4A()
# figure4B()
# figure5()
# figure6()
figure7()
# mentions_stat()
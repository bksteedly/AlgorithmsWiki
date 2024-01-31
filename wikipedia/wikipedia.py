import pandas as pd
import json
from urllib.parse import quote
import urllib.request
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import ks_2samp
from scipy.stats import wasserstein_distance
from scipy.stats import chi2_contingency

sheet1 = "/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/wikipedia/sheet1_wikipedia.csv" # add sheet1 path here

def create_dataset():
#adds formatted_title and reads_url column in csv file
  df = pd.read_csv(sheet1)
  df = df.fillna('')
  titles_list = df['Page title'].tolist()
  formatted_titles_list = []
  reads_url_list = []
  for title in titles_list:
    if title == '':
      formatted_title = ''
      reads_url = ''
      formatted_titles_list.append(formatted_title)
      reads_url_list.append(reads_url)
    else:   
      formatted_title = quote(title.replace(' ', '_'))
      reads_url = f'https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/user/{formatted_title}/monthly/20150701/20230731'
      formatted_titles_list.append(formatted_title)
      reads_url_list.append(reads_url)
  df['formatted_title'] = formatted_titles_list
  df['reads_url'] = reads_url_list
  df.to_csv('sheet1_output.csv', index=False) # save the output file
  
  #scrape the reads data and write everything into a csv file
  list_of_dicts = []
  reads_url_list = df['reads_url'].tolist()
  for reads_url in reads_url_list:
    if reads_url == '': 
      list_of_dicts.append([])
    else:
      with urllib.request.urlopen(reads_url) as url:
        data = url.read().decode('utf-8')
        items_dict = json.loads(data)
        desired_keys = ['article', 'timestamp', 'views']
        items_list = items_dict.get('items', [])
        selected_data = []
        for item in items_list:
          selected_item = {key: item[key] for key in desired_keys if key in item}
          selected_data.append(selected_item)
        list_of_dicts.append(selected_data)
  formatted_list = []
  for list in list_of_dicts:
    if len(list) == 0: # if the list is empty (when the algo has no wikipedia page)
      formatted_list.append({})
    else:
      formatted_dict = {}
      for dict in list:
        formatted_dict['formatted_title'] = dict['article']
        formatted_dict[dict['timestamp']] = dict['views']
      formatted_list.append(formatted_dict)

  df_output = pd.DataFrame(formatted_list)
  df_output = df_output.drop('formatted_title', axis=1)
  df_output['average_monthly_reads'] = df_output.mean(axis=1)
  df_output.to_csv('views.csv', index=False)
  merged_df = pd.merge(df, df_output, left_index=True, right_index=True)
  merged_df.to_csv('sheet1_output_views.csv', index=False)

  df1 = pd.read_csv('sheet1_output.csv')
  df1 = df1.fillna('')
  df2 = pd.read_csv('sheet1_output_views.csv')
  df2 = df2.fillna('')
  # Merge the DataFrames based on the common column
  merged_df = pd.merge(df1, df2, left_index=True, right_index=True)
  # Save the merged DataFrame to a new CSV file
  merged_df.to_csv("merged.csv", index=False)

  
  
def preliminary_analysis():
  merged_dict = pd.read_csv('merged.csv').to_dict(orient='records')
  min_time_complexities = {}

  # Iterate through the list of dictionaries and find min time complexity class for each family
  for entry in merged_dict:
    family_name = entry['Family Name']
    time_complexity_class = entry['Time Complexity Class']
    if family_name not in min_time_complexities:
        min_time_complexities[family_name] = time_complexity_class
    else:
        min_time_complexities[family_name] = min(min_time_complexities[family_name], time_complexity_class)

  # Iterate through the list of dictionaries and add the min_time_complexity_class to each entry
  for entry in merged_dict:
    family_name = entry['Family Name']
    entry['min_time_complexity_class'] = min_time_complexities[family_name]
    if entry['min_time_complexity_class'] == entry['Time Complexity Class']:
        entry['is_optimal'] = True
    else:
        entry['is_optimal'] = False

  df = pd.DataFrame(merged_dict)
  df.to_csv('merged.csv', index=False)

  reads_all = []
  reads_optimal = []
  reads_not_optimal = []
  total_optimal = 0
  wiki_optimal = 0
  total_algos = 0
  for algo in merged_dict:
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
  print('total number of algorithms on wikipedia: ' + str(len(reads_all)))
  print('number of optimal algorithms on wikipedia: ' + str(len(reads_optimal)))
  print('number of non-optimal algorithms on wikipedia: ' + str(len(reads_not_optimal)))
  print('average page reads for all algorithms on wikipedia: ' + str(np.mean(reads_all)))
  print('average page reads for optimal algorithms on wikipedia: ' + str(np.mean(reads_optimal)))
  print('average page reads for nonoptimal algorithms on wikipedia: ' + str(np.mean(reads_not_optimal)))
  print('fraction of optimal algorithms on wikipedia: ' + str(wiki_optimal/total_optimal))
  print('total number of optimal algorithms in Sheet1: ' + str(total_optimal))
  print('total number of algorithms in Sheet1: ' + str(total_algos))

  t_stat, p_value = stats.ttest_ind(reads_optimal, reads_not_optimal)
  alpha = 0.05

  if p_value < alpha:
    print('The p-value of ' + str(p_value) + ' is less than 0.05 so the result is statistically significant.')
  else:
    print('The p-value of ' + str(p_value) + ' is greater than 0.05 so the result is not statistically significant.')

  fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

  sns.histplot(reads_optimal, bins=14, kde=False, stat='percent', color='blue', edgecolor='black', ax=axes[0])
  axes[0].set_title('Number of Views for Wikipedia Pages about Optimal Algos')
  axes[0].set_xlabel('Number of Views')
  axes[0].set_ylabel('Percent')

  sns.histplot(reads_not_optimal, bins=14, kde=False, stat='percent', color='red', edgecolor='black', ax=axes[1])
  axes[1].set_title('Number of Views for Wikipedia Pages about Non-Optimal Algos')
  axes[1].set_xlabel('Number of Views')
  axes[1].set_ylabel('Percent')

  plt.tight_layout()
  plt.show()


def complexity_classes_figure():
  df = pd.read_csv('merged.csv')
  merged_dict = df.to_dict(orient='records')
  wiki_complexity_classes = []
  non_wiki_complexity_classes = []
  for algo in merged_dict:
    if algo['Time Complexity Class'] != '#VALUE!':
      if algo['One of them'] == 1:
        wiki_complexity_classes.append(float(algo['Time Complexity Class']))
      else:
        on_wiki_complexity_classes.append(float(algo['Time Complexity Class']))

  bin_edges = [1, 2, 3, 4, 5, 6, 7, 8]
  bin_labels = ['constant', 'logarithmic', 'linear', 'quasilinear (nlogn)', 'quadratic', 'cubic', 'polynomial (>3)', 'exponential / factorial']

  # Create subplots
  fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

  # Plot the histogram for wiki_complexity_classes
  ax1 = sns.histplot(wiki_complexity_classes, kde=False, bins=7, stat='percent', color='blue', edgecolor='black', ax=axes[0])
  ax1.set_title('Time Complexity Classes for Algos on Wikipedia')
  ax1.set_xlabel('Time Complexity')
  ax1.set_ylabel('Percent')
  ax1.set_xticks(bin_edges)
  ax1.set_xticklabels(bin_labels, rotation=-45, ha='left')

  # Add heights (percentages) on top of bars in the first subplot
  for p in ax1.patches:
    height = p.get_height()
    ax1.annotate(f'{height:.2f}', (p.get_x() + p.get_width() / 2., height), ha='center', va='bottom')

  # Plot the histogram for non_wiki_complexity_classes
  ax2 = sns.histplot(non_wiki_complexity_classes, kde=False, bins=8, stat='percent', color='red', edgecolor='black', ax=axes[1])
  ax2.set_title('Time Complexity Classes for Algos not on Wikipedia')
  ax2.set_xlabel('Time Complexity')
  ax2.set_ylabel('Percent')
  ax2.set_xticks(bin_edges)
  ax2.set_xticklabels(bin_labels, rotation=-45, ha='left')

  # Add heights (percentages) on top of bars in the second subplot
  for p in ax2.patches:
    height = p.get_height()
    ax2.annotate(f'{height:.2f}', (p.get_x() + p.get_width() / 2., height), ha='center', va='bottom')

  plt.tight_layout()
  plt.show()

  # Perform K-S test:
  ks_statistic, p_value = ks_2samp(wiki_complexity_classes, non_wiki_complexity_classes)

  print("KS Statistic:", ks_statistic)
  print("P-value:", p_value)

  alpha = 0.05  # Significance level
  if p_value < alpha:
    print("The two datasets are significantly different (reject the null hypothesis)")
  else:
    print("There is no significant difference between the two datasets (fail to reject the null hypothesis)")


def complexity_classes_dedicated_figure():
  df = pd.read_csv('merged.csv')
  merged_dict = df.to_dict(orient='records')

  wiki_complexity_classes = []
  non_wiki_complexity_classes = []
  for algo in merged_dict:
    if algo['Time Complexity Class'] != '#VALUE!':
      if algo['Has dedicated page?'] == 1:
        wiki_complexity_classes.append(float(algo['Time Complexity Class']))
        if algo['Time Complexity Class'] == 1:
          print(algo)
        else:
          non_wiki_complexity_classes.append(float(algo['Time Complexity Class']))

  bin_edges = [1, 2, 3, 4, 5, 6, 7, 8]
  bin_labels = ['constant', 'logarithmic', 'linear', 'quasilinear (nlogn)', 'quadratic', 'cubic', 'polynomial (>3)', 'exponential / factorial']

  # Create subplots
  fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

  # Plot the histogram for wiki_complexity_classes
  ax1 = sns.histplot(wiki_complexity_classes, kde=False, bins=7, stat='percent', color='blue', edgecolor='black', ax=axes[0])
  ax1.set_title('Time Complexity Classes for Algos with Page on Wikipedia')
  ax1.set_xlabel('Time Complexity')
  ax1.set_ylabel('Percent')
  ax1.set_xticks(bin_edges)
  ax1.set_xticklabels(bin_labels, rotation=-45, ha='left')

  # Add heights (percentages) on top of bars in the first subplot
  for p in ax1.patches:
    height = p.get_height()
    ax1.annotate(f'{height:.2f}', (p.get_x() + p.get_width() / 2., height), ha='center', va='bottom')

  # Plot the histogram for non_wiki_complexity_classes
  ax2 = sns.histplot(non_wiki_complexity_classes, kde=False, bins=8, stat='percent', color='red', edgecolor='black', ax=axes[1])
  ax2.set_title('Time Complexity Classes for Algos without Page on Wikipedia')
  ax2.set_xlabel('Time Complexity')
  ax2.set_ylabel('Percent')
  ax2.set_xticks(bin_edges)
  ax2.set_xticklabels(bin_labels, rotation=-45, ha='left')

  # Add heights (percentages) on top of bars in the second subplot
  for p in ax2.patches:
    height = p.get_height()
    ax2.annotate(f'{height:.2f}', (p.get_x() + p.get_width() / 2., height), ha='center', va='bottom')

  plt.tight_layout()
  plt.show()

  # Perform K-S test:
  ks_statistic, p_value = ks_2samp(wiki_complexity_classes, non_wiki_complexity_classes)

  print("KS Statistic:", ks_statistic)
  print("P-value:", p_value)

  alpha = 0.05  # Significance level
  if p_value < alpha:
    print("The two datasets are significantly different (reject the null hypothesis)")
  else:
    print("There is no significant difference between the two datasets (fail to reject the null hypothesis)")

import pandas
import numpy as np
import matplotlib.pyplot as plt
import random
import math
import copy
import warnings
warnings.filterwarnings("ignore")
import collections

def perc_of_families_improving_per_decade(df,algorithm_families):
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

		print(families_improving_per_decade)

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
	print(cumulative)

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
		
	print("families_improving_per_decade", families_improving_per_decade)
	print("families_improving_per_decade_wiki", families_improving_per_decade_wiki)
	print("cumulative", cumulative)
	print("cumulative_all", cumulative_all)
	print("cumulative_wiki", cumulative_wiki)
	
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

class GraphGenerator:
	def main(self):
		print("Loading dataset...")
		#Import CSV file
		dataframe = pandas.read_csv('merged.csv')
		dataframe['Parallel?'] = dataframe['Parallel?'].str.replace(r'\D', '', regex=True)
		dataframe['Parallel?'] = dataframe['Parallel?'].astype('Int64')
		dataframe['Approximate?'] = dataframe['Approximate?'].str.replace(r'\D', '', regex=True)
		dataframe['Approximate?'] = dataframe['Approximate?'].astype('Int64')
		dataframe = dataframe.loc[(dataframe['Quantum?'] == 0) & (dataframe['Parallel?'] == 0) & (dataframe['Exact algorithm?'] == 1) & (dataframe['Exact Problem Statement?'] == 1) & (dataframe['Randomized?'] == 0) & (dataframe['Approximate?'] == 0) & (dataframe['GPU-based?'] == 0)]
		algorithm_families_all = dataframe['Family Name'].unique()

		family_names_wiki = []
		# iterate through each row in the dataframe and add the family name to a list of family names if one of them is 1
		for index, row in dataframe.iterrows():
			if row['One of them'] == 1:
				family_names_wiki.append(row['Family Name'])
		# convert the list to a set then back to a list to remove duplicates. This is the list of families on wiki
		family_names = list(set(family_names_wiki))
		# iterate through each row in the dataframe and check to see if the family name is in the list of families. If it is, keep it. Otherwise remove. 
		dataframe_wiki = dataframe[dataframe['Family Name'].isin(family_names_wiki)]
		algorithm_families_wiki = dataframe_wiki['Family Name'].unique()

		print("Percentage of Algorithm Families Improved Each Decade ...")
		perc_of_families_improving_per_decade(dataframe,algorithm_families_all)

if __name__ == "__main__":
	generator = GraphGenerator()
	generator.main()

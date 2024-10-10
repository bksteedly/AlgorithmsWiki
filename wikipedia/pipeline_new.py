import pandas
import numpy as np
import matplotlib.pyplot as plt
import random
import math
import copy
import warnings
warnings.filterwarnings("ignore")
import collections

def dist_of_starting_complexities(df,algorithm_families):
	'''
	The mapping for the starting complexities are as follows
	'Exp' - 1
	'Polynomial>3' - 2
	'Cubic' - 3
	'Quadratic' - 4
	'nlogn' - 5
	'Linear' - 6
	'logn' - 7
	'Constant' - 8
	'''
	
	starting_complexities = []
	for name in algorithm_families:
		algorithms = df.loc[df['Family Name'] == name] 
		starting_complexity = algorithms.iloc[0]['Starting Complexity'] 
		starting_complexities.append(starting_complexity)
	print(starting_complexities)
	group_starting_complexities = [0,0,0,0,0,0,0] #Initalize with Dictionary
	for c_class in range(7):
		group_starting_complexities[c_class] = starting_complexities.count(c_class+1)
	classes = ('Exponential or Factorial', 'Polynomial>3', 'Cubic', 'Quadratic', 'nlogn', 'Linear', 'Constant') #dict.keys() # Second dict with printable names. 
	fig=plt.figure(figsize=(14, 6))
	plt.bar(np.arange(len(classes)), group_starting_complexities, align='center', alpha=0.5)
	plt.xticks(np.arange(len(classes)), classes)
	plt.ylabel('Number of Families')
	plt.ylabel('Time Complexity Groups')
	plt.title('Distribution of Algorithms at First Discovery')
	plt.savefig('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/Paper/how_fast/dist_of_starting_complexities.pdf')
	plt.savefig('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/Paper/how_fast/dist_of_starting_complexities.png')

def perc_of_families_improving_per_decade(df,algorithm_families):
	
	families_improving_per_decade = [0,0,0,0,0,0,0,0]
	print("algorithm families:", algorithm_families)
	print("dataframe:", df)
	for name in algorithm_families:
		print("name", name)
		algorithms = df.loc[df['Family Name'] == name]
		print("algorithms", len(algorithms), algorithms)
		algorithms['Time Complexity Improvement?'] = algorithms['Time Complexity Improvement?'].astype(str).str.strip().astype(float)
		time_complexity_improvement_algorithms = algorithms.loc[algorithms['Time Complexity Improvement?']==1]
		print("time_complexity_improvement_algorithms", time_complexity_improvement_algorithms)
		time_complexity_improvement_algorithms_years = time_complexity_improvement_algorithms['Year'].tolist()
		time_complexity_improvement_algorithms_years.sort()
		print("time_complexity_improvement_algorithms_years", time_complexity_improvement_algorithms_years)
		time_complexity_improvement_algorithms_years.pop(0)
		temp_decades = [0,0,0,0,0,0,0,0]
		for q in time_complexity_improvement_algorithms_years:
			#Adjust the publication year to now divide them by 10 and then subtract 194 to bring them to a scale from 0 - 7.
			temp_i = int(math.floor(q / 10.0)) - 194
			#If there is an improvement in a decade, make that decade store 1 for this family. 
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
	s = 0
	for i in group_origin_decades:
		s = s + i
		cumulative.append(s)
	print(cumulative)

	#Find % of families improving in a decade
	for i in range(8):
		cumulative[i] = (families_improving_per_decade[i]/(1.0*cumulative[i]))*100

	decades = ('1940s','1950s','1960s','1970s','1980s','1990s','2000s','2010s')
	fig=plt.figure(figsize=(14, 6))
	plt.bar(np.arange(len(decades)), cumulative, align='center', alpha=0.5)
	plt.xticks(np.arange(len(decades)), decades)
	plt.ylabel('Percentage of Families')
	plt.title('Percentage of Algorithm Families Improved Each Decade')
	plt.savefig('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/Paper/how_fast/perc_of_families_improving_per_decade.pdf')
	plt.savefig('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/Paper/how_fast/perc_of_families_improving_per_decade.png')
	plt.show()

def dist_of_family_origin_years(df,algorithm_families):
	
	origin_years = []
	origin_years_floor = []
	for name in algorithm_families:
		algorithms = df.loc[df['Family Name'] == name]
		origin_years.append(algorithms['Year'].min())
		origin_years_floor.append(int(math.floor(algorithms['Year'].min() / 10.0)) * 10)
	group_origin_decades = [0,0,0,0,0,0,0,0] #You would just have use a dataframe.
	for decade in range(8): 
		group_origin_decades[decade] = origin_years_floor.count(1940+decade*10)
	decades = ('1940s','1950s','1960s','1970s','1980s','1990s','2000s','2010s')
	fig=plt.figure(figsize=(14, 6))
	plt.bar(np.arange(len(decades)), group_origin_decades, align='center', alpha=0.5)
	plt.xticks(np.arange(len(decades)), decades)
	plt.ylabel('Number of Families')
	plt.ylabel('Decades')
	plt.title('Number of New Algorithm Families')
	plt.savefig('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/Paper/how_fast/dist_of_family_origin_years.pdf')
	plt.savefig('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/Paper/how_fast/dist_of_family_origin_years.png')


def step_chart_family(df,algorithm_families,problem_size): #Add a parameter to pass problem size, #Check for quantum and parallel
	
	for name in algorithm_families:
		algorithms = df.loc[df['Family Name'] == name]
		time_complexity_improvement_algorithms = algorithms.loc[algorithms['Time Complexity Improvement?']==1]
		algorithm_names = algorithms['Algorithm Name'].tolist()
		x_scatter = algorithms['Year'].tolist() #Xaxis has the years of publication
		y_scatter = np.log2(algorithms[problem_size]).tolist() #Yaxis has the log of asymptotic performance
		print(y_scatter)
		x_step = time_complexity_improvement_algorithms['Year'].tolist()
		y_step = np.log2(time_complexity_improvement_algorithms[problem_size]).tolist()
		
		fig, ax = plt.subplots(figsize=(18, 8))
		c = 0
		for x,y in zip(x_scatter,y_scatter):
			ax.scatter(x, y, label=algorithm_names[c],alpha=0.8, edgecolors='none')
			c = c + 1
		#Some box adjustments to get the labels at the bottom.
		box = ax.get_position()
		ax.set_position([box.x0, box.y0 + box.height * 0.1,
		                 box.width, box.height * 0.9])
		#Add the legend for all algorithms.
		ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
	  		fancybox=True, shadow=True, ncol=5)
		#Adjust x ticks to have a gap of 5 years to reduce clutter.
		plt.xticks(np.arange(1940,2020,5))
		#Add the algorithm family name as the title.
		plt.title(name)

		#This specific adjustment is to add an improvement point at 2018 in the step charts. This is only for representative purposes. 
		x_step.append(2018)
		y_step.append(y_step[len(y_step)-1])

		#Generate the step chart in the same plot.
		plt.step(x_step,y_step,where='post')
		plt.savefig(name+".png")

def dist_of_improvement_rates(df,algorithm_families,problem_size): #Define size parameter
	
	improvement_rate_percentages = []
	improvement_rate_percentages_classes = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]  #Within this function, use the default function.
	for name in algorithm_families:
		algorithms = df.loc[df['Family Name'] == name] #Use another dataframe on the family level - record the improvement %. Use it separately and call it as a parameter.
		time_complexity_improvement_algorithms = algorithms.loc[algorithms['Time Complexity Improvement?']==1]
		improvement_val = time_complexity_improvement_algorithms[problem_size].max()/time_complexity_improvement_algorithms[problem_size].min()
		year_difference = 2018-time_complexity_improvement_algorithms['Year'].min()
		inv_year_difference = 1/(year_difference*1.0)
		improvement_rate_percentage = (math.pow(improvement_val,inv_year_difference) - 1)*100
		improvement_rate_percentages.append(improvement_rate_percentage)
		improvement_rate_percentages_classes[min((improvement_rate_percentage/5),14)] = improvement_rate_percentages_classes[min((improvement_rate_percentage/5),14)] + 1

	x1 = ['0-5%', '5-10%', '10-15%', '15-20%', '20-25%', '25-30%','30-35%','35-40%','40-45%','45-50%','50-55%','55-60%','60-65%','65-70%','1000%']
	x2 = ['0-5%', '5-10%', '10-15%', '15-20%', '20-25%', '25-30%','30-35%','35-40%','40-45%','45-50%','50-55%','55-60%','60-65%','65-70%','1000%']
	y1 = improvement_rate_percentages_classes
	y2 = 15,6,14,21,12,20,7,5,3,1,0,0,0,0,0
	fig=plt.figure(figsize=(14, 6))
	#plt.subplot(2, 1, 1)
	plt.plot(x1, y1, 'o-')
	plt.title('Percentage Improvement Per Year')
	plt.ylabel('Number of Families')
	#plt.subplot(2, 1, 2)
	#plt.plot(x2, y2, '.-')
	#plt.xlabel('Percentage Ranges')
	#plt.ylabel('Number of Families')
	plt.show()

def combined_step_chart_family(df,algorithm_families,problem_size):
	fig, ax = plt.subplots(figsize=(18, 8))
	
	for name in algorithm_families:
		algorithms = df.loc[df['Family Name'] == name]
		time_complexity_improvement_algorithms = algorithms.loc[algorithms['Time Complexity Improvement?']==1]
		algorithm_names = algorithms['Algorithm Name'].tolist()
		x_step = time_complexity_improvement_algorithms['Year'].tolist()
		y_step = np.log2(time_complexity_improvement_algorithms[problem_size]).tolist()
		x_step.sort()
		y_step.sort()
		#This specific adjustment is to add an improvement point at 2018 in the step charts. This is only for representative purposes. 
		x_step.append(2018)
		y_step.append(y_step[len(y_step)-1])

		#Generate the step chart in the same plot.
		plt.step(x_step,y_step,where='post', label=name)
	
	#Some box adjustments to get the labels at the bottom.
	box = ax.get_position()
	ax.set_position([box.x0, box.y0 + box.height * 0.1,
	                 box.width, box.height * 0.9])
	#Add the legend for all algorithms.
	ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
  		fancybox=True, shadow=True, ncol=5)
	#Adjust x ticks to have a gap of 5 years to reduce clutter.
	plt.xticks(np.arange(1940,2020,5))
	#Add the algorithm family name as the title.
	plt.title("Combined Step Chart")
	plt.show()
	
	
def transition_probabilities(df):
	transition_df = df.loc[(df['Time Complexity Improvement?']==1)]
	transition_df = transition_df[['Family Name','Algorithm Name','Year','Transition Class']]
	transition_df = transition_df[transition_df['Transition Class'].str.contains("->")]
	transitions = transition_df['Transition Class'].tolist()
	
	unique_classes = []
	for t in transitions:
		unique_classes.append(int(t.split("->")[0]))
		unique_classes.append(int(t.split("->")[1]))
	unique_classes = list(set(unique_classes))
	unique_classes_range = max(unique_classes)-min(unique_classes)+1


	algorithm_families = transition_df['Family Name'].unique()
	families_per_class_per_year = []
	transitions_per_year = []

	
	iterator = 1
	while(iterator < unique_classes_range):
		iterator2 = iterator + 1
		while (iterator2 <= unique_classes_range):
			transition_str = str(iterator)+"->"+str(iterator2)
			temp = []
			temp.append(transition_str)
			for col in range(79):
				temp.append(0)
			transitions_per_year.append(temp)
			iterator2 = iterator2 + 1
		
		iterator = iterator + 1

	for row in range(unique_classes_range):
		temp = []
		for col in range(79):
			temp.append(0)
		families_per_class_per_year.append(temp)
		
	for name in algorithm_families:
		algorithms = df.loc[df['Family Name'] == name]
		start_year = algorithms['Year'].min()
		starting_class = int(algorithms.iloc[0]['Starting Complexity'])


		algorithms = algorithms.loc[(algorithms['Time Complexity Improvement?']==1)]
		algorithms = algorithms[algorithms['Transition Class'].str.contains("->")]

		
		transition_class_for_family = []
		for row in range(unique_classes_range):
			temp = []
			for col in range(79):
				temp.append(0)
			transition_class_for_family.append(temp)

		transition_dictionary = list(zip(algorithms['Year'],algorithms['Transition Class']))


		print (transition_dictionary)
		
		transition_class_for_family[int(starting_class)-1][int(start_year)-1940] = 1
		checkpoint_year = start_year
		ending_transition = 0
		current_transition = ""
		for keyiter in transition_dictionary:


			for i in range(len(transitions_per_year)):
				
				if transitions_per_year[i][0] == keyiter[1]:
					transitions_per_year[i][int(keyiter[0])-1940+1] = transitions_per_year[i][int(keyiter[0])-1940+1] + 1


			current_transition = keyiter[1]
			current_transition = current_transition.split('->')
			for updater in range(checkpoint_year,int(keyiter[0])):
				transition_class_for_family[int(current_transition[0])-1][updater-1940] = 1
			checkpoint_year = int(keyiter[0])
			ending_transition = int(current_transition[1])-1

		for updater in range(checkpoint_year,2019):
			transition_class_for_family[int(current_transition[1])-1][updater-1940] = 1


		for row in range(unique_classes_range):
			for col in range(79):
				families_per_class_per_year[row][col] = families_per_class_per_year[row][col] + transition_class_for_family[row][col]
		
		#print (families_per_class_per_year)
	print (families_per_class_per_year)
	print (transitions_per_year)
	for i in range(len(families_per_class_per_year)):
		for j in range(len(transitions_per_year)):
			if int(transitions_per_year[j][0].split('->')[0])-1 == i:
				for k in range(79):
					if families_per_class_per_year[i][k]!=0:
						transitions_per_year[j][k+1] = transitions_per_year[j][k+1]/(1.0*families_per_class_per_year[i][k])

	#print (transitions_per_year)


def serial_correlation(algorithm_families):
	
	for name in algorithm_families:
		algorithms = df.loc[df['Family Name'] == name]
		time_complexity_improvement_algorithms = algorithms.loc[algorithms['Time Complexity Improvement?']==1]
		years = time_complexity_improvement_algorithms['Year'].tolist()
		
		time_series_family = []
		for b in range(1940,2019):
			if b in years:
				#If there is a complexity improvement in this year, append the number of improvements. This will be used to randomly permute later.
				time_series_family.append(years.count(b))
				#If there is a complexity improvement in this year, append the number of improvements.
				time_series.append(years.count(b))
				#If there is a complexity improvement in this year, append the number of improvements but for appending these time series remove the first and last.
				if b!=1940 and b!=2018:
					time_series_corrected.append(years.count(b))

			else:
				#If not improvement, append 0. This will be used to randomly permute later.
				time_series_family.append(0)
				#If not improvement, append 0.
				time_series.append(0)
				if b!=1940 and b!=2018:
					#If not improvement, append 0.
					time_series_corrected.append(0)

		Random_family_series.append(time_series_family)
		time_series_family_lag = []
		time_series_family_lag.append('N/A')
		rand2 = []
		rand2.append('N/A')
		rand1 = np.random.permutation(time_series_family)


		for f in range(len(time_series_family)-1):
			time_series_family_lag.append(time_series_family[f])
			rand2.append(rand1[f])

		for j in range(len(time_series_family)):
			final_time_series.append(time_series_family[j])
			final_time_series_lag.append(time_series_family_lag[j])
			random_time_series.append(rand1[j])
			random_time_series_lag.append(rand2[j])


		random_correlations = []
		for k in range(1000):
			random_time_series_iter = []
			random_time_series_lag_iter = []
			for m in Random_family_series:
				temp_m = np.random.permutation(m)
				for n in temp_m:
					random_time_series_iter.append(n)
				random_time_series_lag_iter.append('N/A')
				for n in range(len(m)-1):
					random_time_series_lag_iter.append(m[n])

			df2 = pandas.DataFrame({'Value': random_time_series_iter, 'Value.L1': random_time_series_lag_iter})
			df2 = df2.replace('N/A',np.NaN)
			random_correlations.append(df2.corr().iloc[0][1])

		#Print random correlations
		#print (random_correlations)
		fig=plt.figure(figsize=(14, 6))
		plt.hist(random_correlations)
		plt.vlines(0.1635,0,30,linestyles='dashed')
		plt.show()


def constants_scatter_plot():
	pass

class GraphGenerator:
	def main(self):
		print("Loading dataset...")
		#Import CSV file
		dataframe = pandas.read_csv('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/Wellesley/AlgorithmsWiki/wikipedia/merged.csv')
		dataframe = dataframe.drop(dataframe[dataframe['One of them'] == 0].index)
		#Convert datatype
		dataframe['Parallel?'] = dataframe['Parallel?'].astype(str).str.replace(r'[^0-9.]', '', regex=True).astype(float)
		dataframe['Approximate?'] = dataframe['Approximate?'].astype(str).str.replace(r'[^0-9.]', '', regex=True).astype(float)
		dataframe['Quantum?'] = dataframe['Quantum?'].astype(str).str.strip().astype(float)
		dataframe['Exact Problem Statement?'] = dataframe['Exact Problem Statement?'].astype(str).str.strip().astype(float)
		dataframe['Exact algorithm?'] = dataframe['Exact algorithm?'].astype(str).str.strip().astype(float)
		dataframe['Randomized?'] = dataframe['Randomized?'].astype(str).str.strip().astype(float)
		dataframe['GPU-based?'] = dataframe['GPU-based?'].astype(str).str.strip().astype(float)
		dataframe = dataframe.loc[(dataframe['Quantum?'] == 0) & (dataframe['Parallel?'] == 0) & (dataframe['Exact Problem Statement?'] == 1) & (dataframe['Exact algorithm?'] == 1) & (dataframe['Randomized?'] == 0) & (dataframe['Approximate?'] == 0) & (dataframe['GPU-based?'] == 0)]
        #algorithm_families = df['Family Name'].unique()
		algorithm_families = dataframe['Family Name'].unique()

		# print("Generating Distribution of Original Complexities ...")
		# dist_of_starting_complexities(dataframe,algorithm_families)

		# print("Ditribution of Originating Years ...")
		# dist_of_family_origin_years(dataframe,algorithm_families)

		print("Percentage of Algorithm Families Improved Each Decade ...")
		perc_of_families_improving_per_decade(dataframe,algorithm_families)

		# print("Step charts for the families for n = 1 thousand ...")
		# step_chart_family(dataframe,algorithm_families, 'n = 1000 scale')
		# print("Step charts for the families for n = 1 million ...")
		# step_chart_family(dataframe,algorithm_families, 'n = 10^6 scale')
		# print("Step charts for the families for n = 1 billion ...")
		# step_chart_family(dataframe,algorithm_families, 'n = 10^9 scale')
		
		# print("Average Improvement Rate per Year for n = 1 thousand ...")
		# dist_of_improvement_rates(dataframe,algorithm_families, 'n = 1000 scale')
		# print("Average Improvement Rate per Year for n = 1 million ...")
		# dist_of_improvement_rates(dataframe,algorithm_families, 'n = 10^6 scale')
		# print("Average Improvement Rate per Year for n = 1 billion ...")
		# dist_of_improvement_rates(dataframe,algorithm_families, 'n = 10^9 scale')
		
		# print("Combined step improvement charts for n = 1 thousand ...")
		# combined_step_chart_family(dataframe,algorithm_families,'n = 1000 scale')
		# print("Combined step improvement charts for n = 1 million ...")
		# combined_step_chart_family(dataframe,algorithm_families,'n = 10^6 scale')
		# print("Combined step improvement charts for n = 1 billion ...")
		# combined_step_chart_family(dataframe,algorithm_families,'n = 10^9 scale')
		
		# print("Transition probabilites ...")
		# transition_probabilities(dataframe)
		

if __name__ == "__main__":
	generator = GraphGenerator()
	generator.main()

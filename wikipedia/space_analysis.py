import math
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
import helpers
from matplotlib import cm as CM
import seaborn as sns
from tabulate import tabulate
from scipy import stats

def no_tradeoff_necessary(family_name, variation, data):
    """
    Returns list of algorithm names if there are algorithms (among the algorithms that we have analyzed the space)
        for a problem variation that are both the fastest and most space efficient.
    Otherwise, returns []

    Prints this list as well.
    """
    df = data
    df = df.replace(np.nan, '', regex=True)
    df = df[(df['Time Complexity Class'] != '#VALUE!') &
            (df['Space Complexity Class'] != '#VALUE!') &
            (df["Looked at?"] != 0.001)]
    algorithms = df.loc[df['Family Name'] == family_name]
    if variation != "By Family":
        algorithms = algorithms.loc[algorithms['Variation'] == variation]
    try:
        algorithms[algorithms['Param: Space Class'].str.contains(':')]
    except:
        print(algorithms['Param: Space Class'])
        print(algorithms["Algorithm Name"])
    algorithms = algorithms[algorithms['Param: Space Class'].str.contains(':')].sort_values('Year')
    
    if algorithms.empty:
        # print('No data found for family name: ' +
        #       family_name + ' and variation: ' + variation)
        return "No data"


    best_time = None
    best_time_algs = []
    best_space = None
    best_space_algs = []
    algs = []

    for index, row in algorithms.iterrows():
        item = {}
        item['year'] = int(row['Year'])
        try:
            item['space'] = float(row['Space Complexity Class']) - 1
        except:
            print("SPACE ERROR:", family_name, variation, row['Space Complexity Class'])
            continue
        try:
            item['time'] = float(row['Time Complexity Class']) - 1 #math.ceil(float(row['Time Complexity Class']) - 1)
        except:
            print("TIME ERROR:", family_name, variation, row['Algorithm Name'], row['Time Complexity Class'])
            continue
        item['name'] = row['Algorithm Name']

        algs.append(item['name'])

        if best_space is None:
            best_space_algs = [item['name']]
            best_space = item['space']
        elif item['space'] < best_space:
            best_space_algs = [item['name']]
            best_space = item['space']
        elif item['space'] == best_space:
            best_space_algs.append(item['name'])

        if best_time is None:
            best_time_algs = [item['name']]
            best_time = item['time']
        elif item['time'] < best_time:
            best_time_algs = [item['name']]
            best_time = item['time']
        elif item['time'] == best_time:
            best_time_algs.append(item['name'])

    best = []
    for alg in algs:
        if alg in best_time_algs and alg in best_space_algs:
            best.append(alg)

    return best

def fraction_of_optimality(by_family_or_variation, data=None):
    """
    Determine the fraction of variants that have an algorithm that is both
    faster and more space efficient (asymptotically) than the other algorithms
    """
    if data is None:
        data = pd.read_csv("Analysis/data.csv")
    total = 0
    has_optimal = 0
    families = helpers.get_families(data)
    for family in families:
        if by_family_or_variation == "Variation":
            variations = helpers.get_variations(family)
            for variation in variations:
                # total += 1
                optimal_algs = no_tradeoff_necessary(family, variation, data)
                if type(optimal_algs) != str:
                    total += 1
                    if len(optimal_algs) > 0:
                        has_optimal += 1
                        # print(family, variation, optimal_algs)
                    else:
                        # print(family, variation)
                        continue
        else:
            optimal_algs = no_tradeoff_necessary(family, "By Family", data)
            if type(optimal_algs) != str:
                total += 1
                if len(optimal_algs) > 0:
                    has_optimal += 1
                    # print(family, variation, optimal_algs)
                else:
                    # print(family, variation)
                    continue

    return (total, has_optimal, has_optimal/total)

def get_space_improvements_by_year(family_name, variation, rounded_up):
    df = pd.read_csv('Analysis/data.csv')
    df = df.replace(np.nan, '', regex=True)
    algorithms = df.loc[df['Family Name'] == family_name]
    if variation != "by family":
        algorithms = algorithms.loc[algorithms['Variation'] == variation]

    algorithms = algorithms[algorithms['Param: Space Class'].str.contains(':')].sort_values('Year')
    
    if algorithms.empty:
        print('No space data found for family name: ' +
              family_name + ' and variation: ' + variation)
        return []


    # Get the algorithms that improve the space bounds
    improvements = []
    best_space = None
    algorithms = algorithms.sort_values('Year')
    for index, row in algorithms.iterrows():
        item = {}
        item['year'] = int(row['Year'])
        if rounded_up:
            item['space'] = math.ceil(float(row['Space Complexity Class']) - 1)
        else:
            item['space'] = float(row['Space Complexity Class']) - 1
        item['name'] = row['Algorithm Name']

        # See if this alg improves the space bound
        if best_space is None:
            best_space = item['space']
        elif item['space'] < best_space:
            best_space = item['space']
            improvements.append(item['year'])

    return improvements

def get_time_improvements_by_year(family_name, variation, rounded_up):
    df = pd.read_csv('Analysis/data.csv')
    df = df.replace(np.nan, '', regex=True)
    algorithms = df.loc[df['Family Name'] == family_name]
    if variation != "by family":
        algorithms = algorithms.loc[algorithms['Variation'] == variation]

    algorithms = algorithms[algorithms['Time Complexity Class']!=''].sort_values('Year')
    
    if algorithms.empty:
        print('No time data found for family name: ' +
              family_name + ' and variation: ' + variation)
        return []


    # Get the algorithms that improve the time bounds
    improvements = []
    best_time = None
    algorithms = algorithms.sort_values('Year')
    for index, row in algorithms.iterrows():
        item = {}
        item['year'] = int(row['Year'])
        if rounded_up:
            item['time'] = math.ceil(float(row['Time Complexity Class']) - 1)
        else:
            item['time'] = float(row['Time Complexity Class']) - 1
        item['name'] = row['Algorithm Name']

        # See if this alg improves the time bound
        if best_time is None:
            best_time = item['time']
        elif item['time'] < best_time:
                best_time = item['time']
                improvements.append(item['year'])

    return improvements

def get_time_improvements_by_type(family_name, variation, rounded_up):
    df = pd.read_csv('Analysis/data.csv')
    df = df.replace(np.nan, '', regex=True)
    algorithms = df.loc[df['Family Name'] == family_name]
    if variation != "by family":
        algorithms = algorithms.loc[algorithms['Variation'] == variation]
    
    algorithms = algorithms[algorithms['Time Complexity Class']!=''].sort_values('Year')

    if algorithms.empty:
        print('No time data found for family name: ' +
              family_name + ' and variation: ' + variation)
        return [], []


    # Get the algorithms that improve the time bounds
    improvements = [] # elements of the type [a,b] where the improvements improve from runtime a to runtime b
    names = []
    best_time = None
    algorithms = algorithms.sort_values('Year')
    for index, row in algorithms.iterrows():
        item = {}
        item['year'] = int(row['Year'])
        if rounded_up:
            item['time'] = math.ceil(float(row['Time Complexity Class']) - 1)
        else:
            item['time'] = float(row['Time Complexity Class'] - 1)
        item['name'] = row['Algorithm Name']

        # See if this alg improves the time bound
        if best_time is None:
            best_time = item['time']
            names.append(item['name'])
        elif item['time'] < best_time:
            improvements.append([best_time, item['time']])
            names.append(item['name'])
            best_time = item['time']

    return improvements, names

def get_space_improvements_by_type(family_name, variation, rounded_up):
    df = pd.read_csv('Analysis/data.csv')
    df = df.replace(np.nan, '', regex=True)
    algorithms = df.loc[df['Family Name'] == family_name]
    if variation != "by family":
        algorithms = algorithms.loc[algorithms['Variation'] == variation]

    algorithms = algorithms[algorithms['Param: Space Class'].str.contains(':')].sort_values('Year')
    
    if algorithms.empty:
        print('No space data found for family name: ' +
              family_name + ' and variation: ' + variation)
        return []


    # Get the algorithms that improve the space bounds
    improvements = [] # elements of the type [a,b] where the improvements improve from runtime a to runtime b
    names = []
    best_space = None
    algorithms = algorithms.sort_values('Year')
    for index, row in algorithms.iterrows():
        item = {}
        item['year'] = int(row['Year'])
        if rounded_up:
            item['space'] = math.ceil(float(row['Space Complexity Class']) - 1)
        else:
            item['space'] = float(row['Space Complexity Class']) - 1
        item['name'] = row['Algorithm Name']

        # See if this alg improves the space bound
        if best_space is None:
            best_space = item['space']
            names.append(item['name'])
        elif item['space'] < best_space:
            improvements.append([best_space, item['space']])
            best_space = item['space']
            names.append(item['name'])

    return improvements, names

def get_time_improvements_first_to_best(family_name, variation, rounded_up):
    df = pd.read_csv('Analysis/data.csv')
    df = df.replace(np.nan, '', regex=True)
    algorithms = df.loc[df['Family Name'] == family_name]
    if variation != "by family":
        algorithms = algorithms.loc[algorithms['Variation'] == variation]

    algorithms = algorithms[algorithms['Time Complexity Class']!=''].sort_values('Year')
    
    if algorithms.empty:
        print('No time data found for family name: ' +
              family_name + ' and variation: ' + variation)
        return False


    # Get the algorithms that improve the time bounds
    improvements = [] # elements of the type [a,b] where the improvements improve from runtime a to runtime b
    best_time = None
    algorithms = algorithms.sort_values('Year')
    for index, row in algorithms.iterrows():
        item = {}
        item['year'] = int(row['Year'])
        if rounded_up:
            item['time'] = math.ceil(float(row['Time Complexity Class']) - 1)
        else:
            item['time'] = float(row['Time Complexity Class']) - 1
        item['name'] = row['Algorithm Name']

        # See if this alg improves the time bound
        if best_time is None:
            first_time = (item['time'], item['name'])
            best_time = (item['time'], item['name'])
        elif item['time'] < best_time[0]:
            best_time = (item['time'], item['name'])
        
    improvements = [[first_time[0], best_time[0]]], [first_time[1], best_time[1]]
    return improvements

def get_space_improvements_first_to_best(family_name, variation, rounded_up):
    df = pd.read_csv('Analysis/data.csv')
    df = df.replace(np.nan, '', regex=True)
    algorithms = df.loc[df['Family Name'] == family_name]
    if variation != "by family":
        algorithms = algorithms.loc[algorithms['Variation'] == variation]

    algorithms = algorithms[algorithms['Param: Space Class'].str.contains(':')].sort_values('Year')
    
    if algorithms.empty:
        print('No space data found for family name: ' +
              family_name + ' and variation: ' + variation)
        return False

    # Get the algorithms that improve the space bounds
    improvements = [] # elements of the type [a,b] where the a is the first space and b is the best space for the problem
    best_space = "unassigned"
    first_space = "unassigned"
    algorithms = algorithms.sort_values('Year')
    for index, row in algorithms.iterrows():
        item = {}
        item['year'] = int(row['Year'])
        if rounded_up:
            item['space'] = math.ceil(float(row['Space Complexity Class']) - 1)
        else:
            item['space'] = float(row['Space Complexity Class']) - 1
        item['name'] = row['Algorithm Name']

        # See if this alg improves the space bound
        if best_space == "unassigned":
            first_space = (item['space'], item['name'])
            best_space = (item['space'], item['name'])
        elif item['space'] < best_space[0]:
            best_space = (item['space'], item['name'])

    improvements = [[first_space[0], best_space[0]]], [first_space[1], best_space[1]]
    return improvements

def hist_improvements(number_or_year, time_or_space, by_family_or_variation, include_title):
    """
    number_or_year: "Number" or "Year"
    time_or_space: "Time" or "Space"
    by_family_or_variation: "Family" or "Variation"
    """
    by_family_or_variation = by_family_or_variation.lower()

    fams = helpers.get_families()
    improvements = []
    save_dest = "Analysis/Plots/Histograms/"
    for fam in fams:
        if by_family_or_variation == "variation":
            vars = helpers.get_variations(fam)
        elif by_family_or_variation == "family":
            vars = ["by family"]
        for var in vars:
            if number_or_year == "Year":
                if time_or_space == "Time":
                    res = get_time_improvements_by_year(fam, var, False)
                elif time_or_space == "Space":
                    res = get_space_improvements_by_year(fam, var, False)
                improvements.extend(res)
            elif number_or_year == "Number":
                if time_or_space == "Time":
                    res = get_time_improvements_by_type(fam, var, False)[0]
                elif time_or_space == "Space":
                    res = get_space_improvements_by_type(fam, var, False)[0]
                improvements.append(len(res))

    if number_or_year == "Year":
        plot_title = f"Decades {time_or_space} Improvements (by {by_family_or_variation})"
        bins = range(1940, 2030, 10)
        sns.set_theme()
        counts, bins, patches = plt.hist(improvements, bins=bins)

        # print(f"\n{plot_title}")
        # for bar, b0, b1 in zip(counts, bins[:-1], bins[1:]):
        #     print(f'{b0:3d} - {b1:3d}: {bar:4.0f}')

        plt.ylabel(f"Number of {time_or_space} Improvements")
        plt.xlabel("Year")
        if include_title:
            plt.title(f"Number of {time_or_space} Improvements per Decade")

    elif number_or_year == "Number":
        plot_title = f"Number of {time_or_space} Improvements (by {by_family_or_variation})"
        bins = range(0,max(improvements) + 1,1)
        labels, counts = np.unique(improvements, return_counts=True)
        sns.set_theme()
        ax = plt.bar(labels, counts, align='center')
        plt.gca().set_xticks(labels)

        print(f"\n{plot_title}")
        for container in ax:
            bar_x = int(container.get_x() + container.get_width() / 2)
            bar_y = container.get_height()
            print(f'{bar_x:3d}: {bar_y:4.0f}')
            
        plt.ylabel(f"Number of Problems")
        plt.xlabel(f"Number of {time_or_space} Improvements")
        if include_title:
            plt.title(f"Number of Problems With a Given Number\nof {time_or_space} Improvements")
        xint = range(0, math.ceil(max(improvements))+1)
        plt.xticks(xint)

    plt.savefig(save_dest + plot_title + ".png", dpi=300, bbox_inches="tight")
    plt.clf()
    plt.close("all")
    return

def heat_improvements_by_type(time_or_space, by_family_or_variation, include_title):
    """
    Create a heatmap showing algorithms that improve either the time or space complexity
    for a problem. The y-axis is the complexity before the improvement, x-axis is after.
    
    Args:
        time_or_space: "Time" or "Space" depending on if you want to see improvements in time or space
        by_family_or_variation: "Family" or "Variation" depending on if you want the problems
            to be specified by family (less specific) or by variation (more specific)
    """

    save_dest = 'Analysis/Plots/Heatmaps/'
    title = time_or_space + " Improvements Heatmap (by " + by_family_or_variation +")"

    fams = helpers.get_families()
    df = pd.DataFrame(columns=['Pre-Improvement', 'Post-Improvement'])

    # Get all the improvements from each family/variation
    for fam in fams:
        if by_family_or_variation == "Variation":
            vars = helpers.get_variations(fam)
        elif by_family_or_variation == "Family":
            vars = ["by family"]

        for var in vars:
            if time_or_space == "Space":
                improvements = get_space_improvements_by_type(fam, var, True)[0]
            elif time_or_space == "Time":
                improvements = get_time_improvements_by_type(fam, var, True)[0]
            if not improvements:
                continue
            var_df = pd.DataFrame(improvements, columns=['Pre-Improvement', 'Post-Improvement'])
            df = pd.concat([df, var_df], ignore_index=True)
    
    # Create df cross tabulation for the heatmap
    df2 = pd.crosstab(df['Pre-Improvement'], df['Post-Improvement'])
    for i in range(8):
        if i not in df2.index:
            df2.loc[i] = pd.Series(0, index=df2.columns)
    for i in range(8):
        if i not in df2.columns:
            df2[i] = pd.Series(0, index=df2.index)
    df2 = df2.sort_index(axis=0, ascending=False)
    df2 = df2.sort_index(axis=1)
    # my_labels = ['constant', 'logn', 'linear', 'nlogn', 'quadratic', 'cubic', 'poly > cubic', 'exponential']
    my_labels = ['Constant', 'Logarithmic', 'Linear', 'n log n', 'Quadratic', 'Cubic', 'Poly (> Cubic)', 'Exponential']
    my_labels_dict = {i: my_labels[i] for i in range(len(my_labels))}
    df2 = df2.rename(index=my_labels_dict, columns=my_labels_dict)
    df2 = df2.replace(0, np.nan)

    # Create the plot
    sns.set_theme()
    ax = sns.heatmap(df2, annot=True, cmap='Reds', linewidth=0.3, vmin=0, linecolor='gray', cbar=False)
    plt.box(on=None)
    complexity_label = f" {time_or_space} Complexity"
    if time_or_space == "Space":
        complexity_label = f"\n{complexity_label[1:]}"
        complexity_label += " (Auxiliary)"
    plt.xlabel(f"Post-Improvement{complexity_label}")
    plt.ylabel(f"Pre-Improvement{complexity_label}")
    plt.tick_params(axis='x', colors='black', labelsize=8)
    plt.tick_params(axis='y', colors='black', labelsize=8)
    ax.xaxis.tick_top()
    ax.xaxis.set_label_position('top') 
    ax.invert_xaxis()
    plt.setp(ax.get_xticklabels(), rotation=45, ha="left",
         rotation_mode="anchor") # if you want x-axis label on top, change to ha="left"
    plt.tight_layout()
    
    # Save the plot
    try:
        plt.savefig(save_dest + title + ".png", dpi=300, bbox_inches='tight')
    except Exception as e:
        print(e)
        print("Failed")

    # Close/clear the plot
    plt.clf()
    plt.close("all")
    return

def heat_improvements_first_to_best(time_or_space, by_family_or_variation, include_title):
    """
    Create a heatmap showing how much of an improvement we see in a problem overall.
    The y-axis is the complexity of the first algorithm, x-axis is for the best algorithm.
    
    Args:
        time_or_space: "Time" or "Space" depending on if you want to see improvements in time or space
        by_family_or_variation: "Family" or "Variation" depending on if you want the problems
            to be specified by family (less specific) or by variation (more specific)
    """
    save_dest = 'Analysis/Plots/Heatmaps/'
    title = time_or_space + " Improvements from First to Best"

    fams = helpers.get_families()
    df = pd.DataFrame(columns=['Pre-Improvement', 'Post-Improvement'])

    # Get all the improvements from each family/variation
    for fam in fams:
        if by_family_or_variation == "Variation":
            vars = helpers.get_variations(fam)
        elif by_family_or_variation == "Family":
            vars = ["by family"]

        for var in vars:
            if time_or_space == "Space":
                improvements = get_space_improvements_first_to_best(fam, var, True)[0]
            elif time_or_space == "Time":
                improvements = get_time_improvements_first_to_best(fam, var, True)[0]
            if not improvements:
                continue
            var_df = pd.DataFrame(improvements, columns=['Pre-Improvement', 'Post-Improvement'])
            df = pd.concat([df, var_df], ignore_index=True)
    
    # Create df cross tabulation for the heatmap
    df2 = pd.crosstab(df['Pre-Improvement'], df['Post-Improvement'])
    for i in range(8):
        if i not in df2.index:
            df2.loc[i] = pd.Series(0, index=df2.columns)
    for i in range(8):
        if i not in df2.columns:
            df2[i] = pd.Series(0, index=df2.index)
    df2 = df2.sort_index(axis=0, ascending=False)
    df2 = df2.sort_index(axis=1)
    # my_labels = ['constant', 'logn', 'linear', 'nlogn', 'quadratic', 'cubic', 'poly > cubic', 'exponential']
    my_labels = ['Constant', 'Logarithmic', 'Linear', 'n log n', 'Quadratic', 'Cubic', 'Poly (> Cubic)', 'Exponential']
    my_labels_dict = {i: my_labels[i] for i in range(len(my_labels))}
    df2 = df2.rename(index=my_labels_dict, columns=my_labels_dict)
    df2 = df2.replace(0, np.nan)

    # Create the plot
    sns.set_theme()
    ax = sns.heatmap(df2, annot=True, cmap='Reds', linewidth=0.3, vmin=0, linecolor='gray', cbar=False)
    plt.box(on=None)
    plt.tick_params(axis='x', colors='black', labelsize=8)
    plt.tick_params(axis='y', colors='black', labelsize=8)
    complexity_label = f"{time_or_space} Complexity"
    if time_or_space == "Space":
        complexity_label += " (Auxiliary)"
    plt.xlabel(f"Best {complexity_label}")
    plt.ylabel(f"First {complexity_label}")
    ax.xaxis.tick_top()
    ax.xaxis.set_label_position('top') 
    ax.invert_xaxis()
    plt.setp(ax.get_xticklabels(), rotation=45, ha="left",
         rotation_mode="anchor") # if you want x-axis label on top, change to ha="left"
    plt.tight_layout()

    # Save the plot
    try:
        plt.savefig(f"{save_dest}{title} (by {by_family_or_variation}).png", dpi=300, bbox_inches='tight')
    except Exception as e:
        print(e)
        print("Failed")

    # Close/clear the plot
    plt.clf()
    plt.close("all")
    return

def heat_best_space_vs_time(include_title):
    data = pd.read_csv('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/Hayden_Figures/wiki_data.csv')
    data = data.replace(np.nan, '', regex=True)
    count = 0
    skipped = 0
    df = pd.DataFrame(columns=["Best Space", "Best Time"])
    for fam in helpers.get_families():
        algorithms = helpers.get_algorithms_for_family(fam, data)
        if algorithms.empty:
            skipped += 1
            continue

        best_space = helpers.get_best_space(algorithms)
        best_time = helpers.get_best_time(algorithms)
        if best_space > best_time:
            print(fam)
            skipped += 1
            continue
        count += 1
        fam_df = pd.DataFrame([[best_space, best_time]], columns=['Best Space', 'Best Time'])
        df = pd.concat([df, fam_df], ignore_index=True)

    # Create df cross tabulation for the heatmap
    df2 = pd.crosstab(df['Best Space'], df['Best Time'])
    for i in range(8):
        if i not in df2.index:
            df2.loc[i] = pd.Series(0, index=df2.columns)
    for i in range(8):
        if i not in df2.columns:
            df2[i] = pd.Series(0, index=df2.index)
    df2 = df2.sort_index(axis=0, ascending=False)
    df2 = df2.sort_index(axis=1)
    # my_labels = ['constant', 'logn', 'linear', 'nlogn', 'quadratic', 'cubic', 'poly > cubic', 'exponential']
    my_labels = ['Constant', 'Logarithmic', 'Linear', 'n log n', 'Quadratic', 'Cubic', 'Poly (> Cubic)', 'Exponential']
    my_labels_dict = {i: my_labels[i] for i in range(len(my_labels))}
    df2 = df2.rename(index=my_labels_dict, columns=my_labels_dict)
    # df2 = df2.replace(0, np.nan)
    # Create the plot
    sns.set_theme()
    mask = np.rot90(np.triu(np.ones_like(df2, dtype=bool), k=1))
    cmap = CM.get_cmap('bone_r', 50)
    cmap = CM.get_cmap('BrBG', 200)
    # cmap = sns.light_palette("seagreen", as_cmap=True)

    ax = sns.heatmap(df2, mask=mask, annot=True, cmap=cmap, cbar_kws={"shrink": 0.95}, center=-1, cbar=True, linewidths=0.001,linecolor="grey") #, linewidth=0.3, linecolor='gray'
    cbar = ax.collections[0].colorbar
    cbar.set_label("Number of Problem Families", labelpad=25, rotation=270)
    plt.box(on=None)
    plt.tick_params(axis='x', colors='black', labelsize=8)
    plt.tick_params(axis='y', colors='black', labelsize=8)
    plt.xlabel(f"Best Time Complexity")
    plt.ylabel(f"Best Auxiliary Space Complexity")
    ax.xaxis.tick_top()
    ax.xaxis.set_label_position('top') 
    ax.invert_xaxis()
    # ax.yaxis.tick_right()
    # ax.yaxis.set_label_position('right')
    # plt.setp(ax.get_yticklabels(), rotation=0, ha="left",
    #      rotation_mode="anchor") # if you want x-axis label on top, change to ha="left"
    plt.setp(ax.get_xticklabels(), rotation=45, ha="left",
         rotation_mode="anchor") # if you want x-axis label on top, change to ha="left"
    plt.tight_layout()

    # Save the plot
    save_dest = "/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/Hayden_Figures/"
    title = "Best Space vs Time"
    try:
        plt.savefig(f"{save_dest}{title}.png", dpi=300, bbox_inches='tight')
    except Exception as e:
        print(e)
        print("Failed")
    
def heat_size_of_improvements(by_family_or_variation, include_title):
    save_dest = 'Analysis/Plots/Heatmaps/'

    fams = helpers.get_families()
    space_df = pd.DataFrame(columns=['Pre-Improvement', 'Post-Improvement'])
    time_df = pd.DataFrame(columns=['Pre-Improvement', 'Post-Improvement'])

    for fam in fams:
        if by_family_or_variation == "Variation":
            vars = helpers.get_variations(fam)
        elif by_family_or_variation == "Family":
            vars = ["by family"]

        for var in vars:
            space_improvements = get_space_improvements_by_type(fam, var, True)[0]
            space_var_df = pd.DataFrame(space_improvements, columns=['Pre-Improvement', 'Post-Improvement'])
            space_df = pd.concat([space_df, space_var_df], ignore_index=True)
            time_improvements = get_time_improvements_by_type(fam, var, True)[0]
            time_var_df = pd.DataFrame(time_improvements, columns=['Pre-Improvement', 'Post-Improvement'])
            time_df = pd.concat([time_df, time_var_df], ignore_index=True)
    
    # Create df cross tabulation for the heatmap
    space_df['Space Improvements (Auxiliary)'] = space_df['Pre-Improvement'] - space_df['Post-Improvement']
    time_df['Time Improvements'] = time_df['Pre-Improvement'] - time_df['Post-Improvement']

    df2 = pd.concat([time_df['Time Improvements'].value_counts(), space_df['Space Improvements (Auxiliary)'].value_counts()], axis=1)
    for i in range(1,8):
        if i not in df2.index:
            df2.loc[i] = pd.Series(0, index=df2.columns)
    df2 = df2.sort_index(axis=0, ascending=False)
    # print(tabulate(df2))


    ax = sns.heatmap(df2, annot=True, cmap='Greens', linewidth=0.3, vmin=0, linecolor='gray', fmt='.3g')
    plt.ylabel("Improvement Size (number of classes)")
    plt.box(on=None)
    plt.tick_params(axis='x', colors='#A6A6A6')
    plt.tick_params(axis='y', colors='#A6A6A6', rotation=0)

    title = "Size of Improvements Heatmap (by " + by_family_or_variation +")"
    if include_title:
        plt.title(title)

    plt.tight_layout()
    # plt.show()

    try:
        plt.savefig(save_dest + title + ".png", dpi=300, bbox_inches='tight')
    except Exception as e:
        print(e)
        print("Failed")

    plt.clf()
    plt.close("all")
    return

def heat_2x2_time_space_improvements(by_problem_or_algorithm, by_family_or_variation, include_title):
    save_dest = f"Analysis/Plots/Heatmaps/"

    df = pd.read_csv('Analysis/data.csv')
    df = df.replace(np.nan, '', regex=True)
    families = helpers.get_families()
    improves_space = []
    improves_time = []
    improves_both = []
    no_improve = []
    count = 0


    def get_array_of_improvements(algorithms, improves_space, improves_time, improves_both, no_improve, count):
        algorithms = algorithms[algorithms['Param: Space Class'].str.contains(':')].sort_values('Year')

        best_time = None
        best_space = None
        first_algo = True
        improved_space = False
        improved_time = False

        for index, row in algorithms.iterrows():
            item = {}
            item['year'] = int(row['Year'])
            item['space'] = float(row['Space Complexity Class']) - 1
            try:
                item['time'] = float(row['Time Complexity Class']) - 1
            except:
                print("Issue getting time complexity for:", row['Family Name'], row['Algorithm Name'], "\n     Time complexity class:", row['Time Complexity Class'])
                return count
            item['name'] = row['Algorithm Name']

            if by_problem_or_algorithm == "Algorithm":
                if first_algo:
                    first_algo = False
                    best_space = item['space']
                    best_time = item['time']
                else:
                    count += 1
                    if item['space'] < best_space and item['time'] < best_time:
                        best_space = item['space']
                        best_time = item['time']
                        improves_both.append(item['name'])
                    elif item['space'] < best_space:
                        best_space = item['space']
                        improves_space.append(item['name'])
                    elif item['time'] < best_time:
                        best_time = item['time']
                        improves_time.append(item['name'])
                    else:
                        no_improve.append(item['name'])
            elif by_problem_or_algorithm == "Problem":
                if first_algo:
                    first_algo = False
                    best_space = item['space']
                    best_time = item['time']
                else:
                    if item['space'] < best_space and item['time'] < best_time:
                        improved_space = True
                        improved_time = True
                    elif item['space'] < best_space:
                        improved_space = True
                    elif item['time'] < best_time:
                        improved_time = True

                    if improved_time and improved_space:
                        break

        if by_problem_or_algorithm == "Problem":
            count += 1
            if improved_time and improved_space:
                improves_both.append(family_name)
            elif improved_time:
                improves_time.append(family_name)
            elif improved_space:
                improves_space.append(family_name)
            else:
                no_improve.append(family_name)
        return count



    for family_name in families:
        vars = helpers.get_variations(family_name)
        algorithms = df.loc[df['Family Name'] == family_name]
        if by_family_or_variation == "Variation":
            for variation in vars:
                var_algorithms = algorithms.loc[algorithms['Variation'] == variation]
                if var_algorithms.empty:
                    print('No data found for family name: ' +
                        family_name + ' and variation: ' + variation)
                    continue
                count = get_array_of_improvements(var_algorithms, improves_space, improves_time, improves_both, no_improve, count)
        else:
            if algorithms.empty:
                print('No data found for family name: ' +
                    family_name)
                continue
            count = get_array_of_improvements(algorithms, improves_space, improves_time, improves_both, no_improve, count)

    print(f"\nNumber of {by_family_or_variation}s used: {count}\n")
    print(f"Improves neither: {len(no_improve)}")
    for i in no_improve:
        print(i)
    print(f"Improves time: {len(improves_time)}")
    print(f"Improves space: {len(improves_space)}")
    print(f"Improves both: {len(improves_both)}\n")
    graph_df = pd.DataFrame({"Doesn't Improve": [len(no_improve)/count, len(improves_time)/count], "Improves": [len(improves_space)/count, len(improves_both)/count]},
    index=["Doesn't Improve", "Improves"])


    ax = sns.heatmap(graph_df, annot=True, cmap='Greens', linewidth=0.1, vmin=0, linecolor='gray', cbar=False)
    plt.ylabel("Time Improvement?")
    plt.xlabel("Space Improvement? (Auxiliary)")
    plt.box(on=None)
    plt.tick_params(axis='x', colors='black', labelsize=8)
    plt.tick_params(axis='y', colors='black', rotation=0, labelsize=8)
    ax.xaxis.tick_top()
    ax.xaxis.set_label_position('top')

    title = f"Proportion of {by_problem_or_algorithm}s that Improve (by {by_family_or_variation})"
    if include_title:
        plt.title(title)
    plt.tight_layout()
    count = 0

    try:
        plt.savefig(save_dest + title + ".png", dpi=300, bbox_inches='tight')
    except Exception as e:
        print(e)
        print("Failed")

    plt.clf()
    plt.close("all")
    return

def pie_best_space_comparative(num_for_split, by_family_or_variation, include_title, domain=None, df=None):
    """
    0: Constant
    1: Log n
    2: Linear
    ...

    Args:
        num_for_split: The number of complexity class that you want split at (e.g. sub___, ___, super___)

    Returns:
        List of two tuples:
            Tuple of three ints (# problems sub___, # problems ___, # problems super___)
            Tuple of the proportions of the above
    """

    if df is None:
        df = pd.read_csv('Analysis/data.csv')
        df = df.replace(np.nan, '', regex=True)

    families = helpers.get_families(df)
    sub_space = 0
    at_space = 0
    super_space = 0
    count = 0

    class_string = {0: "Constant", 1: "Logarithmic", 2: "Linear", 3: "n log n", 4: "Quadratic", 5: "Cubic", 6: "Polynomial (> 3)", 7: "Exponential"}

    if by_family_or_variation == "Variation":
        print(f"\nProblem variations with best-space that is super-{class_string[num_for_split]}")
    else:
        print(f"\nProblem families with best-space that is super-{class_string[num_for_split]}")
        if domain is not None:
            print(f"in the domain {domain}")

    for family_name in families:
        vars = helpers.get_variations(family_name)
        algorithms = df.loc[df['Family Name'] == family_name]
        if by_family_or_variation == "Variation":   
            for variation in vars:
                var_algorithms = algorithms.loc[algorithms['Variation'] == variation]
                if var_algorithms.empty:
                    print('No data found for family name: ' +
                        family_name + ' and variation: ' + variation)
                    continue
                best_space = helpers.get_best_space(var_algorithms)
                count += 1
                if best_space < num_for_split:
                    sub_space += 1
                elif best_space == num_for_split:
                    at_space += 1
                elif best_space > num_for_split:
                    print(f"{family_name}: {variation} -- {class_string[best_space]}")
                    super_space += 1
        else:
            if algorithms.empty:
                print('No data found for family name: ' +
                    family_name)
                continue
            best_space = helpers.get_best_space(algorithms)
            count += 1
            if best_space < num_for_split:
                sub_space += 1
            elif best_space == num_for_split:
                at_space += 1
            elif best_space > num_for_split:
                print(f"{family_name} -- {class_string[best_space]}")
                super_space += 1
                
    print(f"\nNumbers of {by_family_or_variation}:")
    if domain is not None:
        print(f"in domain {domain}")
    print(f"Sub-{class_string[num_for_split]}: {sub_space}, ({sub_space / count})")
    print(f"At-{class_string[num_for_split]}: {at_space}, ({at_space / count})")
    print(f"Super-{class_string[num_for_split]}: {super_space}, ({super_space / count})\n")
    if num_for_split == 0:
        data = [at_space, super_space]
        labels = [f"{class_string[num_for_split]}", f"Super-{class_string[num_for_split]}"]
        explode = [0, 0]
    else:
        data = [sub_space, at_space, super_space]
        labels = [f"Sub-{class_string[num_for_split]}", f"{class_string[num_for_split]}", f"Super-{class_string[num_for_split]}"]
        explode = [0,0,0.1]
    sns.set_palette("Reds", 3)
    plt.figure(figsize=(18, 9))
    for i in range(len(data)):
        if data[i] == 0:
            labels[i] = None

    def make_autopct(counts):
        def my_autopct(pct):
            total = sum(counts)
            val = int(round(pct*total/100.0))
            if val == 0:
                return ""
            else:
                return '{p:.1f}%'.format(p=pct)
        return my_autopct
        
    plt.pie(data, labels=labels, autopct=make_autopct(data), explode=explode, startangle=90, counterclock=False)
    if domain is not None:
        plt.title(f"{domain}", fontsize=20)
    if include_title:
        if domain is not None:
            plt.title(f"Problems' Best Space Complexity (Auxiliary) Compared to {class_string[num_for_split]} Space")
        else:
            plt.title(f"{domain} Problems' Best Space Complexity (Auxiliary) Compared to {class_string[num_for_split]} Space")
    if domain is None:
        save_dest = "Analysis/Plots/Best Space Algos/"
    else:
        save_dest = f"Analysis/Plots/Best Space Algos/By Domain/{domain} "
    plt.savefig(f"{save_dest}{class_string[num_for_split]} Pie (by {by_family_or_variation}).png", dpi=300, bbox_inches='tight')
    plt.clf()
    plt.close("all")
    return [(sub_space, at_space, super_space), (sub_space / count, at_space / count, super_space / count)]

def pie_best_space(by_family_or_variation, include_title, domain=None, df=None):
    """
    Args:
        by_family_or_variation: "Family" or "Variation"

    Returns:
        List of # of problems with best space algo in each of the classes
    """
    if df is None:
        df = pd.read_csv('Analysis/data.csv')
        df = df.replace(np.nan, '', regex=True)

    families = helpers.get_families(df)
    counts = [0 for i in range(8)]

    class_string = {0: "Constant", 1: "Logarithmic", 2: "Linear", 3: "n log n", 4: "Quadratic", 5: "Cubic", 6: "Polynomial (> 3)", 7: "Exponential"}

    if by_family_or_variation == "Variation":
        print(f"\nProblem variations with best-space")
    else:
        print(f"\nProblem families with best-space")
        if domain is not None:
            print(f"in the domain {domain}")

    for family_name in families:
        vars = helpers.get_variations(family_name)
        algorithms = df.loc[df['Family Name'] == family_name]
        if by_family_or_variation == "Variation":   
            for variation in vars:
                var_algorithms = algorithms.loc[algorithms['Variation'] == variation]
                if var_algorithms.empty:
                    print('No data found for family name: ' +
                        family_name + ' and variation: ' + variation)
                    continue
                best_space = helpers.get_best_space(var_algorithms)
                counts[best_space] += 1
        else:
            if algorithms.empty:
                print('No data found for family name: ' +
                    family_name)
                continue
            best_space = helpers.get_best_space(algorithms)
            counts[best_space] += 1
                
    print(f"\nNumbers of {by_family_or_variation}:")
    for i in range(len(class_string)):
        print(f"{class_string[i]}: {counts[i]}, ({'{:.2f}'.format(counts[i] / sum(counts) * 100)}%)")
    print()

    labels = [class_string[i] for i in range(len(class_string))]
    for i in range(len(counts)):
        if counts[i] == 0:
            labels[i] = None
    sns.set_palette("Reds", len(class_string))
    plt.figure(figsize=(18, 9))

    def make_autopct(counts):
        def my_autopct(pct):
            total = sum(counts)
            val = int(round(pct*total/100.0))
            if val == 0:
                return ""
            else:
                return '{p:.1f}%'.format(p=pct)
        return my_autopct

    # patches, texts, autotexts = plt.pie(counts, labels=labels, autopct='%1.1f%%', startangle=90, counterclock=False)
    patches, texts, autotexts = plt.pie(counts, labels=labels, autopct=make_autopct(counts), startangle=90, counterclock=False)
    if domain is not None:
        plt.title(f"{domain}", fontsize=20)
    if include_title:
        if domain is None:
            plt.title(f"Problems' Best Auxiliary Space Complexity")
        else:
            plt.title(f"{domain} Problems' Best Auxiliary Space Complexity")
    if domain is None:
        save_dest = "Analysis/Plots/Best Space Algos/"
    else:
        save_dest = f"Analysis/Plots/Best Space Algos/By Domain/{domain} "
    plt.tight_layout()
    plt.savefig(f"{save_dest}Best Space Pie (by {by_family_or_variation}).png", dpi=300, bbox_inches='tight')
    plt.clf()
    plt.close("all")
    return counts

def pie_best_time(by_family_or_variation, include_title, domain=None, df=None):
    """
    Args:
        by_family_or_variation: "Family" or "Variation"

    Returns:
        List of # of problems with best space algo in each of the classes
    """
    if df is None:
        df = pd.read_csv('Analysis/data.csv')
        df = df.replace(np.nan, '', regex=True)

    families = helpers.get_families(df)
    counts = [0 for i in range(8)]

    class_string = {0: "Constant", 1: "Logarithmic", 2: "Linear", 3: "n log n", 4: "Quadratic", 5: "Cubic", 6: "Polynomial (> 3)", 7: "Exponential"}

    if by_family_or_variation == "Variation":
        print(f"\nProblem variations with best-time")
    else:
        print(f"\nProblem families with best-time")
        if domain is not None:
            print(f"in the domain {domain}")

    for family_name in families:
        vars = helpers.get_variations(family_name)
        algorithms = df.loc[df['Family Name'] == family_name]
        if by_family_or_variation == "Variation":   
            for variation in vars:
                var_algorithms = algorithms.loc[algorithms['Variation'] == variation]
                if var_algorithms.empty:
                    print('No data found for family name: ' +
                        family_name + ' and variation: ' + variation)
                    continue
                best_time = helpers.get_best_time(var_algorithms)
                counts[best_time] += 1
        else:
            if algorithms.empty:
                print('No data found for family name: ' +
                    family_name)
                continue
            best_time = helpers.get_best_time(algorithms)
            counts[best_time] += 1
                
    print(f"\nNumbers of {by_family_or_variation}:")
    for i in range(len(class_string)):
        print(f"{class_string[i]}: {counts[i]}, ({'{:.2f}'.format(counts[i] / sum(counts) * 100)}%)")
    print()

    labels = [class_string[i] for i in range(len(class_string))]
    for i in range(len(counts)):
        if counts[i] == 0:
            labels[i] = None
    sns.set_palette("Reds", len(class_string))
    plt.figure(figsize=(18, 9))

    def make_autopct(counts):
        def my_autopct(pct):
            total = sum(counts)
            val = int(round(pct*total/100.0))
            if val == 0:
                return ""
            else:
                return '{p:.1f}%'.format(p=pct)
        return my_autopct

    # patches, texts, autotexts = plt.pie(counts, labels=labels, autopct='%1.1f%%', startangle=90, counterclock=False)
    patches, texts, autotexts = plt.pie(counts, labels=labels, autopct=make_autopct(counts), startangle=90, counterclock=False)
    if domain is not None:
        plt.title(f"{domain}", fontsize=20)
    if include_title:
        if domain is None:
            plt.title(f"Problems' Best Time Complexity")
        else:
            plt.title(f"{domain} Problems' Best Auxiliary Time Complexity")
    if domain is None:
        save_dest = "Analysis/Plots/Best Time Algos/"
    else:
        save_dest = f"Analysis/Plots/Best Time Algos/By Domain/{domain} "
    plt.tight_layout()
    plt.savefig(f"{save_dest}Best Time Pie (by {by_family_or_variation}).png", dpi=300, bbox_inches='tight')
    plt.clf()
    plt.close("all")
    return counts

def pie_best_space_comparative_by_domain(num_for_split, by_family_or_variation, include_title):
    """Plot the pie chart of best space compared to a specific class for all problems in each domain separately"""
    df = pd.read_csv('Analysis/data.csv')
    df = df.replace(np.nan, '', regex=True)
    gb = df.groupby(by="Domains")
    for domain, group in gb:
        pie_best_space_comparative(num_for_split, by_family_or_variation, include_title, domain, group)

def pie_best_space_by_domain(by_family_or_variation, include_title):
    """Plot the pie chart of best space for all problems in each domain separately"""
    df = pd.read_csv('Analysis/data.csv')
    df = df.replace(np.nan, '', regex=True)
    gb = df.groupby(by="Domains")
    for domain, group in gb:
        pie_best_space(by_family_or_variation, include_title, domain, group)

def pie_best_time_by_domain(by_family_or_variation, include_title):
    """Plot the pie chart of best space for all problems in each domain separately"""
    df = pd.read_csv('Analysis/data.csv')
    df = df.replace(np.nan, '', regex=True)
    gb = df.groupby(by="Domains")
    for domain, group in gb:
        pie_best_time(by_family_or_variation, include_title, domain, group)

def hist_papers_per_decade(include_title):
    """
    Create a histogram showing the number of papers in our database per decade.

    Note: "1940s" is actually "1940s and before"
    """

    df = pd.read_csv('Analysis/data_dirty.csv')
    df = df.replace(np.nan, '', regex=True)

    save_dest = "Analysis/Plots/Histograms/"
    plot_title = "Number of Papers Per Decade"

    df.loc[df["Year"] < 1940, "Year"] = 1940
    years = df[df["Derived Space Complexity?"].isin(["0", "1", 0, 1])]["Year"]
    bins = range(1940, 2030, 10)
    sns.set_theme()
    counts, bins, patches = plt.hist(years, bins=bins)

    # print(f"{plot_title}")
    # for bar, b0, b1 in zip(counts, bins[:-1], bins[1:]):
    #     print(f'{b0:3d} - {b1:3d}: {bar:4.0f}')

    plt.ylabel("Number of Papers")
    plt.xlabel("Decade Published")
    if include_title:
        plt.title(plot_title)
    plt.tight_layout()

    plt.savefig(save_dest + plot_title + ".png", dpi=300, bbox_inches="tight")
    plt.clf()
    plt.close("all")
    return

def hist_space_analysis_per_decade(absolute_or_percent, original, include_title):
    """
    Creates two histograms--one showing the number of papers in our database that actually analyzed space complexity per decade,
    and one showing the number of papers that didn't analyze the space complexity (and we had to derive it ourselves) per decade.

    Note: "1940s" is actually "1940s and before"

    Args:
        absolute_or_percent: string "Absolute" or "Percent"
        original: Bool, True=space complexity in the original paper, False=space complexity in any paper
    """

    save_dest = "Analysis/Plots/Histograms/"

    # Get the data first
    df = pd.read_csv('Analysis/data_dirty.csv')
    df = df.replace(np.nan, '', regex=True)
    df.loc[df["Year"] < 1940, "Year"] = 1940
    if original:
        not_analyzed_years = df[df["Space Complexity in Original Paper?"].isin(["0", 0])]["Year"]
        not_analyzed_years = not_analyzed_years.rename("Without Space Analysis")
        analyzed_years = df[df["Space Complexity in Original Paper?"].isin(["1", 1])]["Year"]
        analyzed_years = analyzed_years.rename("With Space Analysis")
    else:
        not_analyzed_years = df[df["Derived Space Complexity?"].isin(["1", 1])]["Year"]
        not_analyzed_years = not_analyzed_years.rename("Without Space Analysis")
        analyzed_years = df[df["Derived Space Complexity?"].isin(["0", 0])]["Year"]
        analyzed_years = analyzed_years.rename("With Space Analysis")
    bins = range(1940, 2030, 10)

    # Papers With Space Complexity Analysis
    plot_title = "Number of Papers Per Decade With Space Analysis"

    sns.set_theme()
    analyzed_counts, analyzed_bins, patches = plt.hist(analyzed_years, bins=bins)


    plt.ylabel("Number of Papers")
    plt.xlabel("Decade Published")
    if include_title:
        plt.title(plot_title)
    plt.tight_layout()

    plt.savefig(save_dest + plot_title + ".png", dpi=300, bbox_inches="tight")
    plt.clf()
    plt.close("all")

    # Papers Without Space Complexity Analysis
    plot_title = "Number of Papers Per Decade Without Space Analysis"
    
    sns.set_theme()
    not_analyzed_counts, not_analyzed_bins, patches = plt.hist(not_analyzed_years, bins=bins)

    print(f"\nNumber of Papers Per Decade With Space Analysis")
    # for bar, b0, b1, other in zip(analyzed_counts, analyzed_bins[:-1], analyzed_bins[1:], not_analyzed_counts):
    #     print(f'{b0:3d} - {b1:3d}: {bar:4.0f} ({(bar/(bar + other) * 100):.2f}%)')

    print(f"\nNumber of Papers Per Decade Without Space Analysis")
    # for bar, b0, b1, other in zip(not_analyzed_counts, not_analyzed_bins[:-1], not_analyzed_bins[1:], analyzed_counts):
    #     print(f'{b0:3d} - {b1:3d}: {bar:4.0f} ({(bar/(bar + other) * 100):.2f}%)')

    plt.ylabel("Number of Papers")
    plt.xlabel("Decade Published")
    if include_title:
        plt.title(plot_title)
    plt.tight_layout()

    plt.savefig(save_dest + plot_title + ".png", dpi=300, bbox_inches="tight")
    plt.clf()
    plt.close("all")

    # Putting the two together
    if absolute_or_percent == "Absolute":
        plot_title = f"Number of {'Original ' if original else ''}Algorithm Papers with Space Complexity Analysis"
        save_title = plot_title + " (Absolutes)"
    elif absolute_or_percent == "Percent":
        plot_title = f"Percentage of {'Original ' if original else ''}Algorithm Papers with Space Complexity Analysis"
        save_title = plot_title + " (Percents)"
    
    sns.set_theme()
    if absolute_or_percent == "Absolute":
        # plt.ylabel("Number of Papers", fontsize=8)
        counts, bins, patches = plt.hist([analyzed_years, not_analyzed_years], bins=bins,
                                        label=["With Space Analysis", "Without Space Analysis"],
                                        histtype="bar")

        with_space, without_space = counts
        print(f"\n{plot_title} -- Papers With vs Without Space Analysis")
        for with_bar, without_bar, b0, b1 in zip(with_space, without_space, bins[:-1], bins[1:]):
            print(f'{b0:3d} - {b1:3d}: {with_bar:4.0f} {without_bar:4.0f}')
    elif absolute_or_percent == "Percent":
        # plt.ylabel("Percent of Papers", fontsize=8)
        total_per_year = [with_ + without_ for (with_, without_) in zip(analyzed_counts, not_analyzed_counts)]
        percent_with = [with_ / total for (with_, total) in zip(analyzed_counts, total_per_year)]
        percent_without = [without_ / total for (without_, total) in zip(not_analyzed_counts, total_per_year)]
        width = 2.25
        labels = ["1940s\nand earlier", "1950s", "1960s", "1970s", "1980s", "1990s", "2000s", "2010s"]
        plt.bar([i*3 for i in range(len(labels))], percent_with, width, label="With space analysis", color="#C81C1C") # #C81C1C, #1B83A0, #00BCA0
        plt.bar([i*3 for i in range(len(labels))], percent_without, width, label="Without space analysis", bottom=percent_with, color="#1B83A0")
        for i in range(len(labels)):
            plt.annotate("{:.0%}".format(percent_with[i]), (i * 3, percent_with[i] / 2), fontsize=8, ha="center", va="center", color="white")
            plt.annotate("{:.0%}".format(percent_without[i]), (i * 3, percent_with[i] + percent_without[i] / 2), fontsize=8, ha="center", va="center", color="white")
        plt.xticks([i*3 for i in range(len(labels))], labels)
        plt.xticks(fontsize=8)
        plt.yticks(fontsize=8)
        plt.ylim((0, 1))
        plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1.0))

    if include_title:
        plt.title(plot_title)
    # plt.legend(loc="upper right")
    plt.legend(loc="lower center", bbox_to_anchor=(0.2, -0.2, 0.6, 0.2), mode="expand", ncol=2, fontsize=8)
    plt.tight_layout()

    plt.savefig(save_dest + save_title + ".png", dpi=300, bbox_inches="tight")
    plt.clf()
    plt.close("all")

    if absolute_or_percent == "Percent":
        x = range(len(percent_with))
        y = percent_with
        res = stats.linregress(x, y)
        plt.plot(x, y, 'o')
        plt.plot(x, res.intercept + res.slope * x, 'r')
        plt.xticks(range(len(percent_with)), labels)
        lt = ""
        action = ""
        if res.pvalue < 0.05:
            lt = "<"
            action = "reject"
        else:
            lt = ">"
            action = "not reject"
        print(f"\nThe percentage of papers with space analysis is increasing by {'{:.2f}'.format(res.slope * 100)} per decade\nwith an r-value of {'{:.4f}'.format(res.rvalue)} and a p-value of {'{:.4f}'.format(res.pvalue)} which is {lt} 0.05,\nso we may {action} the null hypothesis that the percentage doesn't change over time.\n")
        plt.clf()
        plt.close("all")
        # plt.show()
    return

def hist_optimal_algos_per_decade(by_family_or_variation, include_title):
    """
    Creates a 100% histogram, showing the % of problems with an optimal algo vs ones with space-time tradeoffs, per decade.
    """
    save_dest = "Analysis/Plots/Histograms/"

    # Get the data first
    df = pd.read_csv('Analysis/data_dirty.csv')
    df = df.replace(np.nan, '', regex=True)
    df.loc[df["Year"] < 1940, "Year"] = 1940
    percents_optimal = []
    for decade_end in range(1950, 2030, 10):
        decade_df = df[df["Year"] < decade_end]
        decade_df = decade_df[decade_df["Space Complexity Class"] != "#VALUE!"]
        percents_optimal.append(fraction_of_optimality(by_family_or_variation, decade_df)[2])
    percents_tradeoff = [1.0 - percent for percent in percents_optimal]
    bins = range(1940, 2030, 10)

    # Make the plot
    plot_title = "Time Complexity - Space Complexity Tradeoffs"
    sns.set_theme()
    plt.ylabel("Percent of Problems", fontsize=8)
    width = 2.25
    labels = ["1940s\nand earlier", "1950s", "1960s", "1970s", "1980s", "1990s", "2000s", "2010s"]
    plt.bar([i*3 for i in range(len(labels))], percents_tradeoff, width, label="Time-space tradeoff", color="#C81C1C") # #C81C1C, #1B83A0, #00BCA0
    plt.bar([i*3 for i in range(len(labels))], percents_optimal, width, label="Single algorithm optimal", bottom=percents_tradeoff, color="#1B83A0")
    for i in range(len(labels)):
        plt.annotate("{:.1%}".format(percents_tradeoff[i]), (i * 3, percents_tradeoff[i] / 2), fontsize=8, ha="center", va="center", color="white")
        plt.annotate("{:.1%}".format(percents_optimal[i]), (i * 3, percents_tradeoff[i] + percents_optimal[i] / 2), fontsize=8, ha="center", va="center", color="white")
    plt.xticks([i*3 for i in range(len(labels))], labels)
    plt.xticks(fontsize=8)
    plt.yticks(fontsize=8)
    plt.ylim((0, 1))
    plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1.0))
    
    if include_title:
        plt.title(plot_title)
    # plt.legend(loc="upper right")
    plt.legend(loc="lower center", bbox_to_anchor=(0.2, -0.2, 0.6, 0.2), mode="expand", ncol=2, fontsize=8)
    plt.tight_layout()

    plt.savefig(save_dest + plot_title + f" (by {by_family_or_variation}).png", dpi=300, bbox_inches="tight")
    plt.clf()
    plt.close("all")

    x = range(len(percents_tradeoff))
    y = percents_tradeoff
    res = stats.linregress(x, y)
    plt.plot(x, y, 'o')
    plt.plot(x, res.intercept + res.slope * x, 'r')
    plt.xticks(range(len(percents_tradeoff)), labels)
    lt = ""
    action = ""
    if res.pvalue < 0.05:
        lt = "<"
        action = "reject"
    else:
        lt = ">"
        action = "not reject"
    print(f"\nThe percentage of problem {by_family_or_variation.lower()}s with tradeoffs is increasing by {'{:.2f}'.format(res.slope * 100)} per decade\nwith an r-value of {'{:.4f}'.format(res.rvalue)} and a p-value of {'{:.4f}'.format(res.pvalue)} which is {lt} 0.05,\nso we may {action} the null hypothesis that the percentage doesn't change over time.\n")
    # plt.show()
    plt.clf()
    plt.close("all")
    return

def hist_space_and_time_improvements_per_decade(by_family_or_variation, include_title):
    by_family_or_variation = by_family_or_variation.lower()

    fams = helpers.get_families()
    space_improvements = []
    time_improvements = []

    for fam in fams:
        if by_family_or_variation == "variation":
            vars = helpers.get_variations(fam)
        elif by_family_or_variation == "family":
            vars = ["by family"]
        for var in vars:
            space_ = get_space_improvements_by_year(fam, var, False)
            time_ = get_time_improvements_by_year(fam, var, False)
            if space_:
                space_improvements.extend(space_)
            if time_:
                time_improvements.extend(time_)

    # Putting the two side-by-side
    save_dest = "Analysis/Plots/Histograms/"
    plot_title = "Improvements Per Decade (Bars)"
    
    bins = range(1940, 2030, 10)
    sns.set_theme()
    counts, bins, patches = plt.hist([time_improvements, space_improvements], bins=bins,
                                    label=["Time Improvements", "Space Improvements (Auxiliary)"],
                                    histtype="bar")

    time, space = counts
    print(f"\n{plot_title} -- Time improvements vs space improvements")
    # for time_bar, space_bar, b0, b1 in zip(time, space, bins[:-1], bins[1:]):
        # print(f'{b0:3d} - {b1:3d}: {time_bar:4.0f} {space_bar:4.0f}')

    plt.ylabel("Number of Improvements")
    plt.xlabel("Decade Published")
    if include_title:
        plt.title(plot_title)
    plt.legend(loc="upper left")
    plt.tight_layout()

    plt.savefig(save_dest + plot_title + f" (by {by_family_or_variation})" + ".png", dpi=300, bbox_inches="tight")
    plt.clf()
    plt.close("all")
    return


include_title = False

# helpers.clean_data()

# hist_optimal_algos_per_decade("Family", include_title)
# hist_optimal_algos_per_decade("Variation", include_title)

# print("\n-----------------------------\n")

# hist_improvements("Number", "Time", "Family", include_title)
# hist_improvements("Number", "Time", "Variation", include_title)
# hist_improvements("Number", "Space", "Family", include_title)
# hist_improvements("Number", "Space", "Variation", include_title)
# hist_improvements("Year", "Time", "Family", include_title)
# hist_improvements("Year", "Time", "Variation", include_title)
# hist_improvements("Year", "Space", "Family", include_title)
# hist_improvements("Year", "Space", "Variation", include_title)

# print("\n-----------------------------\n")

# heat_improvements_by_type("Time", "Family", include_title)
# heat_improvements_by_type("Time", "Variation", include_title)
# heat_improvements_by_type("Space", "Family", include_title)
# heat_improvements_by_type("Space", "Variation", include_title)

# heat_improvements_first_to_best("Time", "Family", include_title)
# heat_improvements_first_to_best("Time", "Variation", include_title)
# heat_improvements_first_to_best("Space", "Family", include_title)
# heat_improvements_first_to_best("Space", "Variation", include_title)

# print("\n-----------------------------\n")

# heat_size_of_improvements("Family", include_title)
# heat_size_of_improvements("Variation", include_title)

# print("\n-----------------------------\n")

# heat_2x2_time_space_improvements("Algorithm", "Family", include_title)
# heat_2x2_time_space_improvements("Algorithm", "Variation", include_title)
# heat_2x2_time_space_improvements("Problem", "Family", include_title)
# heat_2x2_time_space_improvements("Problem", "Variation", include_title)


# print("\n-----------------------------\n")

# pie_best_space_comparative(0, "Family", include_title)
# pie_best_space_comparative(0, "Variation", include_title)
# pie_best_space_comparative(2, "Family", include_title)
# pie_best_space_comparative(2, "Variation", include_title)

# pie_best_space_comparative_by_domain(0, "Family", include_title)
# pie_best_space_comparative_by_domain(2, "Family", include_title)

# pie_best_space("Family", include_title)
# pie_best_space("Variation", include_title)
# pie_best_time("Family", include_title)

# pie_best_space_by_domain("Family", include_title)
# pie_best_time_by_domain("Family", include_title)

# print("\n-----------------------------\n")

# hist_papers_per_decade(include_title)
# hist_space_analysis_per_decade("Percent", False, include_title)
# hist_space_analysis_per_decade("Percent", True, include_title)
# hist_space_and_time_improvements_per_decade("Family", include_title)
# hist_space_and_time_improvements_per_decade("Variation", include_title)




# count = 0
# total = 0
# for family in helpers.get_families():
    # improvements = get_space_improvements_by_type(family, "by family", False)[1]
    # improvements = get_time_improvements_by_type(family, "by family", False)[1]
    # total += 1
    # if len(improvements) == 1:
    #     continue
    # else:
        # count += 1
        # print()
        # print(family)
        # print(improvements)
        # print()
# print(f"{count} out of {total}")


heat_best_space_vs_time(True)

# pie_best_space("Family", True)
# pie_best_time("Family", True)
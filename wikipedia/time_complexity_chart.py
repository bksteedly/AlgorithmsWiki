import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

def time_complexity_chart():
    df = pd.read_csv('complexity_chart.csv')
    plt.figure(figsize=(11,8.25))
    plt.scatter(y=df['Time Complexity Class'], x=df['overall avg reads'])

    # Customize the plot (optional)
    plt.xlabel('Overall Average Reads')
    plt.ylabel('Time Complexity Class')
    plt.title('Wikipedia Average Monthly Reads and Time Complexity')
    custom_labels = ["Constant","Logorithmic","Linear","n log n","Quadratic","Cubic","Poly (> Cubic)","Exponential"]
    plt.gca().set_yticklabels(custom_labels)
    plt.yticks(rotation = 18)

    # Display the plot
    plt.savefig('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/wikipedia/time_complexity_vs_avg_reads.jpg')
    plt.show()

def space_complexity_chart():
    df = pd.read_csv('complexity_chart.csv')
    plt.figure(figsize=(11,8.25))
    plt.scatter(y=df['Space Complexity Class'], x=df['overall avg reads'])

    # Customize the plot (optional)
    plt.xlabel('Overall Average Reads')
    plt.ylabel('Space Complexity Class')
    plt.title('Wikipedia Average Monthly Reads and Space Complexity')
    custom_labels = ["Constant","Logorithmic","Linear","n log n","Quadratic","Cubic","Poly (> Cubic)","Exponential"]
    plt.gca().set_yticklabels(custom_labels)
    plt.yticks(rotation = 18)

    # Display the plot
    plt.savefig('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/wikipedia/space_complexity_vs_avg_reads.jpg')
    plt.show()

def reads_year_chart():
    df = pd.read_csv('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/wikipedia/reads_and_year_data.csv')
    plt.figure(figsize=(11,8.25))
    plt.scatter(y=df['overall avg reads'], x=df['Year'])

    # Customize the plot (optional)
    plt.xlabel('Year')
    plt.ylabel('Overall Average Reads')
    plt.title('Wikipedia Average Monthly Reads by Algorithm Year')
    #plt.yticks(rotation = 18)

    # Display the plot
    plt.savefig('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/wikipedia/year_v_avg_reads.jpg')
    plt.show()

def wiki_problems_and_articles_chart():
    df = pd.read_csv('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/wikipedia/problems_and_articles.csv')
    numbers = df['Number of Articles']
    df.plot(kind='bar')
    plt.xlabel('Problems')
    plt.ylabel('Number of Articles')
    plt.title('Wikipedia Articles Per Problem')
    plt.legend().set_visible(False)
    plt.xticks([25,50,75,100])
    plt.savefig('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/wikipedia/wiki_problems_and_articles.jpg')
    plt.show()

def sheet1_problems_and_articles_chart():
    df = pd.read_csv('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/wikipedia/problems_and_articles.csv')
    numbers = df['Sheet1 Algos']
    plt.bar(df.index, numbers)
    plt.xlabel('Problems')
    plt.ylabel('Number of Articles')
    plt.title('Sheet1 Articles Per Problem')
    plt.legend().set_visible(False)
    plt.xticks([25,50,75,100])
    plt.savefig('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/wikipedia/sheet1_problems_and_articles.jpg')
    plt.show()

def time_complexity_over_time():
    df = pd.read_csv('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/wikipedia/wikipedia_complexity_year.csv')
    plt.figure(figsize=(11,8.25))
    plt.scatter(y=df['Time Complexity Class'], x=df['Year'])

    # Customize the plot (optional)
    plt.xlabel('Year')
    plt.ylabel('Time Complexity Class')
    plt.title('Overall Average Reads Over Time')
    custom_labels = ["Constant","Logorithmic","Linear","n log n","Quadratic","Cubic","Poly (> Cubic)","Exponential"]
    plt.gca().set_yticklabels(custom_labels)
    plt.yticks(rotation = 18)

    # Display the plot
    plt.savefig('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/wikipedia/time_complexity_over_time.jpg')
    plt.show()
    
    


time_complexity_chart()
#space_complexity_chart()
#reads_year_chart()
#wiki_problems_and_articles_chart()
#sheet1_problems_and_articles_chart()
#time_complexity_over_time()





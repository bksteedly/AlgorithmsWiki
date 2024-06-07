import pandas as pd
import matplotlib.pyplot as plt

def num_authors_over_time():
    #read the data from the csv file and put it into a list
    df = pd.read_csv("/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/authors/output.csv")
    avg_authors_by_year = df.groupby('Year')['Number of Authors'].mean()
    plt.plot(avg_authors_by_year.index, avg_authors_by_year.values)
    plt.xlabel('Year')
    plt.ylabel('Average Number of Authors')
    plt.title('Average Number of Authors by Year')
    plt.savefig('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/authors/authors_visual.jpg')
    plt.show()

def time_complexity_num_authors():
    df1 = pd.read_csv("/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/authors/output.csv")
    df2 = pd.read_csv("/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/authors/Sheet1.csv")
    df2_subset = df2[["Algorithm Name", "Time Complexity Class"]]
    df = df1.merge(df2_subset, left_on="Algorithm", right_on="Algorithm Name", how="left")
    df.drop(columns=["Algorithm Name"])
    df = df[df['Number of Authors'] > 0]
    df = df[df['Time Complexity Class'].notnull()]
    df = df[df['Time Complexity Class'] != '#VALUE!']
    df['Time Complexity Class'] = df['Time Complexity Class'].astype(float)
    df.to_csv('time_complexity_num_authors_data.csv', index=False)
    y = df['Time Complexity Class']
    x = df['Number of Authors']
    plt.figure(figsize=(12, 8))
    plt.scatter(x,y)
    plt.ylabel("Time Complexity Class")
    plt.xlabel("Number of Authors")
    custom_yticks = [1,2,3,4,5,6,7,8]
    custom_ytick_labels = ['constant','logarithmic','linear','quasilinear (n log n)','quadratic','cubic','polynomial (>3)','exponential / factorial']
    plt.yticks(custom_yticks, custom_ytick_labels)
    plt.yticks(rotation=30)
    plt.title("Relationship Between an Algorithm's Time Complexity Class and Number of Authors on the Paper")
    plt.savefig('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/authors/time_complexity_class_authors_visual.jpg')
    plt.show


#num_authors_over_time()
time_complexity_num_authors()
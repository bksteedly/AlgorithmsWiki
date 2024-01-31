import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt


df = pd.read_csv('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/wikipedia/reads_and_year_data.csv')
x = df['Year']
y = df['overall avg reads']

x = sm.add_constant(x)
model = sm.OLS(y, x).fit()
print(model.summary())

plt.scatter(x['Year'], y, label='Data')
plt.plot(x['Year'], model.predict(x), color='red', label='Regression Line')
plt.xlabel('Year')
plt.ylabel('Average Monthly Reads')
plt.title('Relationship between Year of Algorithm and Average Monthly Reads')
plt.savefig('/Users/bellasteedly/Library/Mobile Documents/com~apple~CloudDocs/AlgorithmsWiki/wikipedia/year_vs_avg_reads_reg.jpg')
plt.show()




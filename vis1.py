import matplotlib as mt
import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import scipy.stats as sst

#data frame 
data = pd.read_csv("Crime.csv")
# print(data['State'].unique())
data.drop(columns='Unnamed: 0',inplace=True)
data = data.rename(columns={
    'K&A': 'Kidnapping and Abduction', 
    'DD': 'Dowry Deaths', 
    'AoW': 'Assault against Women', 
    'AoM': 'Insult to Modesty of Women',
    'DV': 'Domestic Violence',
    'WT': 'Women Trafficking'
})
print("Summary of the Data Frame:")
print(data.info())
print("Statistical Summary of the DataFrame:")
print(data.describe().T)

#data visualisation
print("Data Visualisation using matplotlib and seaborn python libraries:")
plt.figure(figsize = (10, 5), facecolor = 'grey')

# - - box plot
plt.subplot(1, 2, 1)
sb.boxplot(data['Rape'], boxprops = dict(color = 'green'))
plt.title('Boxplot for Number of Rape Cases:')
plt.ylabel('Values')
plt.xlabel('Rape')

# - - scatter plot
plt.subplot(1, 2, 2)
plt.scatter(data['Year'], data['Women Trafficking'], c = 'violet')
plt.xlabel("Year")
plt.ylabel("Women Trafficking")
plt.title('ScatterPlot showing Women Trafficking Cases:')
plt.tight_layout()

plt.figure(figsize=(10, 5),facecolor = 'grey')

# - - bar chart
plt.subplot(2, 2, 1)
sb.barplot(y = 'Dowry Deaths', x ='Year', data = data)
plt.xticks(rotation = 60)
plt.title('Bar Chart for Number of Dowry Deaths')

# - - histogram
plt.subplot(2, 2, 2)
plt.hist(data['Dowry Deaths'], bins = 5)
plt.title('Histogram showing the Number of Dowry Deaths')
plt.ylabel('Frequency')
plt.xlabel('Values')
plt.tight_layout()

plt.figure(figsize=(10, 5),facecolor = 'white')

# - - pie chart
plt.subplot(1,2,1)
df = data.groupby('Year')[['Women Trafficking', 'Assault against Women']].sum()
plt.pie(df['Women Trafficking'], labels = {2001,2002,2003,2004,2005,2006,2007,2008,2009,
                                           2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,
                                           2020,2021})
plt.title('Crimes Against Women(2001-2021)')

# - - qq plot

plt.figure(figsize=(10, 5),facecolor = 'grey')

plt.subplot(1,2,1)
sst.probplot(data['Insult to Modesty of Women'], plot = plt)
plt.title('QQ Plot on Insult Cases Against Women')
plt.xlabel('Theoretical Quantiles')
plt.ylabel('Sample Quantiles')

plt.show()

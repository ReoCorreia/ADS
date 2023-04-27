#Load the required libraries and data
import seaborn as sns
import pandas as pd

df = pd.read_csv('10 - tips.csv')
print(df)

print("\n\nAggregate Data")
aggrdf = df.groupby('day').agg({'total_bill':['sum'],'tip':['sum'],'size':['sum']})
print(aggrdf)

#Data Visualization
#1) Correlation plot
#sns.heatmap(df.corr())

#2) Boxplot
#sns.boxplot(y=df['total_bill'],data=df)

#3) Lineplot
#sns.lineplot(data=df['total_bill'])

#4) Bar Graph
#sns.barplot(y=df['day'],x=df['total_bill'],data=df,color='b')

#5) Scatterplot
#sns.scatterplot(x=df['total_bill'], y=df["tip"])

#6) Pie Diagram
#plot = aggrdf.plot.pie(y='total_bill', figsize=(5, 5))

#7) Histogram
#hist = df['size'].hist()

#8) Area Plot
#ax = aggrdf.plot.area()

#9) Density Plot
#ad = df['tip'].plot.kde()

#10) Multiple Linear Regression
#g = sns.lmplot(data=df,x="total_bill", y="tip", hue="day")

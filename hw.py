import pandas as pd
import numpy as np

#creating a dataframe from a dictionary
data = pd.read_csv('titanic.csv')
print(data.head())

#Find the mean fare of passengers wrt sex and pclass like ( Male 1st Class Passenger ). Do this for all possible combinations - Total 6 combinations.
grouped_data = data.groupby(['Sex', 'Pclass'])['Fare'].mean()
print(grouped_data)

#Find the mean age of passengers who died wrt sex.
grouped_data = data[data['Survived'] == 0].groupby('Sex')['Age'].mean()
print(grouped_data)

#Find the median age of passengers who died wrt sex.
grouped_data = data[data['Survived'] == 0].groupby('Sex')['Age'].median()
print(grouped_data)

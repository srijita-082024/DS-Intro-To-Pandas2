import pandas as pd

data = pd.read_csv('titanic.csv')

# get a particular column out of a condition
adult_names = data[data['Age'] >= 18]['Name']
print(adult_names)

#slicing a dataframe
slice = data[0:5]
print(slice)

slice2 = data.iloc[0:5]
print(slice2)

#change value in a dataset
data.iloc[0:3,3] = "Srijita Naha"
print(data["Name"])

#save the modified dataset
data.to_csv('titanic_modified.csv', index=False)

#creating new column in the dataset
data["Test"] = data["Fare"] + 2
data["Test2"] = data["Fare"] * data["Pclass"]

#renaming column names
data_renamed = data.rename(columns={"Pclass": "Passenger Class","SibSp": "Siblings/Spouses Aboard"})
print(data_renamed.info())

#performing mathematical operations on multiple columns
print(data["Age"].mean())
print(data[["Age", "Fare"]].mean())

#Get the count of rows in each category
print(data["Pclass"].value_counts())

#sorting the data
data.sort_values(by="Fare", ascending=False, inplace=True)
print(data[["Name", "Fare"]].head())

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

file_name = "pokemon_data.csv"
df = pd.read_csv(file_name)

# print the file
# print(df)

# print the first three row
# print(df.head(3))

# print the last 3 row
# print(df.tail(3))

# print the column 
# print(df.columns)

# print all names
# print(df['Name'])
# print(df.Name)

# specify the number of column 
# print(df['Name'][0:5])

# To get multiple column 
# print(df[['Name','Type 1', 'HP']])

# print out each row
# print(df.iloc[0:4])

# To print row by row
# for index, row in df.iterrows():
#     print(index, row['Name'])

# sorting/Describing data
# print(df.loc[df['Type 1'] == 'Grass'])
# print(df.describe())
# print(df.sort_values('Name', ascending= False))
# print(df.sort_values(['Type 1', 'HP'], ascending= False))
# print(df.sort_values(['Type 1', 'HP'], ascending= [1,0]))

# making changes to the data
# df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed'] 
# df.head(5)
# print(df.head())

# Drop Specific column 
# df = df.drop(columns=['Total'])
# df.head(5)
# print(df.head())

# if 'Total' not in df.columns:
#     print("The 'Total' column does not exist. Adding it now.")
#     df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']

# if 'Total' in df.columns:
#     df = df.drop(columns=['Total'])
# else:
#     print("The 'Total' column does not exist, so it cannot be dropped.")

# print(df.columns)

# Another way to add columns
# df['Total'] = df.iloc[:, 4:10].sum(axis=1)

# To insert column in btw columns
# cols = list(df.columns)
# df = df[cols[0:4] + [cols[-1]] + cols [4:12]]
# df.head(5)
# print(df.head())

# To save new modification into a dataframe
# df.to_csv('modified.csv', index=False)

# Filtering Data
# new_df=df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]


# new_df.reset_index(drop=True, inplace=True)
# print(new_df)
# new_df.to_csv('filtered.csv')

# Allow to and Not allow the name to include mega
# print(df.loc[df['Name'].str.contains('Mega')])
# print(df.loc[~df['Name'].str.contains('Mega')])

# To get fire or grass
# print(df.loc[df['Type 1'].str.contains('Fire|Grass', regex=True)])

# Filter letter that start with pi and the rest set of number can be A-Z
# print(df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)])

# Working with a large amount of dataset
# for df in pd.read_csv('modified.csv', chunksize=5):
#     print('CHUNK DF')
#     print(df)

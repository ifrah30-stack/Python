# 1. Reading CSV
import pandas as pd
df = pd.read_csv('data.csv')

# 2. Data cleaning
df.dropna(inplace=True)

# 3. Filtering rows
df = df[df['status'] == 'Active']

# 4. Grouping data
grouped = df.groupby('department').sum()

# 5. Merging datasets
merged_df = pd.merge(df1, df2, on='id')

# 6. Convert to JSON
df.to_json('output.json', orient='records')

# 7. Rename columns
df.rename(columns={'old': 'new'}, inplace=True)

# 8. Fill missing values
df['salary'].fillna(df['salary'].mean(), inplace=True)

# 9. SQL to DataFrame
import sqlite3
con = sqlite3.connect("company.db")
df = pd.read_sql_query("SELECT * FROM employees", con)

# 10. Excel Export
df.to_excel('output.xlsx', index=False)

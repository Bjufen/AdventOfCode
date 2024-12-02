import pandas as pd

data = pd.read_csv('../../resources/day01.csv')

data['list1'] = data['list1'].sort_values().values
data['list2'] = data['list2'].sort_values().values

total_diff = (data['list1'] - data['list2']).abs().sum()

print("Part 1 (total_diff):", total_diff)


data['occurrence'] = data['list1'].apply(lambda x: (data['list2'] == x).sum())

data['product'] = data['list1'] * data['occurrence']

print("Part 2 (occurrenceSum):", data['product'].sum())

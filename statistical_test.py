import pandas as pd
from scipy import stats
import os

# Load the data
data_path = r'd:\sricharan-A\documents\Apex_Software_solutions\T2\sales_data.csv'
df = pd.read_csv(data_path)

# Filter for the two age groups
group_1 = df[(df['Age'] >= 35) & (df['Age'] <= 44)]['Amount']
group_2 = df[(df['Age'] >= 25) & (df['Age'] <= 34)]['Amount']

# Calculate means
mean_1 = group_1.mean()
mean_2 = group_2.mean()

# Perform T-test
t_stat, p_value = stats.ttest_ind(group_1, group_2, equal_var=False)

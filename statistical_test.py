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

# Confidence interval calculation for the difference in means
diff = mean_1 - mean_2
n1, n2 = len(group_1), len(group_2)
v1, v2 = group_1.var(), group_2.var()
se = ((v1/n1) + (v2/n2))**0.5
conf_level = 0.95
df_welch = ((v1/n1 + v2/n2)**2) / ((v1/n1)**2 / (n1-1) + (v2/n2)**2 / (n2-1))
t_crit = stats.t.ppf((1 + conf_level) / 2, df_welch)
margin_of_error = t_crit * se
conf_int = (diff - margin_of_error, diff + margin_of_error)

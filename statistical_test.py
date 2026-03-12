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

# Results
print(f"--- Hypothesis Testing Results ---")
print(f"Age Group 35-44 Mean AOV: ${mean_1:.2f} (n={n1})")
print(f"Age Group 25-34 Mean AOV: ${mean_2:.2f} (n={n2})")
print(f"Difference in Means: ${diff:.2f}")
print(f"P-value: {p_value:.4f}")
print(f"95% Confidence Interval for Difference: (${conf_int[0]:.2f}, ${conf_int[1]:.2f})")

if p_value < 0.05:
    print("\nConclusion: The difference is statistically significant (p < 0.05).")
    print("Null Hypothesis rejected. Younger and older customer segments exhibit different spending patterns.")
else:
    print("\nConclusion: The difference is NOT statistically significant (p >= 0.05).")
    print("Failed to reject the Null Hypothesis. Spending patterns appear similar across these age groups.")

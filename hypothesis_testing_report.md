# Hypothesis Testing Report: Age-Based Spending Patterns

## 1. Objective
To validate the business intuition that more mature customer segments (Ages 35-44) exhibit higher spending power compared to younger segments (Ages 25-34).

## 2. Methodology
- **Test Type**: Independent Two-Sample T-test (Welch's T-test to account for unequal variances).
- **Metric**: Average Order Value (AOV) per transaction.
- **Hypothesis**:
    - **Null Hypothesis (H₀)**: There is no significant difference in the mean AOV between the 35-44 and 25-34 age groups.
    - **Alternative Hypothesis (H₁)**: The mean AOV for the 35-44 group is significantly higher than that for the 25-34 group.

## 3. Results
| Metric | Age Group 35-44 | Age Group 25-34 |
| :--- | :--- | :--- |
| **Mean AOV** | **$443.12** | **$339.19** |
| **Sample Size (n)** | 213 | 206 |
| **Difference** | **+$103.94** | |

- **P-Value**: **0.0302** (Significant at α=0.05)
- **95% Confidence Interval**: ($10.00, $197.88)

import pandas as pd
from scipy import stats
import os

class AnalysisEngine:
    """
    A class-based engine for performing statistical validation on sales data.
    """
    def __init__(self, data_path):
        self.data_path = data_path
        self.df = None

    def load_data(self):
        self.df = pd.read_csv(self.data_path)

    def perform_t_test(self, age_group_1=(35, 44), age_group_2=(25, 34)):
        group_1 = self.df[(self.df['Age'] >= age_group_1[0]) & (self.df['Age'] <= age_group_1[1])]['Amount']
        group_2 = self.df[(self.df['Age'] >= age_group_2[0]) & (self.df['Age'] <= age_group_2[1])]['Amount']
        
        t_stat, p_value = stats.ttest_ind(group_1, group_2, equal_var=False)
        return group_1, group_2, p_value

    def run_analysis(self):
        self.load_data()
        g1, g2, p = self.perform_t_test()
        print(f"P-value: {p:.4f}")

if __name__ == "__main__":
    path = r'd:\sricharan-A\documents\Apex_Software_solutions\T2\sales_data.csv'
    engine = AnalysisEngine(path)
    engine.run_analysis()

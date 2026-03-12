import pandas as pd
from scipy import stats
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AnalysisEngine:
    """
    A class-based engine for performing statistical validation on sales data.
    """
    def __init__(self, data_path):
        self.data_path = data_path
        self.df = None

    def load_data(self):
        try:
            if not os.path.exists(self.data_path):
                raise FileNotFoundError(f"Data file not found at {self.data_path}")
            self.df = pd.read_csv(self.data_path)
            logger.info("Data loaded successfully.")
        except Exception as e:
            logger.error(f"Failed to load data: {e}")
            raise

    def perform_t_test(self, age_group_1=(35, 44), age_group_2=(25, 34)):
        try:
            group_1 = self.df[(self.df['Age'] >= age_group_1[0]) & (self.df['Age'] <= age_group_1[1])]['Amount']
            group_2 = self.df[(self.df['Age'] >= age_group_2[0]) & (self.df['Age'] <= age_group_2[1])]['Amount']
            
            if group_1.empty or group_2.empty:
                raise ValueError("One or both age groups have no data.")

            t_stat, p_value = stats.ttest_ind(group_1, group_2, equal_var=False)
            logger.info(f"T-test performed. P-value: {p_value:.4f}")
            return group_1, group_2, p_value
        except Exception as e:
            logger.error(f"Error during T-test: {e}")
            raise

    def run_analysis(self):
        try:
            self.load_data()
            g1, g2, p = self.perform_t_test()
            print(f"Analysis Complete. P-value: {p:.4f}")
        except Exception as e:
            logger.critical(f"Analysis failed: {e}")

if __name__ == "__main__":
    path = r'd:\sricharan-A\documents\Apex_Software_solutions\T2\sales_data.csv'
    engine = AnalysisEngine(path)
    engine.run_analysis()

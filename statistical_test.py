import pandas as pd
from scipy import stats
import os
import logging
from typing import Tuple, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AnalysisEngine:
    """
    A class-based engine for performing statistical validation on sales data.
    
    Attributes:
        data_path (str): The absolute path to the input CSV file.
        df (pd.DataFrame, optional): The loaded sales data.
    """
    
    def __init__(self, data_path: str):
        """
        Initializes the AnalysisEngine with a specific data source.
        
        Args:
            data_path (str): Path to the source sales data.
        """
        self.data_path = data_path
        self.df: Optional[pd.DataFrame] = None

    def load_data(self) -> None:
        """
        Loads the sales data from the CSV file into a pandas DataFrame.
        
        Raises:
            FileNotFoundError: If the data file does not exist at the provided path.
            Exception: For other common file read errors.
        """
        try:
            if not os.path.exists(self.data_path):
                raise FileNotFoundError(f"Data file not found at {self.data_path}")
            self.df = pd.read_csv(self.data_path)
            logger.info("Data loaded successfully.")
        except Exception as e:
            logger.error(f"Failed to load data: {e}")
            raise

    def perform_t_test(self, 
                       age_group_1: Tuple[int, int] = (35, 44), 
                       age_group_2: Tuple[int, int] = (25, 34)) -> Tuple[pd.Series, pd.Series, float]:
        """
        Performs a Welch's Two-Sample T-test between two age-defined sub-populations.
        
        Args:
            age_group_1 (Tuple[int, int]): Inclusive range for the first age group.
            age_group_2 (Tuple[int, int]): Inclusive range for the second age group.
            
        Returns:
            Tuple[pd.Series, pd.Series, float]: Group 1 data, Group 2 data, and the T-test p-value.
            
        Raises:
            ValueError: If one or both resultant groups contain no data.
        """
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

    def run_analysis(self) -> None:
        """
        Orchestrates the data loading and statistical analysis workflow.
        """
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

import pandas as pd
from scipy import stats
import os
import logging
import yaml
from typing import Tuple, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AnalysisEngine:
    """
    A class-based engine for performing statistical validation on sales data.
    """
    
    def __init__(self, config_path: str = "config.yaml"):
        """
        Initializes the AnalysisEngine by loading external configurations.
        
        Args:
            config_path (str): Path to the YAML configuration file.
        """
        self.config = self._load_config(config_path)
        self.data_path = self.config['data']['path']
        self.df: Optional[pd.DataFrame] = None

    def _load_config(self, path: str) -> dict:
        """Loads configuration from a YAML file."""
        if not os.path.exists(path):
            # Fallback for demonstration or create default
            return {
                'data': {'path': r'd:\sricharan-A\documents\Apex_Software_solutions\T2\sales_data.csv'},
                'analysis': {'groups': {'group_1': [35, 44], 'group_2': [25, 34]}}
            }
        with open(path, 'r') as f:
            return yaml.safe_load(f)

    def load_data(self) -> None:
        """Loads the sales data from the configured CSV path."""
        try:
            if not os.path.exists(self.data_path):
                raise FileNotFoundError(f"Data file not found at {self.data_path}")
            self.df = pd.read_csv(self.data_path)
            logger.info("Data loaded successfully.")
        except Exception as e:
            logger.error(f"Failed to load data: {e}")
            raise

    def perform_t_test(self) -> Tuple[pd.Series, pd.Series, float]:
        """Performs T-test using configured group ranges."""
        try:
            g1_range = self.config['analysis']['groups']['group_1']
            g2_range = self.config['analysis']['groups']['group_2']
            
            group_1 = self.df[(self.df['Age'] >= g1_range[0]) & (self.df['Age'] <= g1_range[1])]['Amount']
            group_2 = self.df[(self.df['Age'] >= g2_range[0]) & (self.df['Age'] <= g2_range[1])]['Amount']
            
            if group_1.empty or group_2.empty:
                raise ValueError("One or both age groups have no data.")

            t_stat, p_value = stats.ttest_ind(group_1, group_2, equal_var=False)
            logger.info(f"T-test performed. P-value: {p_value:.4f}")
            return group_1, group_2, p_value
        except Exception as e:
            logger.error(f"Error during T-test: {e}")
            raise

    def run_analysis(self) -> None:
        """Orchestrates the analysis workflow."""
        try:
            self.load_data()
            _, _, p = self.perform_t_test()
            print(f"Analysis Complete. P-value: {p:.4f}")
        except Exception as e:
            logger.critical(f"Analysis failed: {e}")

if __name__ == "__main__":
    engine = AnalysisEngine()
    engine.run_analysis()

import pandas as pd
from scipy import stats
import os
import logging
import yaml
from typing import Tuple, Optional, Dict, Any

# Configure logging for professional status updates
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AnalysisEngine:
    """
    A professional class-based engine for performing statistical validation on sales data.
    
    Attributes:
        config (Dict[str, Any]): Configuration parameters loaded from YAML or defaults.
        data_path (str): File path to the source CSV data.
        df (Optional[pd.DataFrame]): The loaded sales data.
    """
    
    def __init__(self, config_path: str = "config.yaml"):
        """
        Initializes the AnalysisEngine by loading external configurations.
        
        Args:
            config_path (str): Absolute or relative path to the YAML configuration file.
        """
        self.config = self._load_config(config_path)
        self.data_path = self.config.get('data', {}).get('path', '')
        self.df: Optional[pd.DataFrame] = None

    def _load_config(self, path: str) -> Dict[str, Any]:
        """
        Loads configuration from a YAML file with a fallback mechanism.
        
        Args:
            path (str): Path to the YAML file.
            
        Returns:
            Dict[str, Any]: A dictionary containing configuration parameters.
        """
        if not os.path.exists(path):
            logger.warning(f"Config file not found at {path}. Using default settings.")
            return {
                'data': {'path': r'sales_data.csv'},
                'analysis': {'groups': {'group_1': [35, 44], 'group_2': [25, 34]}}
            }
        try:
            with open(path, 'r') as f:
                return yaml.safe_load(f) or {}
        except Exception as e:
            logger.error(f"Failed to parse config file: {e}")
            return {}

    def load_data(self, override_path: Optional[str] = None) -> None:
        """
        Loads the sales data from the configured CSV path into a pandas DataFrame.
        
        Args:
            override_path (Optional[str]): If provided, uses this path instead of the config path.
            
        Raises:
            FileNotFoundError: If the data file does not exist.
        """
        path = override_path or self.data_path
        try:
            if not os.path.exists(path):
                raise FileNotFoundError(f"Data file not found at {path}")
            self.df = pd.read_csv(path)
            logger.info("Sales data loaded successfully.")
        except Exception as e:
            logger.error(f"Failed to load data: {e}")
            raise

    def perform_t_test(self) -> Tuple[pd.Series, pd.Series, float]:
        """
        Performs Welch's T-test using configured group ranges from the loaded data.
        
        Returns:
            Tuple[pd.Series, pd.Series, float]: Group 1 Series, Group 2 Series, and the resulting p-value.
            
        Raises:
            ValueError: If the DataFrame is not loaded or if groups have no data.
        """
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")

        try:
            g1_range = self.config['analysis']['groups']['group_1']
            g2_range = self.config['analysis']['groups']['group_2']
            
            group_1 = self.df[(self.df['Age'] >= g1_range[0]) & (self.df['Age'] <= g1_range[1])]['Amount']
            group_2 = self.df[(self.df['Age'] >= g2_range[0]) & (self.df['Age'] <= g2_range[1])]['Amount']
            
            if group_1.empty or group_2.empty:
                raise ValueError("One or both age groups contain no data points for comparison.")

            # Welch's T-Test (equal_var=False) for better robustness
            _, p_value = stats.ttest_ind(group_1, group_2, equal_var=False)
            logger.info(f"Statistical T-test executed. P-value: {p_value:.4f}")
            return group_1, group_2, p_value
        except KeyError as e:
            logger.error(f"Missing configuration key for analysis: {e}")
            raise
        except Exception as e:
            logger.error(f"An unexpected error occurred during T-test: {e}")
            raise

    def run_analysis(self) -> None:
        """
        Convenience method to orchestrate the entire analysis workflow from loading to output.
        """
        try:
            self.load_data()
            _, _, p = self.perform_t_test()
            print(f"--- Analysis Complete ---")
            print(f"Statistical Significance (P-value): {p:.4f}")
            if p < 0.05:
                print("Result: Statistically Significant (Reject Null Hypothesis)")
            else:
                print("Result: Not Statistically Significant (Fail to Reject Null Hypothesis)")
        except Exception as e:
            logger.critical(f"Analysis orchestration failed: {e}")

if __name__ == "__main__":
    engine = AnalysisEngine()
    engine.run_analysis()

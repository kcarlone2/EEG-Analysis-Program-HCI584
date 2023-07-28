import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class DataAnalyzer:
    def __init__(self, file_path):
        """
        Initializes a DataAnalyzer object with the provided file path.

        Args:
            file_path (str): Path to the Excel file containing the data.
        """
        self.file_path = file_path
        self.values_dict = None
        self.lowest_dict = None
        self.highest_dict = None
        
    def is_valid_file(self):
        """
        Checks if the Excel file matches the required format.

        Returns:
            bool: True if the file is valid, False otherwise.
        """
        try:
            excel_data = pd.ExcelFile(self.file_path)
        except Exception as e:
            print(f"Error: {e}")
            return False

        required_sheets = ['Scalars', 'Sim Raw EEG']
        for sheet in required_sheets:
            if sheet not in excel_data.sheet_names:
                print(f"Required sheet '{sheet}' not found")
                return False
        
        scalars_sheet = pd.read_excel(self.file_path, sheet_name='Scalars')
        num_rows, num_cols = scalars_sheet.shape
        if num_rows != 192:
            print(f"Invalid number of rows in 'Scalars' sheet. Expected: 192, Actual: {num_rows}")
            return False
        if num_cols < 3:
            print(f"Invalid number of columns in 'Scalars' sheet. Expected at least 3, Actual: {num_cols}")
            return False
        
        sim_raw_eeg_sheet = pd.read_excel(self.file_path, sheet_name='Sim Raw EEG')
        if 'Pure Coherence' not in sim_raw_eeg_sheet.values:
            print("'Pure Coherence' value not found in 'Sim Raw EEG' sheet")
            return False
            
        print("Everything checks out! You are clear to process the data!")  # CH
        return True
  
    def read_scalars(self, sheet_name_scalar):
        """
        Reads the 'Scalars' sheet from the Excel file and extracts mean frequencies.

        Args:
            sheet_name_scalar (str): Name of the 'Scalars' sheet.

        Returns:
            dict: A dictionary containing channel locations as keys and mean frequencies as values.
        """
        df = pd.read_excel(self.file_path, sheet_name=sheet_name_scalar)
        values_dict = {}
        
        for index, row in df.iterrows():
            if row['Channel'] != '' and row['Value'].startswith('MEAN.'):
                key = df.iloc[index, 0]  # Access the first column for channel name
                value = df.iloc[index, 2]  # Access the second column for the value
                values_dict[key] = value
        
        return values_dict
    

    def plot_mean_frequency(self, output_file=None):
        """
        Plots mean frequencies of different channel locations.

        Args:
            output_file (str): File path to save the plot (optional).
        """
        if self.values_dict is None:
            sheet_name_scalar = 'Scalars'
            self.values_dict = self.read_scalars(sheet_name_scalar)

        # ... (rest of the function remains unchanged)


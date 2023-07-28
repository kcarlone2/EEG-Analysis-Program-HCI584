# EEG-Analysis-Program-HCI584

# User's Guide

This guide will help you understand how to install and use the DataAnalyzer project. DataAnalyzer is a tool designed to analyze data from Excel files and perform various operations, such as plotting mean frequencies and identifying extreme values.

## Table of Contents

1. [Setup](#setup)
2. [How to Use DataAnalyzer](#how-to-use-dataanalyzer)
   - [Step 1: Selecting Data File](#step-1-selecting-data-file)
   - [Step 2: Verifying Data File](#step-2-verifying-data-file)
   - [Step 3: Calculating CZ Theta/Beta Ratio](#step-3-calculating-cz-theta-beta-ratio)
   - [Step 4: Plotting Mean Frequency](#step-4-plotting-mean-frequency)
   - [Step 5: Plotting Extreme Numbers](#step-5-plotting-extreme-numbers)
3. [Handling Errors](#handling-errors)
4. [Caveats and Limitations](#caveats-and-limitations)

## Setup <a name="setup"></a>

Before you begin, ensure that you have the following:

1. Python 3.x installed on your system.
2. Jupyter Notebook or JupyterLab environment (optional but recommended for an interactive experience).
3. The required Python libraries, including pandas, matplotlib, seaborn, and ipyfilechooser.

You can install the required libraries using the following command in your terminal or command prompt:

```bash
pip install pandas matplotlib seaborn ipyfilechooser
```

## How to Use DataAnalyzer <a name="how-to-use-dataanalyzer"></a>

### Step 1: Selecting Data File <a name="step-1-selecting-data-file"></a>

1. Clone or download the DataAnalyzer project repository from GitHub into a folder of your choice.

2. Open your Jupyter Notebook or JupyterLab environment.

3. Import the DataAnalyzer class and the FileChooser widget by executing the following code:

```python
from data_analyzer import DataAnalyzer
from ipyfilechooser import FileChooser
```

4. Use the FileChooser widget to select an Excel file containing your data:

```python
fc = FileChooser('.', filter_pattern=['*.xlsx', '*.xls'], title='Please Select data file')
display(fc)
```

5. A file dialog will appear, allowing you to browse and select the desired Excel file. Click on the file and press "Open" to proceed.

### Step 2: Verifying Data File <a name="step-2-verifying-data-file"></a>

After selecting the data file, the DataAnalyzer class will automatically verify if the Excel file meets the required format.

If the file passes the validation, you will see the message:

```
Everything checks out! You are clear to process the data!
```

Otherwise, if there are any issues with the file, you will see informative error messages explaining what needs to be fixed.

### Step 3: Calculating CZ Theta/Beta Ratio <a name="step-3-calculating-cz-theta-beta-ratio"></a>

Once the data file is verified, you can calculate the CZ Theta/Beta ratio. To do this, execute the following code:

```python
analyzer = DataAnalyzer(fc.selected)
analyzer.calculate_cz_theta_beta_ratio()
```

The CZ Theta/Beta ratio is calculated based on the 'Band Ratios' sheet in the Excel file. The calculated ratio will be displayed, along with insights into whether it falls within the normal range or is indicative of specific brain activities.

### Step 4: Plotting Mean Frequency <a name="step-4-plotting-mean-frequency"></a>

To visualize the mean frequencies of different channel locations, you can use the `plot_mean_frequency` function. Execute the following code:

```python
analyzer.plot_mean_frequency()
```

A plot will be displayed, showing the mean frequencies of channel locations. The plot will be saved as 'mean_frequency_plot.png' in the current directory by default. You can specify a different file name by providing the `output_file` parameter to the function.

### Step 5: Plotting Extreme Numbers <a name="step-5-plotting-extreme-numbers"></a>

You can plot the lowest and highest values from the 'Sim Raw EEG' sheet using the `plot_extreme_numbers` function. Execute the following code:

```python
analyzer.plot_extreme_numbers()
```

The function will create a bar graph with the lowest and highest values. The plot will be saved as 'extreme_numbers_plot.pdf' in the current directory by default. To specify a different file name, use the `output_file` parameter.

## Handling Errors <a name="handling-errors"></a>

If any errors occur during the process, DataAnalyzer will display helpful error messages to guide you on what to do next. The messages will inform you about the nature of the error and the steps needed to address it.

## Caveats and Limitations <a name="caveats-and-limitations"></a>

Please note the following limitations of the DataAnalyzer project:

1. The Excel file must follow the required format with specific sheets and data structures. The `is_valid_file` function verifies the file's structure, and any deviations will result in validation errors.

2. The project is designed to work with specific sheet names and column structures. Modifying the Excel file beyond the supported format may lead to unexpected behavior or errors.

3. The project may not handle certain edge cases, such as exceptionally large or complex data files. Performance issues may arise with substantial data sets.

4. The CZ Theta/Beta ratio calculation is based on specific column labels in the 'Band Ratios' sheet. Any deviations in the column names or structure may cause errors in the calculation.


---

By following this guide, you can successfully install and use the DataAnalyzer project to analyze your data and gain valuable insights. If you encounter any difficulties or have further questions, please consult the "Developer's Documentation" or seek assistance from the project's maintainers. Happy data analysis!

# Developer's Guide

This developer's guide provides an overview of the DataAnalyzer project, aimed at new developers who may need to understand and extend the existing codebase. It covers important aspects of the project, including installation, user flow through the code, known issues, future work, and ongoing development considerations.

## Overview

The DataAnalyzer project is designed to analyze data from an Excel file containing EEG data. It utilizes the pandas library for data handling, matplotlib and seaborn for data visualization, and ipyfilechooser for file selection in Jupyter Notebook. The main goal is to process the data and generate insightful plots related to mean frequencies and extreme numbers.

## Install/Deployment/Admin Issues

Assuming the developer has already followed the User's Guide instructions to install and run the application, there are no additional installation steps required for this developer's guide. However, the following points should be noted:

- **Admin Requirements**: The developer may need administrator privileges to access certain files or configurations on the system.
- **Dependencies**: Ensure that the required Python libraries (pandas, matplotlib, seaborn, and ipyfilechooser) are installed in the environment where the application will run.

## User Interaction and Flow Through the Code ("Walkthrough")

The user interacts with the DataAnalyzer project through a Jupyter Notebook interface. Below is a brief overview of the flow:

1. The user is prompted to select an Excel file using the `ipyfilechooser` widget.
2. The selected file path is verified for the presence of required sheets using the `is_valid_file()` method.
3. If the file is valid, the following tasks are performed:
   - The CZ Theta/Beta ratio is calculated and interpreted using the `calculate_cz_theta_beta_ratio()` method.
   - The mean frequency data is plotted and saved to a file using the `plot_mean_frequency()` method.
   - The extreme numbers (lowest and highest values) are plotted and saved to a file using the `plot_extreme_numbers()` method.

## Known Issues

As of the current version, the following issues are known or suspected:

- **Minor**: None reported.
- **Major**: None reported.
- **Optional**: None reported.

## Future Work

The DataAnalyzer project can be expanded in various ways. Some potential future work includes:

- Adding support for additional data visualization and analysis techniques.
- Implementing more complex EEG signal processing algorithms.
- Enhancing the user interface to provide more interactive features.
- Optimizing data processing algorithms for larger datasets.



import pandas as pd  # put all imports on top 

class Analysis(object):
    '''Functions for data analysis'''
    
    def __init__(self, filename):

        #import data file
        self.data_file = pd.read_excel(filename)
        
        #import Scalars sheet of spreadsheet
        self.mean_db = pd.read_excel(filename, sheet_name = 'Scalars')
        
        #Import Sim Raw EEG sheet of spreadsheet
        self.coh = pd.read_excel(filename, sheet_name = 'Sim Raw EEG')
        
    
    
    #loop thru the “Scalars” sheet within the excel file. It will find the mean frequency 
    # for 20 different channels and store this information in a dictionary:

    def mean_frequency(self):
        '''returns a dict with mean frequencies (what are the keys?)'''

        #initialize dictionary to store mean values
        mean_freq = {}
        
        for i,row in self.mean_db.iterrows(): # loop over all rows i would be the row index)
            v = row["Value"]
            #if v == "MEAN.01": should catch any starting with MEAN
            if v[0:5] == "MEAN.":  # will not catch MEANF
                key = row["Channel"]
                value = row["Raw EEG"]
                mean_freq[key] = value
        return mean_freq

        #loop through the value column within the Scalars sheet and find cells that say "mean.01"
        for x in self.mean_db['Value']: 
            if x == "MEAN.01":
                key = self.mean_db["Channel", x]    #set key as the value in the channel column in the same row as x
                value = self.mean_db["Raw EEG", x]  #set value as the value in the Raw EEG column in the same row as x
                mean_freq[key] = value              #add key:value pair to the dictionary
            else: 
                pass                 
            
        return mean_freq
        
    def low_coherence(self):
        #function will loop thru the “Sim Raw EEG” sheet within the excel file and find the 
        # table regarding pure coherence
        # Within this table, the function will find the 3 lowest numbers and the corresponding
        # sites associated with the numbers. The site:number pairs will be stored in a dictionary
        return None
        
    def high_coherence(self):
        #same as for low but finds highest 3 numbers
        return None
        
    def plot_results(self):
        #This function pull results from the data analysis class and plot the results. For the mean frequency, 
        # it will pull the dictionary and plot the results as a line graph
        # 
        # For the lowest coherence and highest coherence, the results will be plotted as a bar graph
        # All plots will be saved to a file
        return None


# test methods
anlsy = Analysis('Analysis_EO_2022.10.17_13.00.34.xlsx')  
mf = anlsy.mean_frequency()
print(mf)

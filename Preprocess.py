import os 
import sys
import pandas as pd 
from IPython.display import display
import datetime
import timeit
import glob

class PreprocessData:
    program_location = ''
    df_ = pd.DataFrame()
    df_ = df_.fillna(0)
    start = 0.00
    today = timeit.default_timer()
    stop = 0.00
    list_files = []

    def __init__(self):
        self.start = timeit.default_timer()
        self.program_location = os.getcwd()
        self.list_files = (glob.glob(self.program_location +"/*.csv"))
        self.processDir()

    def toDf(self, csv):
        temp_df = pd.read_csv(csv, index_col=False)
        new_df = temp_df.iloc[-1]
        
        self.df_ = self.df_.append(new_df, ignore_index=True)
        self.stop = timeit.default_timer()

    def processDir(self):
        for filepath in self.list_files:
            self.toDf(filepath)
        
        

if __name__ == '__main__':
    run_script = PreprocessData()
    print(run_script.df_)
    

   
import os 
import sys
import pandas as pd 
from IPython.display import display 

class PreprocessData:
    dir_name = ''
    df_ = pd.DataFrame()
    df_ = df_.fillna(0)

    def __init__(self):
        self.dir_name = 'insert/path/todirectory/here'
        self.processDir()
        display(self.df_)

    def toDf(self, csv):
        temp_df = pd.read_csv(csv, index_col=False)
        new_df = temp_df.iloc[-1]
        print(new_df)
        self.df_ = self.df_.append(new_df, ignore_index=True)

    def processDir(self):
        for filename in os.listdir(self.dir_name):
            temp_str = self.dir_name + "/" + filename
            print(temp_str)
            self.toDf(temp_str)

if __name__ == '__main__':
    run_script = PreprocessData()
   
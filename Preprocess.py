import os 
import sys
import pandas as pd 

class PreprocessData:
    dir_name = ''

    def __init__(self):
        self.dir_name = '/Users/abeers/Desktop/ProjectBoom/Test'
        self.processDir()

    def processDir(self):
        for filename in os.listdir(self.dir_name):
            with open(filename, 'rU') as f:
                t = f.read()
                t = t.split()
                print(t)

    # def toDf(self, df):




if __name__ == '__main__':
    run_script = PreprocessData()
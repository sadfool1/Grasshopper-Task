import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import time
import matplotlib.pyplot as plt
from tkinter import *
import tkinter as tk


class Main(tk.Frame):
    pd.set_option('max_columns', 120)
    pd.set_option('max_colwidth', 5000)
    plt.rcParams['figure.figsize'] = (12,8)
    
    
    def __init__ (self):
        
        self.root = Tk()
        self.root.grid()
        self.root.title("Graph Data")
        self.timestamp = None
        
        self.price_analyzer = pd.read_csv(os.path.join(os.path.dirname(__file__), "interview_task.csv"))
        print (self.price_analyzer[1])

        
if __name__ == '__main__':
    try:
        Main() #run the class
        
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

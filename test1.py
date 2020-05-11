import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import time
import matplotlib.pyplot as plt
from tkinter import *
import tkinter as tk
import sys
import traceback
import matplotlib 
matplotlib.use("TkAgg") 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import style
import time



class Main(tk.Frame):
    pd.set_option('max_columns', 120)
    pd.set_option('max_colwidth', 5000)
    plt.rcParams['figure.figsize'] = (12,8)
    
    
    def __init__ (self):
        
        self.root = Tk()
        self.root.grid()
        self.root.title("Graph Data")
        self.root.geometry = ("700x700")
        self.root.resizable = (True, True)
        
        graphframe = LabelFrame (self.root, text = "Price Chart").grid(row = 0, column = 0)
        orderbookframe = LabelFrame (self.root, text = "Orde Book").grid(row = 0, column = 1)
        volumeframe = LabelFrame (self.root, text = "Volume").grid(row = 1, column = 0)

        fig = Figure()
        self.graphcanvas = FigureCanvasTkAgg(fig, master = graphframe)
        self.orderbookcanvas = FigureCanvasTkAgg(fig, master = orderbookframe)
        self.volumecanvas = FigureCanvasTkAgg(fig, master = volumeframe)
        
        self.price_analyzer = pd.read_csv(os.path.join(os.path.dirname(__file__), "interview_task.csv"))
        self.timestamp = None


        

        
        
        
if __name__ == '__main__':
    try:
        Main() #run the class
        
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

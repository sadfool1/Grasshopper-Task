import tensorflow as tf
import numpy as np
import os
import sys
import traceback
import pandas as pd

pd.set_option('max_columns', 120)
pd.set_option('max_colwidth', 5000)

price_analyzer = pd.read_csv(os.path.join(os.path.dirname(__file__), "interview_task.csv"))
print (price_analyzer)
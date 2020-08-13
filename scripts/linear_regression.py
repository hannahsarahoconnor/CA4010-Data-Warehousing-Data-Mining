# https://towardsdatascience.com/linear-regression-in-6-lines-of-python-5e1d0cd05b8d
# First link used didnt work - tried to convert date to float

import os
import pandas as pd # To read data
import numpy as np # To perform calculations
import statsmodels.api as sm
import matplotlib.pyplot as plt # To visualize
import scipy
from sklearn.linear_model import LinearRegression # to perform the linear regression
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_squared_error

# Regression: fit the data to a function
# datasets = os.fsencode("../Datasets")
# for dataset in os.listdir(datasets):
#   # convert filename to str from byte literal & add path ( to read )
#   ds = "../Datasets/" + str(dataset, "utf-8")
df = pd.read_csv("../Datasets/Dublin.csv")
print(df.isnull().sum())
# check for any correlations between variables
corr = df.corr()
print(corr)
print(sns.heatmap(corr))
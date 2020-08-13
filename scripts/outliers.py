import os
import pandas as pd # To read data
import numpy as np # To perform calculations
import statsmodels.api as sm
import matplotlib.pyplot as plt # To visualize
from sklearn.linear_model import LinearRegression # to perform the linear regression
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_squared_error
import scipy
from money_parser import price_dec, price_str

# https://jakevdp.github.io/PythonDataScienceHandbook/05.11-k-means.html

def max_min_prices():
  datasets = os.fsencode("../Datasets")
  for dataset in os.listdir(datasets):
  #   # convert filename to str from byte literal & add path ( to read )
    ds = "../Datasets/" + str(dataset, "utf-8")
    if "Donegal" in ds:
      df = pd.read_csv(ds)
      for index, row in df.iterrows():
        row['price'] = price_str(row['price'])
      df.to_csv(ds,index= False)
    df = pd.read_csv(ds)
    try:
    #  ValueError: could not convert string to float: '\x80220,000.00'
      print('County {:s}; max house price €{:.0f}m; min house price €k'.format(str(dataset, "utf-8").strip('.csv'), float(str(df['price'].max()))))
    except Exception as error:
        print("Error")
        print(ds)
        print("OS error: {0}".format(error))





# max_min_prices()
df = pd.read_csv("../Datasets/Dublin.csv")
sns.boxplot(x=df['price'])
plt.style.use('ggplot')
df = pd.DataFrame(pd.read_csv('../Datasets/Dublin.csv'))

# clustering
# https://blog.floydhub.com/introduction-to-anomaly-detection-in-python/

# Generate a Boxplot
# df['price'].plot(kind='box')
# plt.show()

# df['price'].plot(kind='hist')
# plt.show()

# print('Minimum price ' + str(df['price'].min()))
# print('Maximum price ' + str(df['price'].max()))

# Can we look at the relationship with clustering between area codes & price

# Convert the salary values to a numpy array
raw = df['price'].values
raw_y = df['area_code'].values

# For compatibility with the SciPy implementation
raw = raw.reshape(-1, 1)
raw = raw.astype('float64')
print(raw.shape)
# (106026, 1)
# Specify the data and the number of clusters to kmeans()
centroids, avg_distance = scipy.cluster.vq.kmeans(raw, 10)

# Get the groups (clusters) and distances
groups, cdist = scipy.cluster.vq.vq(raw, centroids)

# (106026, 1) , y = np.arange(0,106026)
plt.scatter(raw, raw_y, c=groups)
# ^ ValueError: x and y must be the same size
plt.xlabel('Prices')
plt.ylabel('Dublin Codes')
plt.show()
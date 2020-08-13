# import os


# files = []
# datasets = os.fsencode("../Datasets")
# for dataset in os.listdir(datasets):
#   ds = "../Datasets/" + str(dataset, 'utf-8')
#   files.append(ds)

# dfs = [pd.read_csv(f) for f in files]
# salesdata = pd.concat(dfs,ignore_index=True)
import pandas as pd
import glob, os
path = "../Datasets"
all_files = glob.glob(path + "/*.csv")
li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)
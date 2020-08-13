import pandas as pd
import os

def split_csv(df):
  for county in df.groupby("GEOGDESC"):
    ed = county[0].replace('/',' ')
    ed = ed.replace(' ','_')
    (county[1]).to_csv("../Datasets/ED/" + county[0] + ".csv", index=False)
    
if __name__ == "__main__":
  # a.encode('utf-8').strip()
  df = pd.read_csv("../Datasets/AllThemesTablesED.csv",encoding="unicode_escape")

  # Step 1 - Split up the csv file per county
  split_csv(df)

  # Step 2 - Removing original large file 
  # os.system("rm ../Datasets/PPR-ALL.csv")

  # Done!
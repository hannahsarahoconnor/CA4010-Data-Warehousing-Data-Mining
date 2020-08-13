import pandas as pd
import numpy as np
import os
import re

# Add functions for validating the values in our datasets

# function for creating a dictionary for all the towns in a file & showing how many/unique values

# Like if a town in the column is correct? 

# If town isnt correct but area code is still there then remove town value

# check if the address has an area code and if not the same, drop

# def town_check(df):
#   # df.groupby("town").values()
#   # for town in df.groupby("town"):
#   # print("______________________________________________________________")
#   # print(df.town.unique())
#   # print("______________________________________________________________")
#   pass

def date_check(df):
  regex="(^(((0[1-9]|1[0-9]|2[0-8])[\/](0[1-9]|1[012]))|((29|30|31)[\/](0[13578]|1[02]))|((29|30)[\/](0[4,6,9]|11)))[\/](19|[2-9][0-9])\d\d$)|(^29[\/]02[\/](19|[2-9][0-9])(00|04|08|12|16|20|24|28|32|36|40|44|48|52|56|60|64|68|72|76|80|84|88|92|96)$)"
  for i in df.index:
    match = re.search(regex,  df.at[i, 'date_of_sale'])
    if match is None:
      # drop the value 
      print(i, df.at[i, 'date_of_sale'])

def spelling_check(df):
  
  spell = SpellChecker()
  for i in df.index:
    address_lst = df.at[i, 'address'].split(', ')
    misspelled = spell.unknown(address_lst)
    for word in misspelled:
      if not(spell.correction == word):
        # drop it

if __name__ == "__main__":
  datasets = os.fsencode("../Datasets")
  for dataset in os.listdir(datasets):
    ds = "../Datasets/" + str(dataset, 'utf-8')
    date_check(pd.read_csv(ds))
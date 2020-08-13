import numpy as np
import pandas as pd
import os
from money_parser import price_str

# Use OOP so we can refer to df everywhere

# Housekeeping stuff

def count_entries():
  total = 0 
  datasets = os.fsencode("../Datasets")
  for dataset in os.listdir(datasets):
    ds = "../Datasets/" + str(dataset, 'utf-8')
    df = pd.read_csv("../Datasets/")
    total += len(df)

  return total

def remove_entries():
  pass

def price_to_float():
  pass

def captialise_value():
  pass

if __name__ == "__main__":
  try:
    datasets = os.fsencode("../Datasets")
    for dataset in os.listdir(datasets):
      ds = "../Datasets/" + str(dataset, 'utf-8')
      # df = pd.read_csv("../Datasets/PPR-ALL.csv", encoding="unicode_escape")
      # Rename the columns - Error with Price ()
      df = pd.read_csv(ds,encoding="utf-8")
      if "Sligo" not in ds:
        if "Kildare" not in ds:
          df.columns = ['date_of_sale','address','postal_code','county','price','not_full_market_price','vat_exclusive','property_description','property_size']
          # Step 1 - Remove entry if NOT full market price

          df = df[df['not_full_market_price'] == 'No']
          
          # Remove the Column as all are now No

          df = df.drop('not_full_market_price', axis=1)

          # Step 2 - Remove captialisation of all addresses so there's no inconsistencies. 

          df['address'] = df['address'].str.lower().str.title()

          # Step 3 - Remove entries with Irish descriptions

          df = df[(df['property_description'] == 'Second-Hand Dwelling house /Apartment') | (df['property_description'] == 'New Dwelling house /Apartment')]

          # Step 4 - Convert the Prices to decimals

          # for index, row in df.iterrows():
          #   row['price'] = price_str(row['price'])
          
          # df["price"] = df.price.astype(float)
          df['price'] = df['price'].apply(lambda x: x.lstrip('\x80'))
          df['price'] = df['price'].apply(lambda x: float(x.split()[0].replace(',', ''))).astype(float)
          
        # Step 5 - Property Size Description Tidy
        
        # TODO The below code throws the error message:

          # FutureWarning: elementwise comparison failed; returning scalar instead, but in the future will perform elementwise comparison
          # result = method(y)

          # if row['property_size'] == "greater than or equal to 38 sq metres and less than 125 sq metres"
          #   row['property_size'] == ">= 38 and < 125"
          
          # elif row['property_size'] == "less than 38 sq metres"
          #   row['property_size'] == "< 38"
          
          # elif row['property_size'] == "greater than 125 sq metres"
          #   row['property_size'] == "> 125"
            
        # Lastly, reset the index for each file & save changes made

          df.reset_index(drop=True)
          df.to_csv(ds)
  except:
    print(ds)
    pass

    # Done!

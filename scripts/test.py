import numpy as np
import pandas as pd
import os
import warnings
import sys
from dublin_dict import dublin_codes
# Add check for each row to ensure that no column entries are blank.

def create_column(column, file):
  pass

def populate_column(column, file):
  pass

def remove_column(column, file):
  pass

if __name__ == "__main__":
  # datasets = os.fsencode("../Datasets")
  # for dataset in os.listdir(datasets):

    # convert filename to str from byte literal & add path ( to read )
    # ds = "../Datasets/" + str(dataset, "utf-8")
    ds = "../Datasets/cattest.csv"
    df = pd.read_csv(ds)
    # Could add a list of towns in each country/create unique words dictionary & check against to see if valid
    # 618	07/05/2013	Lisnamacka, Castleblayney, Co. Monaghan		Monaghan	€10,000.00	No -> Wrong Price: https://www.daft.ie/price-register/monaghan/castleblayney/lisnamacka/equality-guidelines
    try:
      # Code for both Dublin & Others here
      df['town'] = np.nan
      df['town'] = df['town'].fillna("")
      df['area_code'] = np.nan
      df['area_code'] = df['area_code'].fillna("")
      # Default Value for area code will be Co. Dublin"
      #df["area_code"] = df["area_code"].fillna("Co. Dublin")
      for i in df.index:
        print(i)
        address_lst = df.at[i, 'address'].split(', ')
        print(address_lst)
        county_prefixes = ["Co.","Co ","County"]
        prefix_found = [address_lst[-1].find(ele) for ele in county_prefixes if(ele in address_lst[-1])]
        if prefix_found:
          prefix_index = prefix_found[0]
          # Better to return position of the prefix
          # Need to consider: Midleton Co.Cork, for example
          if prefix_index > 0:
            address_lst[-1], leftover = address_lst[-1][:prefix_index], address_lst[-1][prefix_index:]
          else:
            del address_lst[-1]
        if "Dublin" in ds:
          if "Dublin" in address_lst[-1] and len(address_lst[-1]) > 6:
            area_code_index = address_lst[-1].find('Dublin ')
            if area_code_index > 0:
              address_lst[-1], area_code = address_lst[-1][:area_code_index], address_lst[-1][area_code_index:]
              df.at[i, 'area_code'] = area_code
            else:
              df.at[i, 'area_code'] = address_lst[-1]
              del address_lst[-1]
          elif not(pd.isnull(df.at[i,"postal_code"])):
            df.at[i, 'area_code'] = df.at[i, 'postal_code']
          else:
            for k, v in dublin_codes.items():
              # Check if town is present in that list of values
              for town in v:
                if address_lst[-1] in v:
                  df.at[i, 'area_code'] = k
              
          # Add value for town
          if "  " in address_lst[-1]:
            df.at[i, 'town'] = address_lst[-1].split("  ")[1]
          else:
            df.at[i, 'town'] = address_lst[-1]
          del address_lst[-1]
          
          # Update address
          address = ", ".join(address_lst)
          df.at[i, 'address'] = address

        else:
          # "Kilmacow, Curraglass, Conna  Mallow"
          if "  " in address_lst[-1]:
            #set town as mallow
            df.at[i, 'town'] = address_lst[-1].split("  ")[1]
            #change to string
            address = ", ".join(address_lst[:2])
            #killmacow, curraglass
            print("address1" + address)
            address = address + ", " + address_lst[-1].split("  ")[0] + ", " + address_lst[-1].split("  ")[1]
            #killmacow, curraglass, Conna, Mallow
            print("address" + address)
            address_lst = address.split(", ")
            print(address_lst)
          else:
            df.at[i, 'town'] = address_lst[-1]
          del address_lst[-1]
          print("Town = " + df.at[i, 'town'])
          
          # Update address
          address = ", ".join(address_lst)
          df.at[i, 'address'] = address
          print("Updated Address = " + df.at[i, 'address'])
           # Code for everything else here
           # Need to also consider the following cases...
          # "9 Cherrywood  Heights, Bailick Road, Midleton  Co.Cork"
              
              # "3 Clerm Terrace, South Douglas Road" - County City - 2 parts >1 word - county city
              # check for two spaces, could be human errors & meant to be comma. 
              # "Seaveagh, Glaslough" - Glaslough is a village/Town  - 2 parts, last part 1 word = town
              
              # if address_lst[-1] == row["County"]:
              #   # TODO REFACTOR THIS CODE
              #   if len(address_lst) == 3 and not (len(address_lst[-2].split()) > 1):
              #     row["Town"] = address_lst[-2]
              #   else:
              #     row["Town"] = row["County"] + " Town"
              # else:
              #   row["Town"] = address_lst[-1]
    except Exception as error:
      print("Oops!",sys.exc_info()[0],"occured.")
      print(error)

    # Drop Area Code for all other files
    if "Dublin" not in ds:
      df = df.drop('area_code', axis=1)

    # Drop Postal Code for all files
    #df = df.drop('postal_code', axis=1)
    
    # Step 6 - Property Size Description Missing Values

    # Step 7 - Save output to csv files & reset index!
    df.reset_index(drop=True)
    df.to_csv(ds)

    # Move above code to appropriate functions, Refactor & tidy up

    # Done!
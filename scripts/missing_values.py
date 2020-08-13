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
  try:  
    datasets = os.fsencode("../Datasets")
    for dataset in os.listdir(datasets):
    #   # convert filename to str from byte literal & add path ( to read )
      ds = "../Datasets/" + str(dataset, "utf-8")
      df = pd.read_csv(ds)
      df['town'] = np.nan
      df['town'] = df['town'].fillna("")
      df['area_code'] = np.nan
      # Default Value for area code will be Co. Dublin"
      df["area_code"] = df["area_code"].fillna("Co. Dublin")
      for i in df.index:
        address_lst = df.at[i, 'address'].split(', ')
        if "Dublin" in ds:
            # check for town first
          for k, v in dublin_codes.items():
              # Check if town is present in that list of values
            for word in address_lst:
              for town in v:
                if str(town) in word:
                  df.at[i, 'town'] = town
                  df.at[i, 'area_code'] = k
          
          area = df.at[i, 'town']
          if df.at[i,'town'] == "":
            # drop the value
            df = df.drop(index=i)
            print(address_lst)


            # if "Dublin" in address_lst[-1] and len(address_lst[-1]) > 6:
            #   area_code_index = address_lst[-1].find('Dublin ')
            #   if area_code_index > 0:
            #     address_lst[-1], area_code = address_lst[-1][:area_code_index], address_lst[-1][area_code_index:]
            #     df.at[i, 'area_code'] = area_code
            #   else:
            #     df.at[i, 'area_code'] = address_lst[-1]
            #     del address_lst[-1]
            # elif not(pd.isnull(df.at[i,"postal_code"])):
            #   df.at[i, 'adrorea_code'] = df.at[i, 'postal_code']
            # else:
            #   for k, v in dublin_codes.items():
            #     # Check if town is present in that list of values
            #     for town in v:
            #       if v in address_lst:
            #         df.at[i, 'area_code'] = k
            # Add a check for if "Dublin" is in the last par|||||||||||             
            # Add value for town
            # "Kilmacow, Curraglass, Conna  Mallow"
            # Check for if "  " in address:
            # Check if any part of the town is in the dictionary & if so take just that part.
            
            # df.at[i, 'town'] = address_lst[-1]
            # del address_lst[-1]

            # If no area code & match not found in dic - drop it!
            
            # Update address
            # address = ", ".join(address_lst)
            # df.at[i, 'address'] = address

        else:
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
              
          county = df.at[i, 'county']
          #check for 2 spaces (missing ",")
          if "  " in address_lst[-1]:
            #set town as mallow
            df.at[i, 'town'] = address_lst[-1].split("  ")[1]
            address = ", ".join(address_lst[:2])
            address = address + ", " + address_lst[-1].split("  ")[0] + ", " + address_lst[-1].split("  ")[1]
            address_lst = address.split(", ")
            # "27 Browneshill Wood, Browneshill Road, Carlow"  
          if county in address_lst and len(address_lst) > 3: 
            df.at[i, 'town'] = address_lst[-2]
            # "3 Clerm Terrace, South Douglas Road" - County City - 2 parts >1 word - county city
          elif len(address_lst) == 2 and len(address_lst[1]) > 1 and len(address_lst[0]) > 1:
            df.at[i, 'town'] = county
          else:
            df.at[i, 'town'] = address_lst[-1]
            
            # Update address
          address = ", ".join(address_lst)
          df.at[i, 'address'] = address
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
      if "Dublin" not in ds:
        df = df.drop('area_code', axis=1)

      # Drop Postal Code for all files
      # KeyError: "['postal_code'] not found in axis"
      # df = df.drop('postal_code', axis=1)
      
      # Step 6 - Property Size Description Missing Values

      # Step 7 - Save output to csv files & reset index!
      df.reset_index(drop=True)
      df.to_csv(ds,index= False)

  except Exception as error:
    print("Oops!",sys.exc_info()[0],"occured.")
    print(error)

    # Drop Area Code for all other files

    # Move above code to appropriate functions, Refactor & tidy up

    # Done!
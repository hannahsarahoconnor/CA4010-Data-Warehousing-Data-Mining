import pandas as pd
df2 = pd.read_csv('../Datasets/AllThemesTablesED.csv')
for j in df2.index:
    family = []
    try:
      if not pd.isnull(df2.at[j,'GEOGDESC']):
        person_family_2 = df2.at[j,'T4_1_2PF']
        person_family_3 = df2.at[j,'T4_1_3PF']
        person_family_4 = df2.at[j,'T4_1_4PF']
        person_family_5 = df2.at[j,'T4_1_5PF']
        person_family_6 = df2.at[j,'T4_1_GRE_6PF']
        
        a = 0 
        while a < person_family_2:
          family.append(2)
          a += 1
        
        b = 0 
        while b < person_family_3:
          family.append(3)
          b += 1
        c = 0 
        while c < person_family_4:
          family.append(4)
          c += 1

        d = 0 
        while d < person_family_5:
          family.append(5)
          d += 1
        
        e = 0 
        while e < person_family_6:
          family.append(6)
          e += 1
        sum_fam = sum(family)
        len_fam = len(family)
        avg_fam = sum_fam/len_fam
        df2.at[j,'average_family_size'] = avg_fam
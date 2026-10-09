import pandas as pd
import os

#create a sample Dataframe with column names 

data={'Name' :['Alice','Bob','Charlie'],
      'Age':[25,30,35],
      'City':['New Yourk','Los Angels','Chicago']
      }

df=pd.DataFrame(data)


#Adding new row to df for v2

new_row_loc={'Name':'GF1','Age':20,'City':'City1'}
df.loc[len(df.index)]=new_row_loc


#Ensure the "data" directory exists at the root level
data_dir='data'
os.makedirs(data_dir,exist_ok=True)

#define the file path
file_path=os.path.join(data_dir,'sample_data.csv')

#Save the Dataframe to a csv file, including column names
df.to_csv(file_path,index=False)
print(f"csv file saved to {file_path}")
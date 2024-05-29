import json
from pandas import DataFrame

def store_dict(data, filename):
  with open(filename, 'w') as f:
    json.dump(data, f, indent=4) 

def store_df(df: DataFrame, filename):
  df.to_csv(filename, index=True)
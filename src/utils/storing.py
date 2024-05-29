import json
import pickle
from pandas import DataFrame

def store_dict(data, filename):
  with open(filename, 'w') as f:
    json.dump(data, f, indent=4) 

def store_df(df: DataFrame, filename):
  df.to_csv(filename, index=True)

def store_matrix(matrix, filename):
  with open(filename, 'wb') as f:
    pickle.dump(matrix, f)
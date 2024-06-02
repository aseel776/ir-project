import json
import pickle
import scipy.sparse as sp
from pandas import DataFrame

def store_json(data, filename):
  with open(filename, 'w') as f:
    json.dump(data, f, indent=4) 

def store_df(df: DataFrame, filename):
  df.to_csv(filename, index=True)

def store_pkl(data, filename):
  with open(filename, 'wb') as f:
    pickle.dump(data, f)

def store_npz(data, filename):
  sp.save_npz(filename, data)
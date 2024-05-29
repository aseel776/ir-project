import json
import pickle
from pandas import read_csv

def load_dict(filename):
  with open(filename, 'r') as f:
    return json.load(f)

def load_df(filename):
  with open(filename, 'r') as f:
     return read_csv(f)

def load_matrix(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)
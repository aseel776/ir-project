import json
import pickle
import scipy.sparse as sp
from pandas import read_csv

def load_dict(filename):
  with open(filename, 'r') as f:
    return json.load(f)

def load_df(filename):
  with open(filename, 'r') as f:
     return read_csv(f)

def load_matrix_pkl(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)
    
def load_matrix_npz(filename):
  return sp.load_npz(filename)
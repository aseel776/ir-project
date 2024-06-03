import json
import pickle
import scipy.sparse as sp
import numpy as np
from pandas import read_csv

def load_json(filename):
  with open(filename, 'r') as f:
    return json.load(f)

def load_df(filename):
  with open(filename, 'r') as f:
     return read_csv(f)

def load_pkl(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)
    
def load_npz(filename):
  return sp.load_npz(filename)

def load_npy(filename):
   return np.load(filename)
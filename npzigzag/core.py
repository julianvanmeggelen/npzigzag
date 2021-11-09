import pandas as pd
import numpy as np

'''
ZigZag2
Vanilla Numpy implmentation of zigzag indicator.
'''

def pct_change(X):
    data_pct_change = diff(X, 1, None) / shift(X,1, None) 
    return data_pct_change

def shift(arr, num, fill_value=np.nan):
    result = np.empty_like(arr)
    if num > 0:
        result[:num] = fill_value
        result[num:] = arr[:-num]
    elif num < 0:
        result[num:] = fill_value
        result[:num] = arr[-num:]
    else:
        result[:] = arr
    return result

def diff(arr, num, fill_value=np.nan):
    result = np.empty_like(arr)
    if num > 0:
        result[:num] = fill_value
        result[num:] = arr[num:] - arr[:-num]
    elif num < 0:
        result[num:] = fill_value
        result[:num] = arr[:num] - arr[-num:]
    else:
        result[:] = arr
    return result

def calczigzag(X, pc, include_first):

    data_pct_change = pct_change(X)
    pct_change_mask = np.sign(data_pct_change)
    pct_change_mask_abs_diff = np.abs(diff(pct_change_mask,1,np.nan))
    split_mask = np.where(pct_change_mask_abs_diff == 2)[0] - 1
    
    data_split_pct_change = pct_change(X[split_mask])

    data_split_pct_change_filtered_indices = np.where(np.abs(data_split_pct_change) > pc)
    data_split_pct_change_filtered = data_split_pct_change[data_split_pct_change_filtered_indices]
    pivot_indices = split_mask[data_split_pct_change_filtered_indices]
    pivot_indices_filtered = pivot_indices[diff(np.sign(data_split_pct_change_filtered),-1,None)!= 0]
    if include_first:
        pivot_indices_filtered = np.concatenate(([0],pivot_indices_filtered))
        
    return pivot_indices_filtered

def zigzag(X, pc, include_first = True):
    '''
    X: numpy.ndarray/list/pandas.core.series.Series
        Data
    pc: float
        Precision level
    include_first: bool
        Boolean indicating whether to include the first observation as a pivot point
    '''

    if type(X) is np.ndarray:
        pivot_indices = calczigzag(X, pc, include_first)
        return pivot_indices

    elif type(X) is pd.Series:
        X_np = X.values 
        X_index = X.index
        pivot_indices = calczigzag(X_np, pc, include_first)
        return X_index[pivot_indices]

    elif type(X) is list:
        X_np = np.array(X)
        pivot_indices = calczigzag(X_np, pc, include_first)
        return pivot_indices
    
    else:
        raise ValueError("X should be pd.series, np.array or list")



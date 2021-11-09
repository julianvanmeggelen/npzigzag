# npzigzag
This is a simple numpy implementation of a zigzag indicator.

## Usage
```python
pip install npzigzag
```
```python
from npzigzag import core as zz
```
This package has one method:\
core.zigzag(X, pc, include_first = True)

Parameters:
* X: *pd.Series or np.ndarray or list* 
    * Main data to compute the indicator on.
* pc: *float*
    * Percentage change treshold. This indicates the minimum jump the timeseries has to make before a pivot is recognized in the zigzag indicator.
* include_first: *bool*
    * Indicates wether or not to add the first observation of X as a pivot point,

Returns:
* pivot_indices: *np.ndarray* if X is *np.ndarray* or *list*, *pd.Int64Index* if X is *pd.Series*
    * Array with indices of zigzag pivot points.

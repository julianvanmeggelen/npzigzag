# npzigzag
This is a simple numpy implementation of a zigzag indicator.

## Usage
```python
pip install npzigzag
```
```python
from npzigzag import core as zz
```
This package has one method:
### core.zigzag(X, pc, include_first = True)

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

### Example:

```python
from npzigzag import core as zz
import numpy as np

X = np.cumprod(1 + np.random.randn(100)/100)
zz_pivots = zz.zigzag(X,0.02, False)

plt.plot(X, '--')
plt.plot(zz_pivots, X[zz_pivots])
plt.scatter(zz_pivots, X[zz_pivots])
```
Ouputs:

![Plot]
(https://github.com/julianvanmeggelen/npzigzag/zz.png)


from pandas.core.dtypes.common import pandas_dtype
from pycylon import CylonContext
from pycylon import DataFrame
from pycylon.indexing.index import BaseArrowIndex
from pprint import pprint
import numpy as np

#pandas->core->indexes->base->astype()

df1 = DataFrame({'a': ['foo', 'bar'], 'b': [1, 2]})
"""
dtype="int32"

#pprint(vars(df1.index))

if dtype is not None:
    dtype = pandas_dtype(dtype)
    print(dtype)
casted = df1.index.values.astype(dtype, copy=True)

print(df1.index)
print(df1.index.values)
print(casted)

bArrow= BaseArrowIndex(casted, dtype=dtype)

#print(bArrow.values)


ct = df1.iloc[0:0]  # returns table (head)
cdf = DataFrame(ct.to_arrow()) #cdf is empty df
print(cdf)
print(cdf.index)
#print(cdf.index.dtype) #not handled for empty df

print('barrow:',bArrow)
print(bArrow.values)

"""

print(df1.index)
df1.set_index([i for i in range(2)])
print(df1.index)
print(df1.index.get_index_array().to_numpy())
print(df1.index.bindex_shd_ptr.get().GetIndexArray())
empty_index_dtype = np.int32
#df1.index =df1.index.astype(empty_index_dtype)
bArrowIndex = df1.index.astype(empty_index_dtype)
print(bArrowIndex)
print(bArrowIndex.values)
#df1.set_index(bArrowIndex)
#out.index.astype(empty_index_dtype)







#from pycylon import Table
from pycylon import CylonContext
from pycylon import DataFrame

ctx: CylonContext = CylonContext(config=None, distributed=False)

d3 = {'col-0': [1, 2, 3], 'col-1': [4, 5, 6]}
cdf3 = DataFrame(d3)

cdf3.set_index([0,1,2]) #[0,1,num_rows-1]


print(cdf3.iloc[0:1]) #returns table

print(cdf3._table.index)

cdf3.shuffle(cdf3.columns)
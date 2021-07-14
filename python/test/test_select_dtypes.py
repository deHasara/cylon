from typing import List, FrozenSet

import pycylon
from pandas.core.dtypes.common import infer_dtype_from_object
from pycylon import CylonContext
from pycylon import DataFrame


import numpy as np

ctx: CylonContext = CylonContext(config=None, distributed=False)

df = {'col-1': [True, False, False], 'col-2':{'a', 'b', 'c'}}

cdf = DataFrame(df)
cdf.set_index([i for i in range(3)])

print("cdf index dtype:", type(cdf.index.values[0]))

print(cdf.dtypes)

print('###')
print(cdf.select_dtypes(include=['int64', 'object'], exclude=['bool'])) #include given priority
print('###')
print(cdf.select_dtypes(include=['int64', 'object'])) #only object type inside df, no int64
print('###')
print(cdf.select_dtypes(exclude=['bool'])) #all columns except bool type returned
print('###')
print(cdf.select_dtypes(exclude=['int64'])) #no int64 in df, so all columns returned
print('###')
print(cdf.select_dtypes(include=['int64'])) #empty selection, not handled by cylon

'''
infer_dtype_from_object(getattr(np, 'int64'))
dtypes = cdf.dtypes
unique_set = set(dtypes.values())
unique_dtypes = np.array(list(unique_set), dtype=object)

print(unique_dtypes, type(unique_dtypes))

include=()#['category']#()#['int64', 'object'] #['category']
exclude=['category']#['bool']
include = frozenset(infer_dtype_from_object(x) for x in include)
exclude = frozenset(infer_dtype_from_object(x) for x in exclude)

print('frozen set:',include)

def extract_unique_dtypes_from_dtypes_set(dtypes_set: FrozenSet[np.generic], unique_dtypes: np.ndarray) -> List[np.generic]:
    extracted_dtypes = [
                    unique_dtype
                    for unique_dtype in unique_dtypes
                    # error: Argument 1 to "tuple" has incompatible type
                    # "FrozenSet[Union[ExtensionDtype, str, Any, Type[str],
                    # Type[float], Type[int], Type[complex], Type[bool]]]";
                    # expected "Iterable[Union[type, Tuple[Any, ...]]]"
                    if issubclass(
                        #here no need to put unique_dtypes.type -> already gets type
                        unique_dtype, tuple(dtypes_set)  # type: ignore[arg-type]
                    )
                ]
    return extracted_dtypes


if include:
    included_dtypes = extract_unique_dtypes_from_dtypes_set(include, unique_dtypes)
    print('included_dtypes:', included_dtypes)
    extracted_columns = [
        column
        for column, dtype in cdf.dtypes.items()
        if dtype in included_dtypes
    ]


if exclude:
    if include: #include given priority always
        pass
    else:
        excluded_dtypes = extract_unique_dtypes_from_dtypes_set(exclude, unique_dtypes)
        print('excluded dtypes:', excluded_dtypes)
        extracted_columns = [
            column
            for column, dtype in cdf.dtypes.items()
            if dtype not in excluded_dtypes
        ]

print(extracted_columns)
if extracted_columns:
    print(cdf.iloc[:,extracted_columns])
else:
    raise NotImplementedError('not handled empty data frames')
'''


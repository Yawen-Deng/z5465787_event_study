""" lec_pd_series.py

Companion codes for the lecture on pandas Series
"""

import pandas as pd


# ---------------------------------------------------------------------------- 
#   The dates and prices lists
# ---------------------------------------------------------------------------- 
dates = [
  '2020-01-02', 
  '2020-01-03',
  '2020-01-06',
  '2020-01-07',
  '2020-01-08',
  '2020-01-09',
  '2020-01-10',
  '2020-01-13',
  '2020-01-14',
  '2020-01-15',
  ]

prices = [
  7.1600, 
  7.1900,
  7.0000,
  7.1000,
  6.8600,
  6.9500,
  7.0000,
  7.0200,
  7.1100,
  7.0400,
  ]

# ----------------------------------------------------------------------------
#   Create a Series instance
# ----------------------------------------------------------------------------
# Create a series object
ser = pd.Series(data=prices, index=dates)
print(ser)

# Output:
#  2020-01-02    7.16
#  2020-01-03    7.19
#  2020-01-06    7.00
#  2020-01-07    7.10
#  2020-01-08    6.86
#  2020-01-09    6.95
#  2020-01-10    7.00
#  2020-01-13    7.02
#  2020-01-14    7.11
#  2020-01-15    7.04
#  dtype: float64

# Select Qantas price on '2020-01-02' ($7.16) using ...

# ... the `prices` list
prc0 = prices[dates.index('2020-01-02')]
print(prc0)

# ... the `ser` series
prc1 = ser['2020-01-02']
print(prc1)

# ----------------------------------------------------------------------------
#   Slicing series
# ----------------------------------------------------------------------------
# Unlike dictionaries, you can slice a series
prcs = ser['2020-01-06':'2020-01-10']

print(prcs)

# Output:
#  2020-01-06    7.00
#  2020-01-07    7.10
#  2020-01-08    6.86
#  2020-01-09    6.95
#  2020-01-10    7.00
#  dtype: float64

# ----------------------------------------------------------------------------
#   Accessing the underlying array
# ----------------------------------------------------------------------------

# Use `.array` to get the underlying data array
ary = ser.array
print(ary)

# Output:
#  <PandasArray>
#  [7.16, 7.19, 7.0, 7.1, 6.86, 6.95, 7.0, 7.02, 7.11, 7.04]
#  Length: 10, dtype: float64

# Like any instance, you can get its type (i.e., the class used to create the
# instance)
type(ser.array)

# Output:
#  <class 'pandas.core.arrays.numpy_.PandasArray'>

# Use the `index` attribute to get the index from a series
the_index = ser.index
print(the_index)

# Output:
# Index(['2020-01-02', '2020-01-03', '2020-01-06', '2020-01-07', '2020-01-08',
#    '2020-01-09', '2020-01-10', '2020-01-13', '2020-01-14', '2020-01-15'],
#   dtype='object')

# Like any instance, you can get its type (i.e., the class used to create the
# instance).
print('The type of `the_index` is', type(the_index))

# Output:
# The type of `the_index` is <class 'pandas.core.indexes.base.Index'>

# ----------------------------------------------------------------------------
#   Changing the index by assignment
# ----------------------------------------------------------------------------

# The old index is:
#
# Index(['2020-01-02', '2020-01-03', '2020-01-06', '2020-01-07', '2020-01-08',
#    '2020-01-09', '2020-01-10', '2020-01-13', '2020-01-14', '2020-01-15'],
#   dtype='object')

# Replace the existing index with another with different values
ser.index = [0, 1, 2, 3, -4, 5, 6, 7, 8, 1000] # Note the -4 and 1000

# The new index is:
# Int64Index([0, 1, 2, 3, -4, 5, 6, 7, 8, 1000], dtype='int64')
print(ser.index)

# Lets see how the series looks like
print(ser)

# Output:
#  0       7.16
#  1       7.19
#  2       7.00
#  3       7.10
# -4       6.86
#  5       6.95
#  6       7.00
#  7       7.02
#  8       7.11
#  1000    7.04
# dtype: float64

# ----------------------------------------------------------------------------
#   Selecting obs using the new index
# ----------------------------------------------------------------------------
# Lets see how the series looks like
print(ser)

# Output:
#  0       7.16
#  1       7.19
#  2       7.00
#  3       7.10
# -4       6.86
#  5       6.95
#  6       7.00
#  7       7.02
#  8       7.11
#  1000    7.04
# dtype: float64

# This will return 7.04
x = ser[1000]
print(x)

# Compare the following cases:
# 1. This will return the element associated with the index label -4
#    (or 6.86)
print(ser[-4])

# 2. This will return the fourth element from the end of the **list** `prices`
#    (or 7.00)
print(prices[-4])
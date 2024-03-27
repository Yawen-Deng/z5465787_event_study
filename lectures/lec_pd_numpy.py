""" lec_pd_numpy.py

Companion code for the lecture on Numpy
"""

import numpy as np
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

# Trading day counter
bday = [
  1,
  2,
  3,
  4,
  5,
  6,
  7,
  8,
  9,
  10]

# ----------------------------------------------------------------------------
#   Create two series
# ----------------------------------------------------------------------------

# Series with prices
prc_ser = pd.Series(data=prices, index=dates)

# Series with trading day
bday_ser = pd.Series(data=bday, index=dates)


# ----------------------------------------------------------------------------
#   Create a dataframe
# ----------------------------------------------------------------------------
# Data Frame with close and Bday columns
df = pd.DataFrame({'Close': prc_ser, 'Bday': bday_ser})
print(df)
# Out:
#              Close  Bday
#  2020-01-02   7.16     1
#  2020-01-03   7.19     2
#  2020-01-06   7.00     3
#  2020-01-07   7.10     4
#  2020-01-08   6.86     5
#  2020-01-09   6.95     6
#  2020-01-10   7.00     7
#  2020-01-13   7.02     8
#  2020-01-14   7.11     9
#  2020-01-15   7.04    10

# Print a concise summary of the object
df.info()
# Returns something like this:
#  <class 'pandas.core.frame.DataFrame'>
#  Index: 10 entries, 2020-01-02 to 2020-01-15
#  Data columns (total 2 columns):
#   #   Column  Non-Null Count  Dtype
#  ---  ------  --------------  -----
#   0   Close   10 non-null     float64
#   1   Bday    10 non-null     int64
#  dtypes: float64(1), int64(1)
#  memory usage: 240.0+ bytes


# Get the series containing "Close" prices
ser = df['Close']

# Get the underlying data array
print(ser.array)
# Returns:
#  <PandasArray>
#  [7.16, 7.19, 7.0, 7.1, 6.86, 6.95, 7.0, 7.02, 7.11, 7.04]
#  Length: 10, dtype: float64

# and the type
print(type(ser.array))
# Output:
#  <class 'pandas.core.arrays.numpy_.PandasArray'>

# The .values attribute will give you a numpy array
# with the contents of the series
print(ser.values)
# Output:
#  array([7.16,7.19,7.0,7.1,6.86,6.95,7.,7.02,7.11,7.04])

# The type is <class 'numpy.ndarray'>
print(type(ser.values))   # --> <class 'numpy.ndarray'>


# ----------------------------------------------------------------------------
#   Working with missing data
# ----------------------------------------------------------------------------

# Add an empty row to the `df` dataframe
# Create a copy
df_nan = df.copy()

# Add an emtpy row to the `df_nan` dataframe
df_nan.loc['3000-01-01'] = [np.nan, np.nan]
print(df_nan)
# Returns:
#             Close  Bday
# 2020-01-02   7.16   1.0
# 2020-01-03   7.19   2.0
# 2020-01-06   7.00   3.0
# 2020-01-07   7.10   4.0
# 2020-01-08   6.86   5.0
# 2020-01-09   6.95   6.0
# 2020-01-10   7.00   7.0
# 2020-01-13   7.02   8.0
# 2020-01-14   7.11   9.0
# 2020-01-15   7.04  10.0
# 3000-01-01    NaN   NaN

# Note that the dtypes changed
print("\nThis is the `df` dataframe:")
print(df.info())
# Returns:
#   This is the `df` dataframe:
#   <class 'pandas.core.frame.DataFrame'>
#   Index: 10 entries, 2020-01-02 to 2020-01-15
#   Data columns (total 2 columns):
#    #   Column  Non-Null Count  Dtype
#   ---  ------  --------------  -----
#    0   Close   10 non-null     float64
#    1   Bday    10 non-null     int64
#   dtypes: float64(1), int64(1)

print("\nThis is the `df_nan` dataframe:")
print(df_nan.info())
# Returns:
#   This is the `df_nan` dataframe:
#   <class 'pandas.core.frame.DataFrame'>
#   Index: 11 entries, 2020-01-02 to 3000-01-01
#   Data columns (total 2 columns):
#    #   Column  Non-Null Count  Dtype
#   ---  ------  --------------  -----
#    0   Close   10 non-null     float64
#    1   Bday    10 non-null     float64
#   dtypes: float64(2)


# Convert dtypes
df_new = df_nan.convert_dtypes()
print(df_new.info())
# Returns
#   Data columns (total 2 columns):
#    #   Column  Non-Null Count  Dtype
#   ---  ------  --------------  -----
#    0   Close   10 non-null     float64
#    1   Bday    10 non-null     Int64
#   dtypes: Int64(1), float64(1)

print(df_new.loc['3000-01-01'])
# Returns:
#   Close    <NA>
#   Bday     <NA>

print(type(df_new.loc['3000-01-01', 'Bday']))


# ----------------------------------------------------------------------------
#   The df.info method
# ----------------------------------------------------------------------------

data = {
     'col_a': [1, 2, 3],
     'col_b': [10.0, None, 13.0],
     }


# First a data frame without a user-defined index
df0 = pd.DataFrame(data)
print('\nprint(df0) -->')
print(df0)
print('\ndf0.info() --> ')
df0.info()


# A data frame with a strings as index labels
idx = ['2020-01-01', '2020-01-02', '2020-01-03']
df1 = pd.DataFrame(data, index=idx)
print('\nprint(df1) -->')
print(df1)
print('\ndf1.info() --> ')
df1.info()


# A data frame with a datetime objs as index labels
idx_dt = pd.to_datetime(idx)
df2 = pd.DataFrame(data, index=idx_dt)
print('\nprint(df2) -->')
print(df2)
print('\ndf2.info() --> ')
df2.info()
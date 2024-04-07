""" lec_pd_datetime.py

Companion codes for the lecture on working with time-series data in Pandas
"""
import os
import datetime as dt

import pandas as pd

import toolkit_config as cfg

CSVLOC = os.path.join(cfg.DATADIR, 'tsla_prc.csv')


# ----------------------------------------------------------------------------
# The datetime class:
#   Implements several methods to generate instances of `datetime`
#   representing a certain date
# ----------------------------------------------------------------------------

# One of the methods implemented by `dt.datetime` is called `now`, which
# returns an instance of `dt.datetime` representing the current date/time.

# Instance of `dt.datetime` with the current date/time
dt_now = dt.datetime.now()

# This will produce a string representing the date/time in `dt_now`
print(dt_now)

# This will confirm that `dt_now` is an instance of the `datetime` class
print(type(dt_now))  # --> <class 'datetime.datetime'>


# From the `print` statement above, we can see that instances of `datetime`
# store the date (year, month, day) and time (hour, minute, second,
# microsecond). You can access these attributes directly from the instance:
s = 'Date in day/month/year format is: {}/{}/{} '.format(dt_now.day, dt_now.month, dt_now.year)
print(s)
# Output (assuming the Aug 21, 2021 date above):
#   Date in day/month/year format is: 21/8/2021


# ----------------------------------------------------------------------------
#   Comparing `repr` and `print` (datetime instances)
# ----------------------------------------------------------------------------
# String representing the data included in the object
print(dt_now)
# Output:
# 2021-08-21 13:24:27.283311

# This will give you a string representing how the instance could be
# constructed
print(repr(dt_now))
# Output:
#   datetime.datetime(2021, 8, 21, 13, 24, 27, 283311)


# Create another datetime instance with value 2021-08-21 13:24:27.283311
a_little_ago = dt.datetime(
    year=2021,
    month=8,
    day=21,
    hour=13,
    minute=27,
    second=1, microsecond=283311)
print(a_little_ago)
# Output:
# 2021-08-21 13:24:27.283311


# Note that we don't have to pass all arguments
dt_other = dt.datetime(
    year=2021,
    month=8,
    day=21,
    )
print(dt_other)
# Output:
# 2021-08-21 00:00:00


# ----------------------------------------------------------------------------
#   `datetime.timedelta` objects
# ----------------------------------------------------------------------------

# Lets create two other datetime instances
dt0 = dt.datetime(year=2019, month=12, day=31)
dt1 = dt.datetime(year=2020, month=1, day=1)

# Operations between datetime objects will return timedelta objects
delta = dt1 - dt0

print(delta)
# Output:
# 1 day, 0:00:00

print(repr(delta))
# Output:
# datetime.timedelta(days=1)


# These two dates are 12 hours apart
t1 = dt.datetime(year=2020, month=12, day=31, hour=12)
t2 = dt.datetime(year=2020, month=12, day=31, hour=0)

new_delta = t1 - t2

print(new_delta)
# Output:
# 12:00:00


# Add 12 hours to some date
#   - `start` will be the starting date
#   - `delta` will be a period of 12 hours
#   - `end` will be the ending date

start = dt.datetime(year=2020, month=12, day=31, hour=0)
delta = dt.timedelta(hours=12)

# This is the new date
end = start + delta

print(start)
# Output:
#   2020-12-31 00:00:00

print(end)
# Output:
#   2020-12-31 12:00:00


# ----------------------------------------------------------------------------
#   The `strftime` method
# ----------------------------------------------------------------------------

# | Directive | Meaning                                                       | Example                  |
# |-----------|---------------------------------------------------------------|--------------------------|
# | %a        | Weekday as locale's abbreviated name.                         | Sun, Mon,...             |
# | %A        | Weekday as locale's full name.                                | Sunday, Monday,...       |
# | %w        | Weekday as a decimal number (Sunday=0,Saturday=6)             | 0, 1,..., 6              |
# | %d        | Day of the month as a zero-padded decimal number.             | 01, 02, …, 31            |
# | %b        | Month as locale's abbreviated name.                           | Jan, Feb,..., Dec        |
# | %B        | Month as locale's full name.                                  | January, February,...    |
# | %m        | Month as a zero-padded decimal number.                        | 01, 02, …, 12            |
# | %y        | Year without century as a zero-padded decimal number.         | 00, 01,..., 99           |
# | %Y        | Year with century as a decimal number.                        | 0001, 1999, 2013, 2014   |
# | %H        | Hour (24-hour clock) as a zero-padded decimal number.         | 00, 01, …, 23            |
# | %I        | Hour (12-hour clock) as a zero-padded decimal number.         | 01, 02, …, 12            |
# | %p        | Locale's equivalent of either AM or PM.                       | AM, PM                   |
# | %M        | Minute as a zero-padded decimal number.                       | 00, 01, …, 59            |
# | %S        | Second as a zero-padded decimal number.                       | 00, 01, …, 59            |
# | %j        | Day of the year as a zero-padded decimal number.              | 001, 002, …, 366         |
# | %U        | Week number of the year (Sunday as the first day of the week) | 00, 01, …, 53            |
# | %W        | Week number of the year (Monday as the first day of the week) | 00, 01, …, 53            |
# | %c        | Locale's appropriate date and time representation.            | Tue Aug 16 21:30:00 1988 |

# Create a datatime object
date = dt.datetime(year=2020, month=12, day=31, hour=0)

# Create a string with the representation we want:
s = date.strftime('%Y-%m-%d')
print(s)
# Output:
#  '2020-12-31'


# ----------------------------------------------------------------------------
#   Time series with Pandas
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
#   Load the data into a dataframe
# ----------------------------------------------------------------------------
prc = pd.read_csv(CSVLOC)
print(prc)
# Output:
#             Date        Open        High  ...       Close   Adj Close    Volume
# 0     2010-06-29    3.800000    5.000000  ...    4.778000    4.778000  93831500
# 1     2010-06-30    5.158000    6.084000  ...    4.766000    4.766000  85935500
# 2     2010-07-01    5.000000    5.184000  ...    4.392000    4.392000  41094000
# 3     2010-07-02    4.600000    4.620000  ...    3.840000    3.840000  25699000
# 4     2010-07-06    4.000000    4.000000  ...    3.222000    3.222000  34334500
# ...          ...         ...         ...  ...         ...         ...       ...
# 2640  2020-12-22  648.000000  649.880005  ...  640.340027  640.340027  51716000
# 2641  2020-12-23  632.200012  651.500000  ...  645.979980  645.979980  33173000
# 2642  2020-12-24  642.989990  666.090027  ...  661.770020  661.770020  22865600
# 2643  2020-12-28  674.510010  681.400024  ...  663.690002  663.690002  32278600
# 2644  2020-12-29  661.000000  669.900024  ...  665.989990  665.989990  22910800
#
# [2645 rows x 7 columns]

prc.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 2645 entries, 0 to 2644
# Data columns (total 7 columns):
#  #   Column     Non-Null Count  Dtype
# ---  ------     --------------  -----
#  0   Date       2645 non-null   object
#  1   Open       2645 non-null   float64
#  2   High       2645 non-null   float64
#  3   Low        2645 non-null   float64
#  4   Close      2645 non-null   float64
#  5   Adj Close  2645 non-null   float64
#  6   Volume     2645 non-null   int64
# dtypes: float64(5), int64(1), object(1)
# memory usage: 144.8+ KB

# 'Date' is a column of strings with dates.
print(prc.loc[:, 'Date'])
# Output:
# 0       2010-06-29
# 1       2010-06-30
# 2       2010-07-01
# 3       2010-07-02
# 4       2010-07-06
#            ...
# 2640    2020-12-22
# 2641    2020-12-23
# 2642    2020-12-24
# 2643    2020-12-28
# 2644    2020-12-29
# Name: Date, Length: 2645, dtype: object

# The index is just a counter
print(prc.index)
# Output:
# RangeIndex(start=0, stop=2645, step=1)


# ----------------------------------------------------------------------------
#   The `to_datetime` method
# ----------------------------------------------------------------------------
# Compare these two cases:

# prc['Date'] is a series
dser = pd.to_datetime(prc['Date'], format='%Y-%m-%d')
print(dser)
# Output:
# 0      2010-06-29
# 1      2010-06-30
# 2      2010-07-01
# 3      2010-07-02
# 4      2010-07-06
#           ...
# 2640   2020-12-22
# 2641   2020-12-23
# 2642   2020-12-24
# 2643   2020-12-28
# 2644   2020-12-29
# Name: Date, Length: 2645, dtype: datetime64[ns]


# prc['Date'].array is a pandas array
didx = pd.to_datetime(prc['Date'].array, format='%Y-%m-%d')
print(didx)
# Output:
# DatetimeIndex(['2010-06-29', '2010-06-30', '2010-07-01', '2010-07-02',
#                '2010-07-06', '2010-07-07', '2010-07-08', '2010-07-09',
#                '2010-07-12', '2010-07-13',
#                ...
#                '2020-12-15', '2020-12-16', '2020-12-17', '2020-12-18',
#                '2020-12-21', '2020-12-22', '2020-12-23', '2020-12-24',
#                '2020-12-28', '2020-12-29'],
#               dtype='datetime64[ns]', length=2645, freq=None)

# Convert the elements in the Date column
prc.loc[:, 'Date'] = pd.to_datetime(prc['Date'], format='%Y-%m-%d')
prc.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 2645 entries, 0 to 2644
# Data columns (total 7 columns):
#  #   Column     Non-Null Count  Dtype
# ---  ------     --------------  -----
#  0   Date       2645 non-null   datetime64[ns]
#  1   Open       2645 non-null   float64
#  2   High       2645 non-null   float64
#  3   Low        2645 non-null   float64
#  4   Close      2645 non-null   float64
#  5   Adj Close  2645 non-null   float64
#  6   Volume     2645 non-null   int64
# dtypes: datetime64[ns](1), float64(5), int64(1)


# ----------------------------------------------------------------------------
#   Setting the index
# ----------------------------------------------------------------------------
# Using the .set_index method
another_df = prc.set_index('Date')
another_df.info()
# <class 'pandas.core.frame.DataFrame'>
# DatetimeIndex: 2645 entries, 2010-06-29 to 2020-12-29
# Data columns (total 6 columns):
#  #   Column     Non-Null Count  Dtype
# ---  ------     --------------  -----
#  0   Open       2645 non-null   float64
#  1   High       2645 non-null   float64
#  2   Low        2645 non-null   float64
#  3   Close      2645 non-null   float64
#  4   Adj Close  2645 non-null   float64
#  5   Volume     2645 non-null   int64
# dtypes: float64(5), int64(1)
# memory usage: 144.6 KB

# Override the variable with another dataframe
# prc = prc.set_index('Date')
# Or use the `inplace` argument:
# (recommended)
prc.set_index('Date', inplace=True)
prc.info()
# <class 'pandas.core.frame.DataFrame'>
# DatetimeIndex: 2645 entries, 2010-06-29 to 2020-12-29
# Data columns (total 6 columns):
#  #   Column     Non-Null Count  Dtype
# ---  ------     --------------  -----
#  0   Open       2645 non-null   float64
#  1   High       2645 non-null   float64
#  2   Low        2645 non-null   float64
#  3   Close      2645 non-null   float64
#  4   Adj Close  2645 non-null   float64
#  5   Volume     2645 non-null   int64
# dtypes: float64(5), int64(1)
# memory usage: 144.6 KB

# Check the new index
print(prc.index)
# Output:
# DatetimeIndex(['2010-06-29', '2010-06-30', '2010-07-01', '2010-07-02',
#                '2010-07-06', '2010-07-07', '2010-07-08', '2010-07-09',
#                '2010-07-12', '2010-07-13',
#                ...
#                '2020-12-15', '2020-12-16', '2020-12-17', '2020-12-18',
#                '2020-12-21', '2020-12-22', '2020-12-23', '2020-12-24',
#                '2020-12-28', '2020-12-29'],
#               dtype='datetime64[ns]', name='Date', length=2645, freq=None)


# ----------------------------------------------------------------------------
#   Setting datetime indexes during read_csv
# ----------------------------------------------------------------------------
# previously:
# prc = pd.read_csv(CSVLOC)

# New version
prc = pd.read_csv(CSVLOC, parse_dates=['Date'], index_col='Date')
prc.info()
# <class 'pandas.core.frame.DataFrame'>
# DatetimeIndex: 2645 entries, 2010-06-29 to 2020-12-29
# Data columns (total 6 columns):
#  #   Column     Non-Null Count  Dtype
# ---  ------     --------------  -----
#  0   Open       2645 non-null   float64
#  1   High       2645 non-null   float64
#  2   Low        2645 non-null   float64
#  3   Close      2645 non-null   float64
#  4   Adj Close  2645 non-null   float64
#  5   Volume     2645 non-null   int64
# dtypes: float64(5), int64(1)
# memory usage: 144.6 KB


# ----------------------------------------------------------------------------
#   Illustrating the advantages of a datetime indexes
# ----------------------------------------------------------------------------
# Select all data for a given year in one go
print(prc.loc['2020'])
# Output:
#                   Open        High  ...   Adj Close     Volume
# Date                                ...
# 2020-01-02   84.900002   86.139999  ...   86.052002   47660500
# 2020-01-03   88.099998   90.800003  ...   88.601997   88892500
# 2020-01-06   88.094002   90.311996  ...   90.307999   50665000
# 2020-01-07   92.279999   94.325996  ...   93.811996   89410500
# 2020-01-08   94.739998   99.697998  ...   98.428001  155721500
# ...                ...         ...  ...         ...        ...
# 2020-12-22  648.000000  649.880005  ...  640.340027   51716000
# 2020-12-23  632.200012  651.500000  ...  645.979980   33173000
# 2020-12-24  642.989990  666.090027  ...  661.770020   22865600
# 2020-12-28  674.510010  681.400024  ...  663.690002   32278600
# 2020-12-29  661.000000  669.900024  ...  665.989990   22910800
#
# [251 rows x 6 columns]

# Select all data for a given month
print(prc.loc['2020-01'])
# Output:
#                   Open        High  ...   Adj Close     Volume
# Date                                ...
# 2020-01-02   84.900002   86.139999  ...   86.052002   47660500
# 2020-01-03   88.099998   90.800003  ...   88.601997   88892500
# 2020-01-06   88.094002   90.311996  ...   90.307999   50665000
# 2020-01-07   92.279999   94.325996  ...   93.811996   89410500
# 2020-01-08   94.739998   99.697998  ...   98.428001  155721500
# 2020-01-09   99.419998   99.760002  ...   96.267998  142202000
# 2020-01-10   96.358002   96.987999  ...   95.629997   64797500
# 2020-01-13   98.699997  105.125999  ...  104.972000  132588000
# 2020-01-14  108.851997  109.482002  ...  107.584000  144981000
# 2020-01-15  105.952003  107.568001  ...  103.699997   86844000
# 2020-01-16   98.750000  102.891998  ...  102.697998  108683500
# 2020-01-17  101.522003  103.134003  ...  102.099998   68145500
# 2020-01-21  106.050003  109.716003  ...  109.440002   89017500
# 2020-01-22  114.377998  118.900002  ...  113.912003  156845000
# 2020-01-23  112.849998  116.400002  ...  114.440002   98255000
# 2020-01-24  114.125999  114.772003  ...  112.963997   71768000
# 2020-01-27  108.398003  112.888000  ...  111.603996   68040500
# 2020-01-28  113.697998  115.362000  ...  113.379997   58942500
# 2020-01-29  115.138000  117.959999  ...  116.197998   89007500
# 2020-01-30  126.484001  130.175995  ...  128.162003  145028500
# 2020-01-31  128.000000  130.600006  ...  130.113998   78596500
#
# [21 rows x 6 columns]

# Selecting date ranges using strings
print(prc.loc['2020-01-01':'2020-01-05'])
# Output:
#                  Open       High        Low      Close  Adj Close    Volume
# Date
# 2020-01-02  84.900002  86.139999  84.342003  86.052002  86.052002  47660500
# 2020-01-03  88.099998  90.800003  87.384003  88.601997  88.601997  88892500


# ----------------------------------------------------------------------------
#   Computing returns
# ----------------------------------------------------------------------------
# Make sure the dataframe is sorted
prc.sort_index(inplace=True)

# compute returns
rets = prc.loc[:, 'Close'].pct_change()
print(rets)
# Output:
# Date
# 2010-06-29         NaN
# 2010-06-30   -0.002512
# 2010-07-01   -0.078472
# 2010-07-02   -0.125683
# 2010-07-06   -0.160938
#                 ...
# 2020-12-22   -0.014649
# 2020-12-23    0.008808
# 2020-12-24    0.024444
# 2020-12-28    0.002901
# 2020-12-29    0.003465
# Name: Close, Length: 2645, dtype: float64

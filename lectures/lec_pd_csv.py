""" lec_pd_csv.py

Companion codes for the lecture on reading and writing CSV files with Pandas
"""

import os

import pandas as pd

import toolkit_config as cfg

QAN_PRC_CSV = os.path.join(cfg.DATADIR, 'qan_prc_2020.csv')
QAN_NOHEAD_CSV = os.path.join(cfg.DATADIR, 'qan_prc_no_header.csv')
QAN_CLOSE_CSV = os.path.join(cfg.DATADIR, 'qan_close_ser.csv')

# ----------------------------------------------------------------------------
#   Reading data from a CSV file
# ----------------------------------------------------------------------------

# Load the data contained in qan_prc_2020.csv to a DF

qan_naive_read = pd.read_csv(QAN_PRC_CSV)
print(qan_naive_read)
# Output:
#             Date  Open   High   Low  Close  Adj Close    Volume
#  0    2020-01-02  7.14  7.210  7.12   7.16   6.985208   4980666
#  1    2020-01-03  7.28  7.310  7.16   7.19   7.014476   2763615
#  2    2020-01-06  7.01  7.030  6.91   7.00   6.829114   7859151
#  3    2020-01-07  7.23  7.255  7.08   7.10   6.926673   7589056
#  4    2020-01-08  7.05  7.080  6.76   6.86   6.692532  13449760
#  ..          ...   ...    ...   ...    ...        ...       ...
#  249  2020-12-22  4.83  4.860  4.78   4.80   4.800000  12150719
#  250  2020-12-23  4.80  4.950  4.80   4.91   4.910000   6895232
#  251  2020-12-24  5.03  5.030  4.89   4.89   4.890000   3588668
#  252  2020-12-29  4.95  5.010  4.94   4.96   4.960000   4330876
#  253  2020-12-30  4.95  4.980  4.91   4.96   4.960000   4010174
#
#  [254 rows x 7 columns]

qan_naive_read.info()
# Output:
#   <class 'pandas.core.frame.DataFrame'>
#   RangeIndex: 223 entries, 0 to 222
#   Data columns (total 7 columns):
#     #   Column     Non-Null Count  Dtype
#    ---  ------     --------------  -----
#     0   Date       223 non-null    object
#     1   Open       223 non-null    float64
#     2   High       223 non-null    float64
#     3   Low        223 non-null    float64
#     4   Close      223 non-null    float64
#     5   Adj Close  223 non-null    float64
#     6   Volume     223 non-null    int64
#   dtypes: float64(5), int64(1), object(1)
#   memory usage: 12.3+ KB

# Using the `set_index` method
qan_naive_read.set_index('Date', inplace=True)
print(qan_naive_read)
# Output:
#              Open   High   Low  Close  Adj Close    Volume
#  Date
#  2020-01-02  7.14  7.210  7.12   7.16   6.985208   4980666
#  2020-01-03  7.28  7.310  7.16   7.19   7.014476   2763615
#  2020-01-06  7.01  7.030  6.91   7.00   6.829114   7859151
#  2020-01-07  7.23  7.255  7.08   7.10   6.926673   7589056
#  2020-01-08  7.05  7.080  6.76   6.86   6.692532  13449760
#  ...          ...    ...   ...    ...        ...       ...
#  2020-12-22  4.83  4.860  4.78   4.80   4.800000  12150719
#  2020-12-23  4.80  4.950  4.80   4.91   4.910000   6895232
#  2020-12-24  5.03  5.030  4.89   4.89   4.890000   3588668
#  2020-12-29  4.95  5.010  4.94   4.96   4.960000   4330876
#  2020-12-30  4.95  4.980  4.91   4.96   4.960000   4010174
#
#  [254 rows x 6 columns]

qan_naive_read.info()
# <class 'pandas.core.frame.DataFrame'>
# Index: 254 entries, 2020-01-02 to 2020-12-30
# Data columns (total 6 columns):
#  #   Column     Non-Null Count  Dtype
# ---  ------     --------------  -----
#  0   Open       254 non-null    float64
#  1   High       254 non-null    float64
#  2   Low        254 non-null    float64
#  3   Close      254 non-null    float64
#  4   Adj Close  254 non-null    float64
#  5   Volume     254 non-null    int64
# dtypes: float64(5), int64(1)
# memory usage: 13.9+ KB

# Using the `index_col` parameter:
qan_better_read = pd.read_csv(QAN_PRC_CSV, index_col='Date')
print(qan_better_read)
# Output:
#              Open   High   Low  Close  Adj Close    Volume
#  Date
#  2020-01-02  7.14  7.210  7.12   7.16   6.985208   4980666
#  2020-01-03  7.28  7.310  7.16   7.19   7.014476   2763615
#  2020-01-06  7.01  7.030  6.91   7.00   6.829114   7859151
#  2020-01-07  7.23  7.255  7.08   7.10   6.926673   7589056
#  2020-01-08  7.05  7.080  6.76   6.86   6.692532  13449760
#  ...          ...    ...   ...    ...        ...       ...
#  2020-12-22  4.83  4.860  4.78   4.80   4.800000  12150719
#  2020-12-23  4.80  4.950  4.80   4.91   4.910000   6895232
#  2020-12-24  5.03  5.030  4.89   4.89   4.890000   3588668
#  2020-12-29  4.95  5.010  4.94   4.96   4.960000   4330876
#  2020-12-30  4.95  4.980  4.91   4.96   4.960000   4010174
#
#  [254 rows x 6 columns]

qan_better_read.info()
# Output:
# <class 'pandas.core.frame.DataFrame'>
# Index: 254 entries, 2020-01-02 to 2020-12-30
# Data columns (total 6 columns):
#  #   Column     Non-Null Count  Dtype
# ---  ------     --------------  -----
#  0   Open       254 non-null    float64
#  1   High       254 non-null    float64
#  2   Low        254 non-null    float64
#  3   Close      254 non-null    float64
#  4   Adj Close  254 non-null    float64
#  5   Volume     254 non-null    int64
# dtypes: float64(5), int64(1)


# ----------------------------------------------------------------------------
#   Storing data to a CSV file
# ----------------------------------------------------------------------------
# First, we read the data into a dataframe
qan_better_read = pd.read_csv(QAN_PRC_CSV, index_col='Date')

# We then save the data into the file located at QAN_NOHEAD_CSV above.
# The column headers will not be saved
qan_better_read.to_csv(QAN_NOHEAD_CSV, header=False)


# ----------------------------------------------------------------------------
#  Saving the contents of a series to a CSV file
# ----------------------------------------------------------------------------
# Create a series from a dataframe
qan_better_read = pd.read_csv(QAN_PRC_CSV, index_col='Date')
ser = qan_better_read.loc[:, 'Close']
print(ser)
# Output:
#  Date
#  2020-01-02    7.16
#  2020-01-03    7.19
#  2020-01-06    7.00
#  2020-01-07    7.10
#  2020-01-08    6.86
#                ...
#  2020-12-22    4.80
#  2020-12-23    4.91
#  2020-12-24    4.89
#  2020-12-29    4.96
#  2020-12-30    4.96
#  Name: Close, Length: 254, dtype: float64

# Save the series to a CSV file
ser.to_csv(QAN_CLOSE_CSV)


# Note that the name of the series will be the same as the column label
print(ser.name)
# Output:
#  'Close'

# Create a series without a name
dates = list(qan_better_read.index)  # --> list with the index labels
data = list(qan_better_read.Close)  # --> list with closing prices
ser_no_name = pd.Series(data, index=dates)
print(ser_no_name)
# Output:
#  2020-01-02    7.16
#  2020-01-03    7.19
#  2020-01-06    7.00
#  2020-01-07    7.10
#  2020-01-08    6.86
#                ...
#  2020-12-22    4.80
#  2020-12-23    4.91
#  2020-12-24    4.89
#  2020-12-29    4.96
#  2020-12-30    4.96
#  Length: 254, dtype: float64

print(f'The name of the series is {ser_no_name.name}')
# Output:
#  'The name of the series is None'

# Now save it to the same CSV file as above
ser_no_name.to_csv(QAN_CLOSE_CSV)
#
#
## Read the data back
#as_df = pd.read_csv(QAN_CLOSE_CSV)
#print(as_df)
#


# ----------------------------------------------------------------------------
#   Saving the contents of an unnamed series (better version)
# ----------------------------------------------------------------------------
# Using the ser_no_name created above
# Save the contents without column headers

#ser_no_name.to_csv(QAN_CLOSE_CSV, header=False)
## Read it back
#as_df = pd.read_csv(QAN_CLOSE_CSV, header=None, index_col=0)
#print(as_df)
#


# ----------------------------------------------------------------------------
#   Saving the contents of an unnamed series (even better version)
# ----------------------------------------------------------------------------
# Using the ser_no_name created above
# Save the contents without column headers

#ser_no_name.to_csv(QAN_CLOSE_CSV, header=False)
## Read it back
#as_df = pd.read_csv(QAN_CLOSE_CSV, header=None, names=["Date", "Close"], index_col=0)
#print(as_df)
#


# ----------------------------------------------------------------------------
#   Saving the contents of an unnamed series (best version)
# ----------------------------------------------------------------------------
# Using the ser_no_name created above
# Save the contents without column headers

#ser_no_name.to_csv(QAN_CLOSE_CSV,
#        index_label="Date",
#        header=['Close'],
#        )
## Read it back
#as_df = pd.read_csv(QAN_CLOSE_CSV, index_col=0)
#print(as_df)
#
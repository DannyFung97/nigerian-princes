%matplotlib inline

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configure libraries
# The seaborn library makes plots look nicer
sns.set()
sns.set_context('talk')

# Don't display too many rows/cols of DataFrames
pd.options.display.max_rows = 7
pd.options.display.max_columns = 8

# Round decimals when displaying DataFrames
pd.set_option('precision', 2)

df_2018_dnc_state_complaints_5yr = pd.read_csv("csv_files/2018_DNC_State_Complaints_5yr.csv")
df_2018_dnc_state_complaints_calltype = pd.read_csv("csv_files/2018_DC_State_Complaints_by_CallType.csv")
df_2018_dnc_state_complaints_topic = pd.read_csv("csv_files/2018_DC_State_Complaints_by_Topic.csv")
df_2017_dnc_state_complaints_calltype = pd.read_csv("csv_files/2017_DC_State_Complaints_by_CallType.csv")
df_2017_dnc_state_complaints_topic = pd.read_csv("csv_files/2017_DC_State_Complaints_by_Topic.csv")


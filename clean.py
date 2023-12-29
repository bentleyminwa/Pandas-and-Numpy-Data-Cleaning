import pandas as pd
import numpy as np

from load import Loader


# Load the Data for Cleaning
data_set = Loader.load_data()


# Dropping Columns
col_drops = ['Edition Statement', 'Corporate Author', 'Corporate Contributors',
             'Engraver', 'Issuance type', 'Flickr URL', 'Shelfmarks']

data_set.drop(columns=col_drops, inplace=True)


# Changing Index of DataFrame
data_set.set_index('Identifier', inplace=True)


# Tidying up Fields in the Data

extr_ = data_set['Date of Publication'].str.extract(r'^(\d{4})', expand=False)      # Regex

data_set['Date of Publication'] = pd.to_numeric(extr_)

data_set['Date of Publication'].isnull().sum() / len(data_set)


# Combining str Methods with Numpy to Clean Columns
pub = data_set['Place of Publication']
london = pub.str.contains('London')
oxford = pub.str.contains('Oxford')

data_set['Place of Publication'] = np.where(london, 'London', np.where(oxford, 'Oxford', pub.str.replace('-', ' ')))


# Cleaning Entire Dataset Using applymap() Function

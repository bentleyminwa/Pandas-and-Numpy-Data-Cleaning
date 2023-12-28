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
data_set = data_set.set_index('Identifier')

print(data_set.head(5))

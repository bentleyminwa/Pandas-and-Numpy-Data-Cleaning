import pandas as pd
import numpy as np

from load import Loader


# Load the Data for Cleaning
data_set = Loader.load_data()


# Dropping Columns
col_drop = ['Edition Statement', 'Corporate Author', 'Corporate Contributors',
            'Former owner', 'Engraver', 'Issuance type', 'Flickr URL', 'Shelfmarks']

data_set.drop(columns=col_drop, inplace=True)


# Changing Index of a DataFrame

data_set = data_set.set_index('Identifier', inplace=True)


# Tidying up Fields in the Data

print(data_set)
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


# Cleaning Entire Dataset using applymap() Function
towns_set = Loader.load_town_data()


def get_citystate(item):
    if ' (' in item:
        return item[:item.find(' (')]
    elif '[' in item:
        return item[:item.find('[')]
    else:
        return item
    

towns_set = towns_set.applymap(get_citystate)


# Renaming Columns and Skipping Rows
olympics_set = Loader.load_olympics_data()

new_col_names = {
    'Unnamed: 0': 'Country',
    '? Summer': 'Summer Olympics',
    '01 !': 'Gold',
    '02 !': 'Silver',
    '03 !': 'Bronze',
    '? Winter': 'Winter Olympics',
    '01 !.1': 'Gold.1',
    '02 !.1': 'Silver.1',
    '03 !.1': 'Bronze.1',
    '? Games': '# Games',
    '01 !.2': 'Gold.2',
    '02 !.2': 'Silver.2',
    '03 !.2': 'Bronze.2'
}


olympics_set.rename(columns=new_col_names, inplace=True)
print(olympics_set.head())
import pandas as pd
import numpy as np

from Exhibit_A.load import Loader


# Load the Data for Cleaning
data_set = Loader.load_data()

print(data_set.columns)
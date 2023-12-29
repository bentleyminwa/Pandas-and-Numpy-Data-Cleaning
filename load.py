import pandas as pd

# Loading Data
class Loader():

    def __init__(self) -> None:
        pass

    def load_data():
        # Loads the book dataset
        df = pd.read_csv("Data/BL-Flickr-Images-Book.csv")

        return df
    
    def load_town_data():
        # Loads the university_towns.txt file
        university_towns = []

        with open('Data/university_towns.txt') as file:
            for line in file:
                if '[edit]' in line:

                    # Remember this `state` until the next is found
                    state = line
                else:

                    # Otherwise, we have a city; keep `state` as last seen
                    university_towns.append((state, line))


        towns_df = pd.DataFrame(university_towns, columns = ['State', 'RegionName'])

        return towns_df

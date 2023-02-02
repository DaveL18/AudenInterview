import pandas as pd
import os

# list to store the data from all csv files
dfs = []
path = r'C:\Users\Documents\Auden\Files'

# loop over each csv file
for i in os.listdir(path):

    # read the csv file into a pandas dataframe
    df = pd.read_csv(path+f'\{i}', encoding='utf-8')
    # add the dataframe to the list of dataframes
    dfs.append(df)

# merge all dataframes into a single dataframe using the ID column as the key
merged_df = dfs[0].merge(dfs[1], on='ID', how='outer')
for i in range(2, len(dfs)):
    merged_df = merged_df.merge(dfs[i], on='ID', how='outer')

# write the combined data to a new csv file
merged_df.to_csv('merged_file.csv', index=False, encoding='utf-8')
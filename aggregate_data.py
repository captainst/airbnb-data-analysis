import pandas as pd
import numpy as np
import os

data_root_path = "./data"
seattle_dir_name = "airbnb-seattle"
boston_dir_name = "airbnb-boston"

seattle_data_path = os.path.join(data_root_path, seattle_dir_name)
boston_data_path = os.path.join(data_root_path, boston_dir_name)

def read_csvs_to_df (datapath, filename):
    df_listing_total = pd.DataFrame()
    # Get a list of all directories inside the specified directory
    data_directories = [name for name in os.listdir(datapath) if os.path.isdir(os.path.join(datapath, name))]
    sorted_dirs = sorted(data_directories, key=lambda x: x.lower())
    for dir in sorted_dirs:
        listing_file_name = os.path.join(datapath, dir, filename)
        print("scanning folder ", listing_file_name)
        df_temp = pd.read_csv(listing_file_name)
        df_listing_total = pd.concat([df_listing_total, df_temp]).reset_index(drop=True)
        
    return df_listing_total
        
print("aggregating seattle listings")
df_listing_total = read_csvs_to_df(seattle_data_path, "listings.csv")
df_listing_total.to_csv(os.path.join(seattle_data_path, "total_listings.csv"), index=False)

print("aggregating boston listings")
df_listing_total = read_csvs_to_df(boston_data_path, "listings.csv")
df_listing_total.to_csv(os.path.join(boston_data_path, "total_listings.csv"), index=False)

print("aggregating seattle calendars")
df_listing_total = read_csvs_to_df(seattle_data_path, "calendar.csv")
df_listing_total.to_csv(os.path.join(seattle_data_path, "total_calendars.csv"), index=False)

print("aggregating boston calendars")
df_listing_total = read_csvs_to_df(boston_data_path, "calendar.csv")
df_listing_total.to_csv(os.path.join(boston_data_path, "total_calendars.csv"), index=False)
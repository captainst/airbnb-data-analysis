# data retrieved from: http://insideairbnb.com/get-the-data

import os
import shutil
import urllib.request
import gzip

datapath_root = "data"
datapath_seattle = "airbnb-seattle"
datapath_boston = "airbnb-boston"

urls_seattle_base = "http://data.insideairbnb.com/united-states/wa/seattle/"
urls_seattle_files = ["2023-06-24/data/listings.csv.gz",
                      "2023-06-24/data/calendar.csv.gz",
                      "2023-06-24/data/reviews.csv.gz",
                      "2023-06-24/visualisations/neighbourhoods.csv",
                      "2023-03-24/data/listings.csv.gz",
                      "2023-03-24/data/calendar.csv.gz",
                      "2023-03-24/data/reviews.csv.gz",
                      "2023-03-24/visualisations/neighbourhoods.csv",
                      "2022-12-24/data/listings.csv.gz",
                      "2022-12-24/data/calendar.csv.gz",
                      "2022-12-24/data/reviews.csv.gz",
                      "2022-12-24/visualisations/neighbourhoods.csv",                      
                      "2022-09-18/data/listings.csv.gz",
                      "2022-09-18/data/calendar.csv.gz",
                      "2022-09-18/data/reviews.csv.gz",
                      "2022-09-18/visualisations/neighbourhoods.csv"
                      ]

urls_boston_base = "http://data.insideairbnb.com/united-states/ma/boston/"
urls_boston_files = ["2023-06-21/data/listings.csv.gz",
                     "2023-06-21/data/calendar.csv.gz",
                     "2023-06-21/data/reviews.csv.gz",
                     "2023-06-21/visualisations/neighbourhoods.csv",
                     "2023-03-19/data/listings.csv.gz",
                     "2023-03-19/data/calendar.csv.gz",
                     "2023-03-19/data/reviews.csv.gz",
                     "2023-03-19/visualisations/neighbourhoods.csv",
                     "2022-12-21/data/listings.csv.gz",
                     "2022-12-21/data/calendar.csv.gz",
                     "2022-12-21/data/reviews.csv.gz",
                     "2022-12-21/visualisations/neighbourhoods.csv",                      
                     "2022-09-15/data/listings.csv.gz",
                     "2022-09-15/data/calendar.csv.gz",
                     "2022-09-15/data/reviews.csv.gz",
                     "2022-09-15/visualisations/neighbourhoods.csv"
                     ]

def is_gz_file(file_path):
    _, file_extension = os.path.splitext(file_path)
    return file_extension.lower() == '.gz'


def extract_gz_file(gz_file_path, extract_path):
    with gzip.open(gz_file_path, 'rb') as f_in:
        with open(extract_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
            
def download_and_extract (url, folder, filename):
    # zip_url = "https://example.com/example.zip"  # Replace with the URL of the zip file
    # extract_folder = "abc"
    
    # Download the zip file
    urllib.request.urlretrieve(url, "temp.download")

    if is_gz_file(url):
        extract_gz_file("./temp.download", os.path.join(folder, filename))
        os.remove("temp.download") # Delete the temporary zip file
    else:
        shutil.move("./temp.download", os.path.join(folder, filename))
        
    
    

# check whether the "data" path exists or not
isExist = os.path.exists(datapath_root)
if (not isExist):
    print("creating data folder ...", end=' ')
    try:
        os.makedirs(datapath_root)
        print("Done!")
    except OSError as e:
        print(f"An error occurred: {e}")
        exit(1)
else:
    print("data folder existing. remove it before download data!")
    exit(0)
# # check whether we have the data
# isExist = os.path.exists(os.path.join(datapath_root, datapath_seattle, "listings.csv"))
# if (not isExist):


print("downloading seattle airbnb data ...")
# if directory exists, first, remove it (with the contents)
dirpath = os.path.join(datapath_root, datapath_seattle)
if (os.path.exists(dirpath)):
    shutil.rmtree(dirpath)
    
os.makedirs(dirpath)

for url in urls_seattle_files:
    date = url.split("/")[0]
    filename = url.split("/")[-1].split(".")[0] + ".csv"
    subpath = os.path.join(dirpath, date)
    if (not os.path.exists(subpath)):
        os.makedirs(subpath)
    download_and_extract(urls_seattle_base+url, subpath, filename)
        
print("downloading boston airbnb data ...")
# if directory exists, first, remove it (with the contents)
dirpath = os.path.join(datapath_root, datapath_boston)
if (os.path.exists(dirpath)):
    shutil.rmtree(dirpath)
    
os.makedirs(dirpath)

for url in urls_boston_files:
    date = url.split("/")[0]
    filename = url.split("/")[-1].split(".")[0] + ".csv"
    subpath = os.path.join(dirpath, date)
    if (not os.path.exists(subpath)):
        os.makedirs(subpath)
    download_and_extract(urls_boston_base+url, subpath, filename)

    
    

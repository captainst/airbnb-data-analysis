<p align="center">
  <a href="http://insideairbnb.com/">
    <img src="./assets/seattle-boston.png" alt="Bootstrap logo" >
  </a>
</p>

## airbnb-data-analysis
This repo contains the try-outs & implementations of the airbnb data analysis project, which is part of the Udacity Data Scientist Program.

Bonus: I have published an article on Medium [here](
https://medium.com/@quchen.ch/data-analysis-on-airbnb-data-7e54e97f4476). Feel free to check it out !

## Table of contents

- [Motivation](#motivation)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Licensing](#licensing)

## Motivation
This project is part of the Udacity Data Scientist Program (Writting a Data Scientst Blog Post). I followed the CRISP-DM process described during the course, and used the latest data from [Airbnb website](http://insideairbnb.com/get-the-data/) to look for valuable insignts, and answering interesting questions.

## Dataset
The airbnb data from kaggle is quite out-dated (year 2017). In order to answer the questions of interest, I downloaded the latest data directly from the [Airbnb website](http://insideairbnb.com/get-the-data/) for the cities of Seattle & Boston from 2022 to 2023.

I prepared the python scripts to automatically download the data ([download_data.py](./download_data.py)) and aggregate the data ([aggregate_data.py](./aggregate_data.py)). The scripts will create a folder "data" and generate the aggregated data into csv file inside.
* Note that the only the data from the last 4 quarters are kept on airbnb website. You might need to adjust the script accordingly in the furture.

After downloading and aggregate the data, the "data" folder is supposed to look like the following: There will be one <b>total_calendars.csv</b> and one <b>total_listings.csv</b> for seattle and boston
```
|-data
  |-airbnb-boston
    |-2022-09-15
        calendar.csv
        listing.csv
    |-2022-12-21
        calendar.csv
        listing.csv
    |-2023-03-19
        calendar.csv
        listing.csv
    |-2023-06-21
        calendar.csv
        listing.csv
    total_calendars.csv
    total_listings.csv
  |-airbnb-seattle
    |-2022-09-18
        calendar.csv
        listing.csv
    |-2022-12-24
        calendar.csv
        listing.csv
    |-2023-03-24
        calendar.csv
        listing.csv
    |-2023-06-24
        calendar.csv
        listing.csv
    total_calendars.csv
    total_listings.csv

```

## Installation
Simply using the pip: 
```
pip install -r requirements.txt
```
It is recommended to install into a virtual environment like Anaconda.

## Usage
Refer to the [airbnb-data-analysis.ipynb](./airbnb-data-analyais.ipynb)

## Licensing
This repository is licensed under [Apache-2.0 license](https://github.com/captainst/airbnb-data-analysis/blob/main/LICENSE)




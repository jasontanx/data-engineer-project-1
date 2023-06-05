
import requests
import pandas as pd
import logging

from transform import rename_data

def get_file():
    # URLs of the CSV files
    url_2021 = 'https://www.aviationfile.com/wp-content/uploads/2022/05/Busiest-European-Airports-2021.csv'

    # Send a GET request to download the file
    response_2021 = requests.get(url_2021)

    # Check if both requests were successful --> success code '200'
    if response_2021.status_code == 200:
        # Save downloading 2021 file
        with open('Busiest-European-Airports-2021.csv', 'wb') as file_2021:
            file_2021.write(response_2021.content)
        
        print("Files downloaded successfully.")
        
        # Read the downloaded CSV files into DataFrames
        df_2021 = pd.read_csv('Busiest-European-Airports-2021.csv')
        
        print("2021 Data:")
        print(df_2021.head())

    else:
        print("Failed to download the file(s).")
        
    rename_data(df_2021)


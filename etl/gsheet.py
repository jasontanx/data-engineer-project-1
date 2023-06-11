from time import datetime, time
from google.cloud import bigquery
import logging

import gspread
from oauth2client.service_account import ServiceAccountCredentials

key_path = "key.json" # secret key file of gcp

def get_logging_format() -> logging.Logger:
    """
    function to return custom format logging

    return logging.Logger
    """

    logging.Formatter.converter = time.gmtime
    logging.basicConfig(
        format="[%(asctime)s,%(msecs)d] %(levelname)-8s [%(filename)s:%(lineno)d] - %(message)s",
        datefmt="%Y-%m-%d, %H:%M:%S",
        level=logging.INFO,
    )
    _logger: logging.Logger = logging.getLogger("de-logging")
    return _logger

logger: logging.Logger = get_logging_format()


def query_data():
    """
    Extract Data from Bigquery table with prepared query
    """

    date_fmt = datetime.now().strftime("%Y%m%d") + ".csv"
    file_name = "european_airport_busy" + date_fmt

    bqclient = bigquery.Client.from_service_account_json(key_path)
    
    job_config = bigquery.QueryJobConfig(allow_large_results=True)

    query_loc = './sql/query.sql'
    sql_file = open(query_loc, 'r')
    query_string = sql_file.read()

    sql_file.close()

    # make api request to run query
    query_job = bqclient.query(query_string, job_config=job_config)

    # wait for job to complete
    query_job.result()

    dataframe = bqclient.query(query_string).to_dataframe(create_bqstorage_client=True)
    print(dataframe.head())

    dataframe.to_csv(file_name) # output path and file_name

    logger.info("export to csv: %s", file_name)
    logger.info("Number of rows exported: %d", len(dataframe))
    logger.info(len(dataframe))

    # return file_name
    load_gsheet(file_name)


SERVICE_ACCOUNT_FILE = 'key.json' # cred to allow that access

def load_gsheet(file_name):

    # Set up authentication for Google Sheets
    SCOPES = ['https://spreadsheets.google.com/feeds', 
            'https://www.googleapis.com/auth/drive'] # asking for access to the scope

    credentials = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    client = gspread.authorize(credentials)

    # Load the CSV file
    # csv_file = 'path/to/your-file.csv'  # Replace with the path to your CSV file
    # with open(csv_file, 'r') as file:
    #     csv_data = file.read()

    with open(file_name, 'r') as file:
        csv_data = file.read()

    # Create a new Google Sheet
    sheet = client.open('busy_european_airport')

    # Write the CSV data to the sheet
    worksheet = sheet.get_worksheet(0)  # write to the first worksheet
    worksheet.update('A1', csv_data)

    print("Data uploaded to Google Sheet successfully...")



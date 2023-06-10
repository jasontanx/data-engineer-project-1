from google.cloud import bigquery
import logging
import time
from etl.gsheet import query_data

project_id = 'myfirstproject-364809'
dataset_id = 'eu_busy_airport'
tbl_id = 'eu_busy_airport_v1'

key_path = "key.json"
# key_path = '/Users/junshengtan/Desktop/de-project/key.json'
# key_path = os.environ['GOOGLE_APPLICATION_CREDENTIALS']
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


def load_bq(df_2021):

    logger.info("ingesting to bq...")
    bq_client = bigquery.Client.from_service_account_json(key_path)
    table_bq = f'{project_id}.{dataset_id}.{tbl_id}'
    job_config = bigquery.LoadJobConfig()
    job_config.write_disposition="WRITE_TRUNCATE" # "WRITE_APPEND" as alternative
    job = bq_client.load_table_from_dataframe(
        df_2021, table_bq, job_config=job_config)
    job.result()
    logger.info("Data ingested to BQ -> %s", table_bq)

    query_data(df_2021)


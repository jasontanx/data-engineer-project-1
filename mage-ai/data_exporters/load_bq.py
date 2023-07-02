from mage_ai.data_preparation.repo_manager import get_repo_path
from mage_ai.io.bigquery import BigQuery
from mage_ai.io.config import ConfigFileLoader
from pandas import DataFrame
from os import path

from google.cloud import bigquery
import logging
import time

project_id = 'myfirstproject-364809'
dataset_id = 'eu_busy_airport'
tbl_id = 'eu_busy_airport_v2'

@data_exporter
def load_bq(df_2021):

    table_id = f'{project_id}.{dataset_id}.{tbl_id}'
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    BigQuery.with_config(ConfigFileLoader(config_path, config_profile)).export(
        df_2021,
        table_id,
        if_exists='replace',  # Specify resolution policy if table name already exists
    )

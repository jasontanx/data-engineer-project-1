# Mage-ai

In this data engineering project, Mage-ai is applied as a tool to build, run and manage the data pipelines for integrating and transforming data.

**About Mage-ai**

I want to know more about Mage-ai! 🪄

❇️ **Mage-ai website**:  https://www.mage.ai/ 

❇️ **Introduction to Mage-ai**: https://docs.mage.ai/introduction/overview

❇️ **Mage-ai Github**: https://github.com/mage-ai/mage-ai

**Set-up for Mac**
1. Using Docker

```
docker run -it -p 6789:6789 -v $(pwd):/home/src mageai/mageai \
  /app/run_app.sh mage start [project_name]
```

2. Using secret credential files in Docker (GCP Credentials used for this project)

```
docker run -it -p 6789:6789
    -v /Users/dragon/secrets:/home/secrets \
    -v $(pwd):/home/src mageai/mageai \
    /app/run_app.sh mage start [project_name]
```

Open http://localhost:6789 in your browser and build a pipeline.

**1. Pipeline Set-Up - ETL**

<img width="191" alt="Screenshot 2023-07-01 at 8 02 18 PM" src="https://github.com/jasontanx/data-engineer-project-1/assets/116934441/d75adb9b-f18b-49f7-abda-8caaf657af71">

**2. Pipeline Set-Up - ETL Code Block**

- Data Loader --> Extract data from the link provided (source)

- Transformer --> transform data variables / fields (rename variable name)

- Data Exporter --> export data to BigQuery (Destination)

<img width="1077" alt="Screenshot 2023-07-01 at 8 03 33 PM" src="https://github.com/jasontanx/data-engineer-project-1/assets/116934441/2510fd20-10c0-4141-bfb5-67f48843ce74">

**3. Pipeline Schedule - Scheduling pipeline to Run Daily**

<img width="1104" alt="Screenshot 2023-07-01 at 8 06 37 PM" src="https://github.com/jasontanx/data-engineer-project-1/assets/116934441/b7c1ee41-f2f8-4859-bac3-aaa6fa225f7e">

**4. Pipeline Status - Pipeline Run Successful**

<img width="1511" alt="Screenshot 2023-07-01 at 8 10 42 PM" src="https://github.com/jasontanx/data-engineer-project-1/assets/116934441/342ab69f-d24f-4eab-a61d-558cc3057f90">

**Source**: 

1. https://docs.mage.ai/getting-started/setup

2. https://docs.mage.ai/production/ci-cd/local-cloud/repository-setup


**Documentation: Data Loading into BigQuery**

https://docs.mage.ai/design/data-loading#bigquery

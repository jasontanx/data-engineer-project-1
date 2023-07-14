# data-engineer-project-1

![git2](https://github.com/jasontanx/data-engineer-project-1/assets/116934441/2455a2dd-28e0-4308-b64b-e9a1a300b70e)

# European Airport & Sentiment Data Engineering Project ✈️

No. | Items | Date Updated 
--- | --- | ---
1 | Repo Creation | 31 May 2023
2 | Upload dataset relevant to the project | 31 May 2023
3 | Design project data architecture | 01 June 2023
4 | Develop BQ table with terraform  | 03 June 2023
5 | Update Github ETL script code | 05 June 2023
6 | Update requirements.txt file | 06 June 2023
7 | Create conda environment in local - experimentation | 08 June 2023
8 | Minor changes on ETL code due to code error | 11 June 2023
9 | Minor ETL code changes - Error resolved | 12 June 2023
10 | Data successfully ingested into Google Sheet and BigQuery ✅ | 13 June 2023
11 | Start exploring 2nd dataset (airport comment) - sentiment analysis | 15 June 2023
12 | Data pre-processing & develop sentiment analysis | 16 June 2023
13 | Looker Studio chart exploration - Day 1 | 18 June 2023
14 | Looker Studio chart exploration - Day 2 | 20 June 2023
15 | Looker Studio chart exploration - Day 3 | 23 June 2023
16 | Looker Studio chart complete  - Day 4 ✅ | 24 June 2023
17 | Explore orchestration tools - Airflow | 26 June 2023
18 | Explore orchestration tools - Mage-ai | 01 July 2023
19 | Update code - Mage-ai + created new repo | 02 July 2023
20 | Update code - Mage-ai + ETL pipeline | 07 July 2023

# Data Architecture 

The following diagram shows the overall data architecture of the project along with the tools involved.

![data_architecture](https://github.com/jasontanx/data-engineer-project-1/assets/116934441/a900ebd4-2f16-48c3-9991-0dbfb13cebce)

In summary, the following tools will be involved:
1. Mage.ai --> Workflow orchestration tool
2. GCP BigQuery --> Data warehouse
3. Terraform --> Infrastructure as Code (IaC) 
4. Goolge Sheet --> Spreadsheet
5. Looker Studio --> Visualisation & Business Intelligence tool 
6. Python --> ETL code

# Final Outcome
Data ingested at GSheet below:
https://docs.google.com/spreadsheets/d/1bTc2AKkWewiNziHm9L4RHIhepFIOvYJm6MVerFi6C0Y/edit#gid=0

Data ingested at BigQuery:
![de_bq_ss](https://github.com/jasontanx/data-engineer-project-1/assets/116934441/18afe1fb-dd34-44fa-ba85-22d688522c9b)

# Looker Studio
European Airport 2021 - Dashboard

<img width="899" alt="Screenshot 2023-06-24 at 3 20 30 PM" src="https://github.com/jasontanx/data-engineer-project-1/assets/116934441/f278bf1d-2e3b-4cd4-8ec1-a225451491ad">

🌟Insights Generated🌟

❇️ **32** European Countries and a total of **101** airports are involved in this dashboard

❇️ There's an increase of **199k** passenger amount from the year 2020 to the year 2021

❇️ **Moscow** has the highest passenger volume by **city** in the year 2021, followed by Paris and London

❇️ **Country** wise, **Russia** has the highest passenger volume, followed by Spain and France

Source:
https://lookerstudio.google.com/reporting/084b0972-c6fd-4d16-87df-5274e9cffc32

# Orchestration Tools - mage.ai

28/6/2023 - Experimented Airflow with Astronomer with newly developed dag.

- Mage-ai

https://docs.mage.ai/introduction/overview


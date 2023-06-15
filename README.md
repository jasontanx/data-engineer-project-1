# data-engineer-project-1

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

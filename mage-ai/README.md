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

**Source**: 

https://docs.mage.ai/getting-started/setup

https://docs.mage.ai/production/ci-cd/local-cloud/repository-setup


Data Loading into BigQuery

https://docs.mage.ai/design/data-loading#bigquery

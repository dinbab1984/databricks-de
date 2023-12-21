# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md # CLI and REST API Lab
# MAGIC
# MAGIC Import this Git repo into your Databricks workspace: [cli-demo](https://github.com/databricks-academy/cli-demo)
# MAGIC
# MAGIC Then, navigate to the following Markdown files to access demo instructions for this lesson.
# MAGIC | Demo | File Path |
# MAGIC | --- | --- |
# MAGIC | Working with the Databricks CLI | [cli-demo/cli-orch.md](https://github.com/databricks-academy/cli-demo/blob/published/cli-orch.md) |
# MAGIC | Configuring and Using the Databricks REST API | [cli-demo/api-demo.md](https://github.com/databricks-academy/cli-demo/blob/published/api-demo.md) |

# COMMAND ----------

# MAGIC %md
# MAGIC # CLI examples
# MAGIC
# MAGIC ## Install CLI
# MAGIC `pip3 install databricks-cli`
# MAGIC ## Configure CLI
# MAGIC `databricks configure --token`
# MAGIC ## GET Clusters List
# MAGIC `databricks clusters list`
# MAGIC
# MAGIC ## Get Jobs List
# MAGIC `databricks jobs list`
# MAGIC
# MAGIC ## Get Jobs Runs List
# MAGIC `databricks runs list`
# MAGIC
# MAGIC ## Trigger a new job (run-now)
# MAGIC `databricks jobs run-now --job-id=763249216788681`
# MAGIC
# MAGIC ## Get a Job Run Info(either single task job run id or individual task run if only supported in CLI)
# MAGIC `databricks runs get --run-id=973737584753150`
# MAGIC
# MAGIC ## Restart a Cluster
# MAGIC `databricks clusters restart --cluster-id=1219-142422-5zm10ixv`
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC # API examples
# MAGIC
# MAGIC ## GET Clusters List
# MAGIC `curl --location --request GET 'https://adb-366368161648507.7.azuredatabricks.net/api/2.0/clusters/list' --header 'Authorization: Bearer <access_token_here>'`
# MAGIC
# MAGIC ## Get Jobs List
# MAGIC `curl --location --request GET 'https://adb-366368161648507.7.azuredatabricks.net/api/2.1/jobs/list' --header 'Authorization: Bearer <access_token_here>'`
# MAGIC
# MAGIC ## Get Jobs Runs List
# MAGIC `curl --location --request GET 'https://adb-366368161648507.7.azuredatabricks.net/api/2.1/jobs/runs/list?=' --header 'Authorization: Bearer <access_token_here>'`
# MAGIC
# MAGIC ## Trigger a new job (run-now)
# MAGIC `curl --location --request POST 'https://adb-366368161648507.7.azuredatabricks.net/api/2.1/jobs/run-now?job_id=763249216788681' --header 'Authorization: Bearer <access_token_here>'`
# MAGIC
# MAGIC ## Get a Job Run Info
# MAGIC `curl --location --request GET 'https://adb-366368161648507.7.azuredatabricks.net/api/2.1/jobs/runs/get?run_id=29894235171072' --header 'Authorization: Bearer <access_token_here>'`
# MAGIC
# MAGIC ## Restart a Cluster
# MAGIC `curl --location --request POST 'https://adb-366368161648507.7.azuredatabricks.net/api/2.0/clusters/restart?cluster_id=1219-142422-5zm10ixv' --header 'Authorization: Bearer <access_token_here>'`
# MAGIC
# MAGIC ## Get Cluster Info
# MAGIC `curl --location --request GET 'https://adb-366368161648507.7.azuredatabricks.net/api/2.0/clusters/get?cluster_id=1219-142422-5zm10ixv' --header 'Authorization: Bearer <access_token_here>'`

# COMMAND ----------

# MAGIC %sh sudo apt-get install jq

# COMMAND ----------

# MAGIC %sh curl --location --request GET 'https://adb-366368161648507.7.azuredatabricks.net/api/2.0/clusters/list' --header 'Authorization: Bearer <access-token-here>' | jq .

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2022 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>

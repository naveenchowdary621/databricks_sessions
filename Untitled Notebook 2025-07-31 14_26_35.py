# Databricks notebook source
print("hi")

# COMMAND ----------

# MAGIC %md
# MAGIC My commands
# MAGIC Hello world
# MAGIC
# MAGIC
# MAGIC This is python
# MAGIC

# COMMAND ----------

# MAGIC %md 
# MAGIC ### ## # **Databricks**
# MAGIC

# COMMAND ----------

# MAGIC %fs 
# MAGIC ls 

# COMMAND ----------

# MAGIC %sh
# MAGIC #ls -l
# MAGIC ls -l data-ingestion-with-lakeflow-connect-3.0.2/Includes/Print-Dataset-Copyrights.py
# MAGIC
# MAGIC

# COMMAND ----------

if dbutils.fs.mkdirs("/mnt/raw"): dbutils.fs.ls("/mnt/raw")

# COMMAND ----------



dbutils.fs.ls("/mnt/raw")

# COMMAND ----------

dbutils.widgets.text("parameter_name", "default_value", "Parameter Name")
parameter_value = dbutils.widgets.get("parameter_name")

# COMMAND ----------

dbutils.secrets.get(scope="my_scope", key="db_password")

# COMMAND ----------

# MAGIC %fs
# MAGIC ls /dbfs/data-ingestion-with-lakeflow-connect-3.0.2

# COMMAND ----------

try:    dbutils.fs.ls("/correct-directory-path")
except Exception as e:
    print(f"Error: {e}")


# COMMAND ----------

dbutils.fs.help()
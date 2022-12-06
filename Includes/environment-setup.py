# Databricks notebook source
# MAGIC %run ../Includes/common/environment-functions

# COMMAND ----------

############################################
# Call functions to setup env
############################################
username = get_username()
database_name = create_database(username)
create_table(table_name, file_type, data_path)
# Databricks notebook source
# MAGIC %run ../Includes/common/environment-functions

# COMMAND ----------

############################################
# Call functions to tear down env
############################################
username = get_username()
database_name = get_database_name(username)
remove_database(database_name)
# Databricks notebook source
# MAGIC %run ../../configs/config

# COMMAND ----------

############################################
# Get tags for environment setup
############################################
def get_tags() -> dict:
  return sc._jvm.scala.collection.JavaConversions.mapAsJavaMap(
    dbutils.entry_point.getDbutils().notebook().getContext().tags()
  )

def get_tag(tag_name: str, default_value: str = None) -> str:
  values = get_tags()[tag_name]
  try:
    if len(values) > 0:
      return values
  except:
    return default_value

def get_username() -> str:
  import uuid
  try:
    return dbutils.widgets.get("databricksUsername")
  except:
    return get_tag("user", str(uuid.uuid1()).replace("-", ""))
  
############################################
# Setup Database
############################################
def get_database_name(username:str) -> str:
  import re
  user = re.sub("[^a-zA-Z0-9]", "", username)
  lesson = lesson_name
  databaseName = f"{user}_{lesson}".lower()
  return databaseName

def create_database(username:str) -> str:
  databaseName = get_database_name(username)
  spark.sql("CREATE DATABASE IF NOT EXISTS {}".format(databaseName))
  spark.sql("USE {}".format(databaseName))
  return databaseName

def create_table(table_name:str, file_type:str, file_path:str) -> None:
  """
  Create a table with a given name, type and path
  """
  spark.sql("""CREATE TABLE IF NOT EXISTS {} USING {} OPTIONS (path "{}")""".format(table_name,file_type,file_path))
  return None

############################################
# Remove Database & Tables
############################################
def remove_database(database_name:str) -> None:
  spark.sql("DROP DATABASE IF EXISTS {} CASCADE".format(database_name))
  return None
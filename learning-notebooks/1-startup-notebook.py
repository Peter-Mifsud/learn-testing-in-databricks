# Databricks notebook source
# MAGIC %md
# MAGIC # Testing in Databricks
# MAGIC Within this folder there will be multiple notebooks that will walk you through how to test your code within Databricks.  We will cover testing techniques like unit testing in Python and Pyspark and assertions in SQL to ensure your code is functioning properly.
# MAGIC 
# MAGIC There are many benefits with writing tests for your code, below are a few that [Guru99 highlights](https://www.guru99.com/unit-testing-guide.html):
# MAGIC > 1. Unit tests help to fix bugs early in the development cycle and save costs.
# MAGIC > 2. It helps the developers to understand the testing code base and enables them to make changes quickly
# MAGIC > 3. Good unit tests serve as project documentation
# MAGIC > 4. Unit tests help with code re-use. Migrate both your code and your tests to your new project. Tweak the code until the tests run again.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Environment Setup
# MAGIC Before we jump into the testing, let's create the environment by running the following CMD.  After the CMD is run you should see an output that reads "Environment setup complete, Database and tables mounted"

# COMMAND ----------

# MAGIC %run ./includes/environment-setup

# COMMAND ----------

# MAGIC %md
# MAGIC To ensure you have access to the database and tables that were just created, run the following CMD
# MAGIC 
# MAGIC You should see a dataset with the fields `rating` and `review` along with 5 records displayed

# COMMAND ----------

display(spark.sql("""SELECT * FROM {}.{}""".format(database_name, table_name)).limit(5))
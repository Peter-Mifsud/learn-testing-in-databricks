# learn-testing-in-databricks

This repo will contain examples of how to test your code within the Databricks environment. It will cover testing techniques like unit testing in Python and Pyspark and assertions in SQL to ensure your code is functioning properly.

## Getting Started

There are 2 ways to import this code into Databricks. The first way is through Databricks Repos, but if that feature is not enable in your workspace you can import the files manually through Databrick's UI. We will cover both methods below:

### Getting Started with Databricks Repos

1. First clone the github repo into Databricks. Review how to do this [here](https://docs.databricks.com/repos/git-operations-with-repos.html).
2. Once you have cloned the code, within the `setup` notebook you will see the following CMD, start by running this CMD. This will setup the database and tables required for the notebook.

```bash
%run ../Includes/environment-setup
```

3. Now you are able to proceed through the notebook to learn about testing.
4. When you are finished, run the last CMD to clean up the environment by dropping the tables and database.

```bash
%run ../Includes/environment-cleanup
```

### Getting Started with Databricks UI (Repos Disabled)

1. If Databricks Repos is not enabled, begin by downloading the code from this repository.
   ![download code](https://github.com/Peter-Mifsud/learn-testing-in-databricks/blob/feat/python-testing/Assets/Images/github-download.png?raw=true)
2. Unzip the file and save it locally on your computer
3. Within the Databricks Notebook UI, [follow the directions](https://docs.databricks.com/notebooks/notebook-export-import.html) to upload the entire folder of code that you previously unzipped.
4. Navigate to the `setup` notebook and you will see the following CMD, start by running this CMD. This will setup the database and tables required for the notebook.

```bash
%run ../Includes/environment-setup
```

5. Now you are able to proceed through the notebook to learn about testing.
6. When you are finished, run the last CMD to clean up the environment by dropping the table and database.

```bash
%run ../Includes/environment-cleanup
```

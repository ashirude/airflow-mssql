# airflow-mssql
Analyse Apache Airflow with MSSQL DB. 
https://airflow.apache.org/docs/stable/

# Purpose 
Create a DAG which will connect to mssql server and run simple stored procedure to create table.

# System Requirements 
Airflow doesn't officially support running on Windows. Need a setup on a Linux VM. 
Install Oracle VM VirtualBox on Windows system and setup Ubuntu OS. 

# Installation Guide 
> Install python on Ubuntu :

$ sudo apt update

$ sudo apt-get install python3.6

From sqlAlchemy docs - The SQL Server dialect uses pyodbc as the default DBAPI.
> Install pyodbc :

https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver15 

$ pip3 install pyodbc

> Install Apache-Airflow :

Refer : https://airflow.readthedocs.io/en/1.9.0/project.html 

$ pip3 install apache-airflow[mssql] 

Now Airflow will create the $AIRFLOW_HOME folder and lay an “airflow.cfg” file with defaults that get you going fast.

Inside airflow.cfg file : 
1. Set load_examples = False
2. Set sql_alchemy_conn = mssql+pyodbc://'<login>':'<password>'@'<serverIP>'/'<airflow_test_DB>'?driver={'<pathofodbcDriver>'} 

NOTE : Do not install pymssql. This gives error - 'str' object has no attribute 'tzinfo'. Tried all timezone aware methods but got no success. Probably missed some airflow or sqlAlchemy configurations.
https://airflow.apache.org/docs/stable/timezone.html 

# Setup DAG and Airflow UI
Airflow - Initiation of DB in MSSQL Server. Creates all metadata tables for the application, it is responsible to setup backend

$ airflow initdb

start the web server, default port is 8080

$ airflow webserver -p 8080

1. Edit coonnections inside airflow UI --> Admin --> Connections
2. Create DAG : repo contains an example DAG.  Inside DAG task, Set mssql_conn_id = '<newly_created_connection>'

# Checkpoints while running DAG
•	check if airflow scheduler is running 

•	check if airflow webserver is running 

•	check if all DAGs are set to On in the web UI 

•	check if the DAGs have a start date which is in the past 

•	check if the DAGs have a proper schedule (before the schedule date) which is shown in the web UI 

•	check if the dag has the proper pool and queue. 
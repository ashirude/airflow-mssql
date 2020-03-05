from airflow import DAG
from airflow.operators.mssql_operator import MsSqlOperator
from airflow.utils.dates import days_ago

import datetime
import pytz
import pendulum

import sqlalchemy as sa

from airflow.utils import timezone

execution_date=datetime.datetime.utcnow()
execution_date=timezone.utcnow()

local_tz = pendulum.timezone("UTC")
sa.types.DateTime(timezone=True)
#local_tz.convert(execution_date)

args = dict(
 start_date=datetime.datetime(2019, 1, 1),
)

dag = DAG("dag_run_sql_proc", 
	"Testing running of SQL proc", 
  	schedule_interval = None,
 	default_args=args)

sql_command = """ EXEC dbo.test_airflow """

t1 = MsSqlOperator( task_id = 'task_run_sql_proc',
                    mssql_conn_id = 'mssql_default',
                    sql = sql_command,
                    dag = dag,
                    database = 'airflow_test',
                    autocommit = True)


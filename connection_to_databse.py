import pyodbc

DRIVER_NAME="SQL SERVER"
SERVER_NAME="LAPTOP-IQ5S5SVR\\DEEPAKTIWARY"
DATABASE_NAME="etl_testing_automation"

connection_string = f'''
DRIVER={{{DRIVER_NAME}}};
SERVER={SERVER_NAME};
DATABASE={DATABASE_NAME};
Trust_Connection=yes
uid="sa"
pwd="Laura123#"
'''

conn=pyodbc.connect(connection_string)

cursor=conn.cursor()
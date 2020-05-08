######################################################################
# TOOL FOR GETTING INFO ON DJANGO SQLITE DB
#
# RUNNING:
# DATABASE INFORMATION: `python3 db_tool.py overview`
#
# TABLE INFORMATION: `python3 db_tool.py info table_name`
# Ex: `python3 db_tool.py info projects_project`
# Note that table names are usually in the format `appname_classname`
######################################################################

import sys
import sqlite3
import pandas as pd

# setup db paths and connections
db_path = 'PersonalSite/db.sqlite3'
option = sys.argv[1]
conn = sqlite3.connect(db_path)

if option == 'info':

    table_name = sys.argv[2]

    # obtaining all the tables in the sqlite db
    try:
        df = pd.read_sql('SELECT * FROM ' + table_name, conn)
        print('--------------------------------------------------------')
        print('Table Description:')
        print(df.dtypes)
        print('--------------------------------------------------------')
        print('Shape:')
        print(df.shape)
        print('--------------------------------------------------------')
        print(df)
        print('--------------------------------------------------------')
    except:
        print('No such table, use `python3 db_tool.py overview` to see tables')

if option == 'overview':

    # setup cursor and query
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = c.fetchall()

    print('--------------------------------------------------------')
    for table in tables:
        print(table)
    print('--------------------------------------------------------')

conn.close()

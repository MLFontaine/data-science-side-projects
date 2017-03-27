#mpg_analysis commands

import MySQLdb as mdb
import sys
import pandas as pd
import pandas.io.sql

#import mysql.connector as sql
#db_con = sql.connect(host='localhost', database='mpg_db', option_files=os.path.expanduser('~/.my.cnf')) #couldnt get this to read my password, only got username for some reason

con = mdb.connect(host='localhost', db='mpg_db', read_default_file='~/.my.cnf')



gas_data = pandas.read_sql("SELECT * FROM mpg_table", con)

print(type(gas_data)) #shows type as pandas dataframe





#con = mdb.connect(host='localhost', db='mpg_db', read_default_file='~/.my.cnf');
#    
#with con:
#    
#    cur = con.cursor(mdb.cursors.DictCursor)
#    cur.execute("SELECT * FROM mpg_table LIMIT 4")
#    
#    rows = cur.fetchall()
#    
#    for row in rows:
#        print row["thedate"], row["mpg"]
#
#if con:
#    con.close()

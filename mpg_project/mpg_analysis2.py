#mpg_analysis commands

import MySQLdb as mdb
import sys
import pandas as pd
import pandas.io.sql
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

#import mysql.connector as sql
#db_con = sql.connect(host='localhost', database='mpg_db', option_files=os.path.expanduser('~/.my.cnf')) #couldnt get this to read my password, only got username for some reason

con = mdb.connect(host='localhost', db='mpg_db', read_default_file='~/.my.cnf')



gas_data = pandas.read_sql("SELECT * FROM mpg_table", con)

print(type(gas_data)) #shows type as pandas dataframe

mpgs=pd.DataFrame(gas_data, columns=['mpg']) #mpg column, or just gas_data['mpg']

print(np.mean(mpgs))

ts = pd.Series(gas_data['mpg'], index=gas_data['thedate'])
ts = ts.cumsum()
plt.show()




#visualization example, http://pandas.pydata.org/pandas-docs/stable/visualization.html

#>>> ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
#>>> ts = ts.cumsum()
#>>> ts.plot()
#<matplotlib.axes._subplots.AxesSubplot object at 0x10ec77a10>
#>>> plt.show()


#Access database with cursor, not a pandas dataframe data structure

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

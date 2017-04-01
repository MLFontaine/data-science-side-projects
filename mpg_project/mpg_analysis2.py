#mpg_analysis commands

import MySQLdb as mdb
import sys
import pandas as pd
import pandas.io.sql
import numpy as np
from numpy import log
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn import linear_model
import matplotlib
import matplotlib.pyplot as plt
plt.style.use('ggplot')

#import mysql.connector as sql
#db_con = sql.connect(host='localhost', database='mpg_db', option_files=os.path.expanduser('~/.my.cnf')) #couldnt get this to read my password, only got username for some reason

con = mdb.connect(host='localhost', db='mpg_db', read_default_file='~/.my.cnf')

gas_data = pandas.read_sql("SELECT * FROM mpg_table", con)

con.close()

print(type(gas_data)) #shows type as pandas dataframe

mpgs=pd.DataFrame(gas_data, columns=['mpg']) #mpg column, or just gas_data['mpg']

print(np.mean(mpgs))

dateplot = plt.plot_date(matplotlib.dates.date2num(gas_data['thedate']), gas_data['mpg'], '-') #time-mpg
plt.ylabel('miles per gallon')
plt.show(dateplot)

mpdmpgplot = plt.scatter(gas_data['mpd'], gas_data['mpg']) #mpd-mpg
plt.ylabel('miles per gallon')
plt.xlabel('miles per day')
plt.show(mpdmpgplot)

#linear regression
mpg_data = gas_data['mpg']
mpd_data = gas_data['mpd']
mpd_data = sm.add_constant(mpd_data)
regression1 = sm.OLS(mpg_data, mpd_data).fit()
print(regression1.summary())

#alternative regression calculation
regression2 = smf.ols(formula = 'mpg ~ mpd', data = gas_data).fit()
print(regression2.summary())

#print(regression2.params) #gives coefficients

#3rd linear regression from scikit-learn
mpg_data2 = gas_data[['mpg']]
mpd_data2 = gas_data[['mpd']]
sk_regr = linear_model.LinearRegression()
sk_regr.fit(mpd_data2, mpg_data2)
print(sk_regr.coef_)
print(sk_regr.intercept_)
print(sk_regr.score(mpd_data2, mpg_data2))

#log transformation, gived worse R^2
gas_data['log_mpd'] = log(gas_data['mpd'])
gas_data['log_mpg'] = log(gas_data['mpg'])

log_lm = smf.ols(formula = 'log_mpg ~ log_mpd', data = gas_data).fit()

print(log_lm.summary())


##plt.scatter(gas_data['log_mpd'], gas_data['log_mpg'])
#plt.show()

print('end')


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

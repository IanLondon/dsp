# Hint:  use Google to find python function
import datetime as dt

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

date_start, date_stop = [dt.datetime.strptime(d, '%m-%d-%Y') for d in (date_start,date_stop)]

day_diff = (date_stop-date_start).days
print "The difference is {} days".format(day_diff)

####b)  
date_start = '12312013'  
date_stop = '05282015'  

date_start, date_stop = [dt.datetime.strptime(d, '%m%d%Y') for d in (date_start,date_stop)]

day_diff = (date_stop-date_start).days
print "The difference is {} days".format(day_diff)

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

date_start, date_stop = [dt.datetime.strptime(d, '%d-%b-%Y') for d in (date_start,date_stop)]

day_diff = (date_stop-date_start).days
print "The difference is {} days".format(day_diff)

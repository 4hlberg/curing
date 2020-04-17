import sqlite3
from datetime import datetime, timedelta

''' input average of readings the last 12 hours in to a table and clean up readings older than 7 days '''
db_file = '/home/pi/testscripts/curing'

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn


if __name__ == '__main__':
   ''' get averages from readings db '''
   conn = create_connection(db_file)
   cur = conn.cursor()
   datetime_now = str(datetime.now() - timedelta(hours=12))
   cur.execute(f"select avg(temp), avg(humid) from readings where reading_time >= '{datetime_now}'" )
   avg_readings = cur.fetchall()

   print(avg_readings)


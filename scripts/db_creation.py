import sqlite3

def insert(table_name):
    conn =  sqlite3.connect("curing")
    cur = conn.cursor()
    settings_sql = ''' INSERT INTO settings (temp_max, temp_min, temp_panic, humid_max, humid_min, humid_panic, humid_duty_cycle, fan_duty_cycle) values (12, 4, 14, 85, 65, 60, 3, 30)'''
    cur.execute(settings_sql)
    conn.commit()

def create(table_name):
    conn =  sqlite3.connect("curing")
    cur = conn.cursor()
    if table_name.lower() == 'settings':
        create_table = ''' CREATE TABLE settings (id integer primary key autoincrement, temp_max float, temp_min float, temp_panic float, humid_max float, humid_min float, humid_panic float, humid_duty_cycle integer, fan_duty_cycle integer)''' 
        cur.execute('''DROP TABLE if exists settings''')   
        conn.commit()
    elif table_name.lower() == 'readings':
        create_table = ''' CREATE TABLE readings (id integer primary key autoincrement, temp float, humid float, reading_time datetime, failure integer, sensor_name text) ''' 
    elif table_name.lower() == 'heartbeat':
        create_table = ''' CREATE TABLE heartbeat (id integer primary key autoincrement, last_heartbeat datetime, mode text)'''
    elif table_name.lower() == 'averages':
        create_table = ''' CREATE TABLE averages (id integer primary key autoincrement, date datetime, temp_average float, humid_average float) '''
    else:
        print("No option chosen")
    conn.execute(create_table)
    return(print(f"Name of the table is {table_name}"))
if __name__ == '__main__':
    print("================= Welcome to the table creator =================")
    print("================= Input the name of the table you want created ================" )
    table_name = input("Input name of table you want created here: ")
    try:
        if table_name.lower() == 'settings':
            create(table_name)
            print(f"created table {table_name}")
            insert(table_name)
        else:
            create(table_name)

    except Exception as e:
        print (e)

#!/usr/bin/python3.u7

import Adafruit_DHT
import datetime
import sqlite3
import os
import RPi.GPIO as GPIO
import sys

DHT_SENSOR = Adafruit_DHT.DHT22

DHT_PIN = 4
db_file = "/home/pi/curing/curing"
get_settings_sql = ''' SELECT * FROM SETTINGS '''
write_readings_sql = ''' INSERT INTO readings (temp, humid, reading_time, failure, sensor_name) VALUES (?, ?, ?, ?, ?)''' 
write_heartbeat_sql = ''' INSERT INTO heartbeat (last_heartbeat, mode) VALUES (?, ?)'''

GPIO.setmode(GPIO.BCM)

''' list with pin numbers not neccessarily the ones you might be using'''

PINLIST = [22, 27, 17, 18]
FRIGE_PIN = 22
HUMID_PIN = 27
FAN_PIN = 17
HEAT_PIN = 18

#loop through pins and set mode and state to 'high' 'high' means not on as far as i've understood

for i in PINLIST:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def insert_reading(conn, reading):
    ''' PRINT LAST READINGS TO DB '''
    cur = conn.cursor()
    cur.execute(write_readings_sql, reading)
    conn.commit()
    return cur.lastrowid 

def write_heartbeat(conn):
    ''' INSERT SIGN OF LIFE IN TO TABLE IN DB '''
    timestamp =  datetime.datetime.now()
    cur = conn.cursor()
    cur.execute(read_heartbeat_sql)
    last_heartbeat = cur.fetchall()
    ''' say something about last time it was written to '''
    cur.execute(write_heartbeat_sql)
    return cur.lastrowid
    
def get_settings(conn):
    ''' GET SETTINGS FROM DB, TO ACT UPON '''
    cur = conn.cursor()
    cur.execute(get_settings_sql)
    settings = cur.fetchall()
    table_id, temp_max, temp_min, temp_panic, humid_max, humid_min, humid_panic, humid_duty_cycle, fan_duty_cycle = settings[0]
    return(temp_max, temp_min, temp_panic, humid_max, humid_min, humid_panic, humid_duty_cycle, fan_duty_cycle, temp_delta, humid_delta)

def determine_temp(temp_reading, temp_min, temp_max, temp_delta):
    ''' this is probably not enough to controll all states, depending on the design if there are concurrent tasks... but may also work fine NOT TESTED'''
    if temp_reading + temp_delta < temp_max and temp_reading - temp_delta > temp_min:
        fridge_mode = 'ON'
    elif temp_reading + temp_delta > temp_max:
        fridge_mode = 'ON'
    elif temp_reading - temp_delta < temp_min:
        fridge_mode = 'OFF'
    else:
        fridge_mode = 'ON'
    return (fridge_mode)
    
def determine_humid(humid_reading, humid_min, humid_max, humid_delta):
    if humid_reading + humid_delta > humid_max:
        humidity_mode = 'OFF'
    elif humid_min < (humid_reading - humid_delta) and (humid_reading + humid_delta) < humid_max:
        humidity_mode = 'OFF'
    elif humid_reading - humid_delta < humid_min:
        humidity_mode = 'ON'
    return (humidity_mode)

def get_sensor_readings(): 
    ''' GET THE READINGS FROM SENSOR

    I'd rather assume to hot than too cold, if readings are out of wack '''

    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is None and temperature is None:
        sys.stderr.write("Failed to get a reading, forcing 10 degrees and 80% humidity\n")
        humid_reading = 80
        temp_reading = 10
        last_reading_time = datetime.datetime.now()
        failure = 1
        
    else:
        temp_reading = "{0:0.1f}".format(temperature)
        humid_reading = "{0:0.1f}".format(humidity)
        last_reading_time = datetime.datetime.now()
        failure = 0
        
    return(temp_reading, humid_reading,last_reading_time, failure, "DHT22")

if __name__ == '__main__':
    '''create connection to the database'''
    conn = create_connection(db_file)
    ''' Write to heartbeat to make sure I'm alive '''
    write_heartbeat(conn)
    ''' Get sensor readings '''
    readings = get_sensor_readings(conn)
    reading_id = insert_reading(conn, readings)
    print(reading_id)
    settings = get_settings(conn)
    ''' compare settings to the readings and decide if action needs to be taken. Starting with temperature'''
    fridge_mode = determine_temp(temp_reading, temp_min, temp_max, temp_delta)
    ''' Set relay for fridge to the correct mode GPIO.LOW means ON and GPIO.HIGH means OFF '''
    if fridge_mode == 'ON'
        GPIO.output(FRIDGE_PIN, GPIO.LOW)
    ''' create function for humidity, will have to check if the fan can be on at the same time, otherwise check for if fan is running must be implemented '''
    
    humidity_mode = determine_humid(humid_reading, humid_min, humid_max, humid_delta)

    if humidity_mode == 'ON'
        GPIO.output(HUMID_PING, GPIO.LOW)
    print(''' I've done what you wanted, now I will sleep''')

    # humidity_mode = 
    #if temp_reading + temp_delta < temp_max:

    #    print(f"Temperature in fridge is {temp_reading} standing by")
    #    ''' check humidity '''
    #    if humid_reading + humid_delta < humid_max:
    #        print(f"Humidity is {humid_reading}, standing by")
    

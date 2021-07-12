import os
import glob
import time
import sys
import datetime
from influxdb import InfluxDBClient

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

host = ""
port = 8086
user = ""
password = ""
dbname = ""

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

client = InfluxDBClient(host, port, user, password, dbname)
measurement = "pool_temperature" # the name of the measurement you'd like to use
location = "poolside"

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    iso = time.ctime()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
    data = [
        {
          "measurement": measurement,
              "tags": {
                  "location": location,
              },
              "fields": {
                  "temperature" : temp_c
              }
          }
        ]
    client.write_points(data)
    return temp_c

read_temp()
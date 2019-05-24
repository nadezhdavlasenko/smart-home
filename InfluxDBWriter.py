from influxdb import InfluxDBClient
import time
import Adafruit_DHT as dht
from time import sleep
import random

print("Going to connect to DB")
dbClient = InfluxDBClient('192.168.1.105', 8086, '', '', 'smarthome')

# Set DATA pin

DHT = 4
try:
    while True:
        # Read Temp and Hum from DHT22
        print("Going to read read_retry")
        h, t = dht.read_retry(dht.DHT22, DHT)

        loginEvents = [{"measurement": "timeseries",

                        "fields":

                            {

                                "Humidity": f"{h}",

                                "Temperature": f"{t}",

                            }

                        }

                       ]
        print("Going to write to DB")
        dbClient.write_points(loginEvents)

        print("Going to sleep 1s ...")
        sleep(1)  # Wait 5 seconds and read again

except KeyboardInterrupt:
    print("KeyboardInterrupt")

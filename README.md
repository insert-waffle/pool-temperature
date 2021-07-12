# Pool Temperature Monitor

Pool temperature monitoring using DS18B20 (waterproof) temperature sensor connected to a Raspberry Pi

## Using the script

Adjust the InfluxDB connection settings at the top of `measure_temperature.py` file to fit your setup and then run with one of the options listed below.

### Run using crontab

1. Correctly connect the sensor to the Raspberry Pi

    NOTE: I am not providing support on how to connect the DS18B20 sensor to the Raspberry Pi, a simple Google search will help you out.

2. Install the InfluxDB client for library from Python.

    `pip3 install influxdb`

3. Run the script.

    `python3 ./measure_temperature.py`

4. Modify crontab to run the script every hour

    Edit crontab using your favorite editor with `crontab -e` and add the following line: `0 */1 * * * /usr/bin/python3 /path/to/script/measure_temperature.py`, this way the cronjob runs every hour.
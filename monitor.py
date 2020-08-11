import psutil
import os
import sys
import json

'''
        What we want to collect:
            - Temps - This may be unclear until we have a better idea of which servers have which temp sensors
            - disks - This may also be unclear because the configuration is not yet known.
            - CPU stats - Average system load - Average load percpu
        '''


def format_data(values):

    #We'll do it ugly, and then we'll do it less ugly
    for value in values:
        print(values[value])
        print(type(values[value]))
        print('---------------------------------------------')

        value_type = type(values[value])
        return_dict = {
            'cpu': {},
            'ram': {},
            'disk': {},
            'temps': {},
            'fans': {}
        }

        #our only tuple is cpu_load_avg
        if value_type == tuple:
            for sub_value in values[value]:
                print(sub_value)
                print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')

    
if __name__ == "__main__":
    #our values
    values = {
        "cpu_freq": psutil.cpu_freq(),
        "cpu_count": psutil.cpu_count(),
        "cpu_load_avg": psutil.getloadavg(),
        "cpu_load_per_cpu": psutil.cpu_percent(percpu=True),
        "virtual_memory": psutil.virtual_memory(),
        "swap_memory": psutil.swap_memory(),
        # "disk_usage": psutil.disk_usage(path), <--- We need a path to call this properly
        "disk_partitions": psutil.disk_partitions(),
        "disk_io_counters": psutil.disk_io_counters(),
        "temps": psutil.sensors_temperatures(fahrenheit=True),
        "fans": psutil.sensors_fans()
    }

    format_data(values)
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

def format_lists(list):
    print(list, '00000000000000000 -------------------- 00000000000000000')
    return list

#If I can write this correctly, then I'll probably be able to 
#Reuse it for these nested values...
def format_data(legal_actions):

    #We'll do it ugly, and then we'll do it less ugly
    return_dict = {}
    for value in legal_actions:
        print(legal_actions)
        print(type(legal_actions[value]))
        print('---------------------------------------------')

        value_type = type(legal_actions[value])

        #We return a ton of different types when we ask for this stuff.
        #We need to filter by type so we can get something useful out of here.
        if value_type == int:
            return_dict[value] = legal_actions[value]
        elif value_type == list:
            if type(legal_actions[value][0]) == float:
                return_dict[value] = legal_actions[value]
            else:
                format_lists(legal_actions[value])
        elif value_type == tuple:
            #our only tuple is cpu_load_avg
            value_array = []
            for sub_value in legal_actions[value]:
                value_array.append(sub_value)
            return_dict[value] = value_array
        elif value_type == dict:
            format_data(legal_actions[value])

    print(return_dict)
    return return_dict

    
if __name__ == "__main__":
    #our values
    legal_actions = {
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

    format_data(legal_actions)
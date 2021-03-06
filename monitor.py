import psutil
import time

'''
        What we want to collect:
            - Temps - This may be unclear until we have a better idea of which servers have which temp sensors
            - disks - This may also be unclear because the configuration is not yet known.
            - CPU stats - Average system load - Average load percpu
        '''


#TODO:
#BRENNAN YOU NEED TO COMPLETELY REWRITE THIS LOL
#THIS NEEDS TO BE TOTALLY REFACTORED IN A WAY THAT BETTER SUPPORTS
#THE "HISTORY" ASPECT.
#OR MAYBE IT DOESN'T, BUT THEN WE ARE GOING TO NEED TO BASICALLY
#COMPLETELY REFORMAT THE DATA IN THE VIEW CLASS WHEN WE WANT TO ACTUALLY SHOW IT
#ALSO WHAT COULD POSSIBLY TAKE ADVANTAGE OF THE DATA IN ITS CURRENT FORMAT??
# 
#What we need:
# { "results": {
        #Over time.
#       "cpu_freq_core_1": {1.08, 2.20, 1.00, 1.00}
#       "cpu_freq_core_2": {1.08, 2.20, 1.00, 1.00}
#       "cpu_freq_core_3": {1.08, 2.20, 1.00, 1.00}
#       etc etc...
#       "timestamps": {'1602364444.3047254', '1602364444.3047254', '1602364444.3047254'}
# }}

# Shitty way to make this happen. We just need to remove the value out of the list.
#Way overcomplicated.
def format_lists(list_to_format):
    list_var = format_tuples(list_to_format[0])
    return list_var

#We have tuples, and custom types that are basically just tuples. 
#Get the information out of them and into a list (along with everything else)
#so that we can ingest it later.
def format_tuples(list_to_format):
    value_array = []
    for sub_value in list_to_format:
        value_array.append(sub_value)
    return value_array

#If I can write this correctly, then I'll probably be able to 
#Reuse it for these nested values...
def format_data(legal_actions):

    #We'll do it ugly, and then we'll do it less ugly
    return_dict = {}
    for value in legal_actions:

        value_type = type(legal_actions[value])
        #A bit of a weird approach, but we have all of these custom types that are basically tuples....
        #So treat them as such.
        tuples = [ tuple, psutil._common.scpufreq, psutil._pslinux.svmem, psutil._common.sswap, psutil._pslinux.sdiskio ]

        #We return a ton of different types when we ask for this stuff.
        #We need to filter by type so we can get something useful out of here.
        if value_type == int or value_type == float:
            return_dict[value] = legal_actions[value]
        elif value_type == list:
            if type(legal_actions[value][0]) == float:
                return_dict[value] = legal_actions[value]
            else:
                return_dict[value] = format_lists(legal_actions[value])
        elif value_type == dict:
            return_dict[value] = format_data(legal_actions[value])
        elif value_type in tuples: 
            return_dict[value] = format_tuples(legal_actions[value])
        else:
            raise ValueError('[[ERR] monitor.format_data] Unknown value type of:', value_type)

    return return_dict

def fetch_data():
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
        "fans": psutil.sensors_fans(),
        "timestamp": time.time()
    }

    return format_data(legal_actions)
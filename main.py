import os
import sys
import json

import monitor
from view import View

legal_options = [ '-v', '-h' ]
arguments_supplied = False
should_print_report = False
should_include_history = False

#init
#Read our config file
#...or just pass in our options....? <--- probably this. Dunno what options I was thinking of, but this will probably be fine.
if len(sys.argv) > 1:
    print('Option {0} was passed in.'.format(sys.argv[1]))
    arguments_supplied = True
    if sys.argv[1] not in legal_options:
        raise Exception('[ERROR] Invalid option provided. Continuing without options.')
    elif '-v' in sys.argv:
        should_print_report = True
    elif '-h' in sys.argv:
        should_include_history = True

if __name__ in "__main__":

    #Erase our file so that it's blank and ready for us, unless we want to keep the history.
    if not should_include_history:
        pass
        # open('test.json', 'w').close()

    #serve it, if we need to.
    if should_print_report:
        View()

    #collect data
    data = monitor.fetch_data()
    # print(data)

    #store it
    #I really wish there was a better solution for this.
    #The best we've got is opening it twice?? Once to read it and once to write it? Tf?
    new_data = { data['timestamp']: data }
    with open('test.json', 'r+') as file_to_use:
        try:
            json_object = json.load(file_to_use)
        except Exception as e:
            #A bit of a bruh moment
            json_object = { 'results': {} }
        json_object['results'][data['timestamp']] = data

    with open('test.json', 'w') as file_to_use:
        file_to_use.write(json.dumps(json_object))

    #We're done, so let's quit successfully.
    exit(0)

import os
import sys
import json

import monitor
from view import View

legal_options = [ '-v' ]
arguments_supplied = False
should_print_report = False

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

if __name__ in "__main__":

    #collect data
    data = monitor.fetch_data()
    # print(data)

    #store it
    new_data = { data['timestamp']: data }
    with open('test.json', 'r+') as file_to_use:
        try:
            json_object = json.load(file_to_use)
            print(json_object['results'])
            json_object['results'][data['timestamp']] = data
            print('????????????', json_object)
            json.dump(json_object, file_to_use)
        except ValueError as e:
            print('uh oh... ', e)

    #serve it, if we need to.
    if arguments_supplied and should_print_report:
        View(data)
        raise NotImplementedError()

    #We're done, so let's quit successfully.
    exit(0)

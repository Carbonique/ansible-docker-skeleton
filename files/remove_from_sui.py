#!/usr/bin/env python3

import json
import sys

def read_json(filename):
  with open(filename, 'r') as f:
    return json.load(f)

def key_value_lookup(object, key, value):
  return (key, value) in object.items()

def app_exists(filename, app_name):
  with open(filename, 'r') as f:
    data = read_json(filename) 

    for apps in data['apps']: 
      if key_value_lookup(apps, 'name', app_name) == True:
        return True

def remove_json_object(filename, app_name):
    data = read_json(filename) 

    for a in data['apps'][:]:
        if (a['name'] == app_name):
            data['apps'].remove(a)
            return data


def remove_app_from_json(filename, app_name):

    if app_exists(filename, app_name):

        data = remove_json_object(filename, app_name)

        with open(filename, 'w') as outfile:
            json.dump(data, outfile)
        return

    print('App ' + app_name + ' not included in ' + filename)
    sys.exit(1)


remove_app_from_json(sys.argv[1], sys.argv[2])




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

def write_json(filename, data):
  with open(filename, 'w') as f:
      json.dump(data, f, indent=4) 

def add_app_to_json(filename, app_name, url, icon):

  if app_exists(filename, app_name):

    print('App ' + app_name + ' already included in ' + filename)
    sys.exit(1)
    
    return 

  data = read_json(filename)
  data['apps'].append({"name": app_name ,
                      "url": url ,
                      "icon": icon })
  write_json(filename, data)

add_app_to_json(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
# apps.json filepath, app_name, url, icon



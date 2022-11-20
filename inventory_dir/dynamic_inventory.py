#!/usr/bin/env python3
'''
Sample custom dynamic inv setting addresses 
'''

import argparse
try:
    import json
except ImportError:
    import simplejson as json


class DynamicInv(object):

    list_of_hosts = [112,134,151]

    def __init__(self):
        self.inventory = {
            "_meta": {
                "hostvars": {}
            },
            "servers": {"hosts": []}
        } 
        self.read_cli_args()

        #--list
        if self.args.list:
            self.inventory = self.dynamic_inv()
        #--host [hostname]
        elif self.args.host:
            # not implemented
            self.inventory = self.empty_inv()
        else:
            self.inventory = self.empty_inv()
        
        print(json.dumps(self.inventory))

    def dynamic_inv(self):
        
        for i in self.list_of_hosts:
            host = f"server{i}"
            self.inventory["_meta"]["hostvars"][host] = {
                "ansible_host": f"192.168.0.{i}",
                "host_var": host
            }
            self.inventory["servers"]["hosts"].append(host)
        return self.inventory

    #Empty inventory for testing
    def empty_inv(self):
        return {'_meta': {'hostvars': {}}}
        #return self.dynamic_inv()
        
    # Read the commnand line args passed to the script.
    def read_cli_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--list', action = 'store_true')
        parser.add_argument('--host', action = 'store')
        self.args = parser.parse_args()
# Get the inventory
DynamicInv()

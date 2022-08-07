#!/usr/bin/env python3
import json

inventory = {
    "_meta": {
        "hostvars": {}
    },
    "servers": {"hosts": []}
}
for i in range(5,7,1):
    host = f"server{i}"
    inventory["_meta"]["hostvars"][host] = {
        "ansible_host": f"192.168.64.{i}",
        "host_var": host
    }
    inventory["servers"]["hosts"].append(host)
print(json.dumps(inventory))

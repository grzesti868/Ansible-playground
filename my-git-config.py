#! /usr/bin/python
#Set basic setting into git config file
import os
cmd = '''
git config --global user.name "Greg"
git config --global --add user.email "ansible@localhost.local"
echo 'Done!'
'''
os.system(cmd)


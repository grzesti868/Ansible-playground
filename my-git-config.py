#! /usr/bin/python
import os
cmd = '''
git config --global user.name "Greg"
git config --global --add user.email "ansible@localhost.local"
'''
os.system(cmd)


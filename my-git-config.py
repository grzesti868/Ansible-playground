#! /usr/bin/python
import os
cmd = '''
git config --global user.name "Greg"
git config --global --add user.mail "ansible@localhost.local"
'''
os.system(cmd)


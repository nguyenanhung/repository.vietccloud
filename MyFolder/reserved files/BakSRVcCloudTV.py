#!/usr/bin/python

import os

FileName = os.path.expanduser(r'~\Documents\GitHub\repository.viplist\MyFolder\cCloudTV.m3u')

filedata = None
with open(FileName, 'r') as file :
    filedata = file.read().replace(',Welcome to cCloudTV.ORG', ',[COLOR magenta]Backup Server - Welcome to cCloudTV.ORG').replace('(Announcement) (US) (English)', '(Announcement) (US) (English)[/COLOR]')
with open(FileName, 'w') as file:
    file.write(filedata)
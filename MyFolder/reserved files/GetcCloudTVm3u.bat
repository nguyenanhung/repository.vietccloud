@echo off
cd %userprofile%\Documents\GitHub\repository.viplist\MyFolder
wget --no-check-certificate -O cCloudTV.m3u http://kodi.ccld.io
python %userprofile%\Documents\GitHub\repository.viplist\MyFolder\BakSRVcCloudTV.py
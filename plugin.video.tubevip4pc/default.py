# -*- coding: utf-8 -*-

import urllib, urllib2, sys, re, os, json
import xbmc, xbmcgui, xbmcplugin, xbmcaddon

plugin_handle = int(sys.argv[1])
mysettings = xbmcaddon.Addon(id = 'plugin.video.tubevip4pc')
profile = mysettings.getAddonInfo('profile')
home = mysettings.getAddonInfo('path')
fanart = xbmc.translatePath(os.path.join(home, 'fanart.jpg'))
iconpath = xbmc.translatePath(os.path.join(home, 'resources/icons'))
icon = xbmc.translatePath(os.path.join(home, 'icon.png'))

dataFile = open(xbmc.translatePath(os.path.join(home, 'resources', 'json', 'data.json')))
data = json.loads(dataFile.read())
dataFile.close()

def platform():
	if xbmc.getCondVisibility('system.platform.android'):
		return 'android'
	elif xbmc.getCondVisibility('system.platform.linux'):
		return 'linux'
	elif xbmc.getCondVisibility('system.platform.windows'):
		return 'windows'
	elif xbmc.getCondVisibility('system.platform.osx'):
		return 'osx'
	elif xbmc.getCondVisibility('system.platform.atv2'):
		return 'atv2'
	elif xbmc.getCondVisibility('system.platform.ios'):
		return 'ios'

def main():
	if platform() == 'windows' or platform() == 'osx' or platform() == 'linux':
		addDir('[COLOR yellow][B]For Windows, Macintosh, or Linux PC only.[/B][/COLOR][COLOR lime][B] PC must have[/B][/COLOR]', 'info', None, icon, fanart)
		addDir('[COLOR yellow][B]Kodi Chrome Launcher [/B][/COLOR][COLOR lime][B]and [/B][/COLOR][COLOR yellow][B]Google Chrome [/B][/COLOR][COLOR lime][B]installed.[/B][/COLOR]', 'info', None, icon, fanart)
		for mainmenu in data['channels']:
			name = mainmenu['name'].encode('utf-8')
			thumb = ('%s/%s') % (iconpath, mainmenu['thumb'])
			addDir(name, str(mainmenu['channel']), 1, thumb, thumb)
	else:
		xbmcgui.Dialog().ok('Tube VIP for PC', '[COLOR magenta]This [B]Tube VIP for PC[/B] add-on can only be used on Windows, Macintosh, or Linux PC.[/COLOR]', '', 'Chỉ dùng được [B]Tube VIP for PC[/B] add-on trong máy Windows, Macintosh, Linux PC.')
		sys.exit()       

def index(url):
	for submenu in data['channels'][int(url)]['items']:
		name = submenu['title'].encode('utf-8')
		thumb = submenu['thumb']
		addDir(name, submenu['link'], None, thumb, thumb)

def get_params():
	param = []
	paramstring = sys.argv[2]
	if len(paramstring)>= 2:
		params = sys.argv[2]
		cleanedparams = params.replace('?', '')
		if (params[len(params)-1] == '/'):
			params = params[0:len(params)-2]
		pairsofparams = cleanedparams.split('&')
		param = {}
		for i in range(len(pairsofparams)):
			splitparams = {}
			splitparams = pairsofparams[i].split('=')
			if (len(splitparams)) == 2:
				param[splitparams[0]] = splitparams[1]
	return param

def addDir(name, url, mode, iconimage, fanart):
	u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name) + "&iconimage=" + urllib.quote_plus(iconimage)
	ok = True
	liz = xbmcgui.ListItem(name, iconImage = "DefaultFolder.png", thumbnailImage = iconimage)
	liz.setInfo( type = "Video", infoLabels = { "Title": name } )
	liz.setProperty('fanart_image', fanart)
	if 'plugin.program.chrome.launcher' in url:
		u = url
	ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz, isFolder = True)
	return ok

params = get_params()
url = None
name = None
mode = None
iconimage = None

try:
	url = urllib.unquote_plus(params["url"])
except:
	pass
try:
	name = urllib.unquote_plus(params["name"])
except:
	pass
try:
	mode = int(params["mode"])
except:
	pass
try:
	iconimage = urllib.unquote_plus(params["iconimage"])
except:
	pass  

print "Mode: " + str(mode)
print "URL: " + str(url)
print "Name: " + str(name)
print "iconimage: " + str(iconimage)

if mode == None or url == None or len(url) < 1:
	main()

elif mode == 1:
	index(url)

xbmcplugin.endOfDirectory(plugin_handle)
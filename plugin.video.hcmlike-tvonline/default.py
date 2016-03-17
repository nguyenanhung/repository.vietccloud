import urllib,urllib2,unicodedata,re
# import time

# TODO: Uncomment!
import xbmcplugin,xbmcgui,xbmc,xbmcaddon,os.path

# TODO: XBMC - Fake APIs!
# ================================================

# def addDir(name,url,mode,iconimage):
# 	print('------------------------')
# 	print(name)
# 	print('- URL: ' + url)
# 	print('- MODE: ' + str(mode))
# 	print('- Icon: ' + iconimage)
# 	print('------------------------ \n')

# def endOfItemList():
# 	return True

# def playVideo(name,url,iconimage):
# 	ok=True
# 	print('---------PlayVidoe---------------')
# 	print(name)
# 	print('- URL: ' + url)
# 	print('- Icon: ' + iconimage)
# 	print('------------------------ \n')
# 	return ok
# ================================================

myaddon = xbmcaddon.Addon()
home    = xbmc.translatePath(myaddon.getAddonInfo('path') ).decode("utf-8")
fanart  = xbmc.translatePath(os.path.join(home, 'fanart.jpg'))

# ------------------- Utils ----------------------
def encodeURL(url):
	return urllib.quote(url, safe="%/:=&?~#+!$,;'@()*[]")

def getPageContent(url):
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0')
	response=urllib2.urlopen(req)
	content=response.read()
	response.close()
	return content

def getTitle(icon, infoList):
	for (thumb, title) in infoList:
		if icon == thumb:
			return title
	return ''

# TODO: Uncomment!
# This function should be put after adding items.
def endOfItemList():
	 # Display channels as thumbnail as default.
	 xbmc.executebuiltin('Container.SetViewMode(%d)' % 500)
	 # End of directory.
	 xbmcplugin.endOfDirectory(int(sys.argv[1]))

# ------------------------------------------------

# mode = 1
def INDEX(url):
	content=getPageContent(url)

	pattern='\s.*<a class=.+ .+ data-original="(.+?)"\s*><img alt="" width="140" height="92" src="(.+?)"></a>'
	links=re.compile(pattern).findall(str(content))
	pattern='\s.*<option  value=".+?" data-imagesrc="(.+?)">(.+?)</option>'
	links2=re.compile(pattern).findall(str(content))

	# Add dir
	for (link, icon) in links:
		title = getTitle(icon, links2)
		if title != '':
			links2.remove((icon, title))
			addDir(title,link,2,icon)
	endOfItemList()

# mode = 2
def VIDEOLINKS(url,name,thumbnail):
	ok=True
	content=getPageContent(url)

	# Process to get m3u link
	pattern = 'id="play_video" data-source="(.+?)"'
	urls=re.compile(pattern).findall(str(content))

	m3uLink = '';
	if len(urls) > 0:
		m3uLink = urls[0]

	# time.sleep(0.005)	# for loading more smooth but it delay!
	playVideo(name,m3uLink,thumbnail)
	return ok

def get_params():
	param=[]
	paramstring=sys.argv[2]
	if len(paramstring)>=2:
		params=sys.argv[2]
		cleanedparams=params.replace('?','')
		if (params[len(params)-1]=='/'):
			params=params[0:len(params)-2]
		pairsofparams=cleanedparams.split('&')
		param={}
		for i in range(len(pairsofparams)):
			splitparams={}
			splitparams=pairsofparams[i].split('=')
			if (len(splitparams))==2:
				param[splitparams[0]]=splitparams[1]
	return param

# TODO: Uncomment!
def playVideo(name,url,iconimage):
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
	liz.setInfo( type="Video", infoLabels={ "Title": name } )
	xbmc.Player().play(url, liz)
	return ok

def addLink(name,url,iconimage):
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
	liz.setInfo( type="Video", infoLabels={ "Title": name } )
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
	return ok

# TODO: Uncomment!
def addDir(name,url,mode,iconimage):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&thumbnail="+urllib.quote_plus(iconimage)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setInfo( type="Video", infoLabels={ "Title": name } )
	liz.setProperty('Fanart_Image', fanart)
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
	return ok

# --------------------------------------------

params=[]

# TODO: Uncomment!
params=get_params()

url=None
name=None
mode=None
thumbnail=''

# TODO: Uncomment!
try:
	url=urllib.unquote_plus(params["url"])
except:
	pass
try:
	name=urllib.unquote_plus(params["name"])
except:
	pass
try:
	mode=int(params["mode"])
except:
	pass
try:
	thumbnail=urllib.unquote_plus(params["thumbnail"])
except:
	pass

# print "Mode: "+str(mode)
# print "URL: "+str(url)
# print "Name: "+str(name)

# # TEST
# mode = 2
# url = 'http://www.htvonline.com.vn/livetv/star-world-hd-3132386E61.html'
# name = 'Start World'
# thumbnail = ''

if mode==None or url==None or len(url)<1:
	INDEX('http://www.htvonline.com.vn/livetv')

elif mode==1:
	INDEX(url)

elif mode==2:
	VIDEOLINKS(url,name,thumbnail)

#!/usr/bin/python
#coding=utf-8
from xbmcswift2 import Plugin , xbmc , xbmcgui , xbmcaddon
import requests , re , urllib , os , zipfile , json , uuid , shutil , pickle
if 64 - 64: i11iIiiIii
OO0o = Plugin ( )
Oo0Ooo = xbmcaddon . Addon ( "plugin.video.kodi4vn.launcher" )
O0O0OO0O0O0 = "plugin://plugin.video.kodi4vn.launcher"
iiiii = "http://echipstore.com:8000"
if 64 - 64: iIIi1iI1II111 + ii11i / oOooOoO0Oo0O
def iI1 ( url ) :
 i1I11i = requests . get ( url + "%st=%s" % ( "&" if "?" in url else "?" , urllib . quote_plus ( OO0o . get_setting ( "token" ) ) ) )
 i1I11i . encoding = "utf-8"
 OoOoOO00 = i1I11i . json ( )
 return OoOoOO00
 if 27 - 27: OOOo0 / Oo - Ooo00oOo00o . I1IiI
def o0OOO ( url ) :
 OoOoOO00 = iI1 ( url )
 return OoOoOO00
 if 13 - 13: ooOo + Ooo0O
def IiiIII111iI ( source , dest_dir ) :
 with zipfile . ZipFile ( source ) as IiII :
  for iI1Ii11111iIi in IiII . infolist ( ) :
   i1i1II = iI1Ii11111iIi . filename . split ( '/' )
   O0oo0OO0 = dest_dir
   for I1i1iiI1 in i1i1II [ : - 1 ] :
    iiIIIII1i1iI , I1i1iiI1 = os . path . splitdrive ( I1i1iiI1 )
    o0oO0 , I1i1iiI1 = os . path . split ( I1i1iiI1 )
    if I1i1iiI1 in ( os . curdir , os . pardir , '' ) : continue
    O0oo0OO0 = os . path . join ( O0oo0OO0 , I1i1iiI1 )
   IiII . extract ( iI1Ii11111iIi , O0oo0OO0 )
   if 100 - 100: i11Ii11I1Ii1i
@ OO0o . route ( '/warning/<s>' )
def Ooo ( s = "" ) :
 o0oOoO00o = xbmcgui . Dialog ( )
 o0oOoO00o . ok ( 'Chú ý: User %s' % OO0o . get_setting ( "email" ) , s )
 return OO0o . finish ( )
 if 43 - 43: O0OOo . II1Iiii1111i
@ OO0o . route ( '/search/' )
def i1IIi11111i ( ) :
 o000o0o00o0Oo ( "Browse" , '/search' )
 oo = OO0o . keyboard ( heading = 'Tìm kiếm' )
 if oo :
  IiII1I1i1i1ii = '%s/yts/none/video/%s/' % ( O0O0OO0O0O0 , urllib . quote_plus ( oo ) )
  IIIII = OO0o . get_storage ( 'search_history' )
  if 'keywords' in IIIII :
   IIIII [ "keywords" ] = [ oo ] + IIIII [ "keywords" ]
  else :
   IIIII [ "keywords" ] = [ oo ]
  OO0o . redirect ( IiII1I1i1i1ii )
  if 26 - 26: O00OoOoo00 . iiiI11 / oooOOOOO * IiiIII111ii / i1iIIi1
@ OO0o . route ( '/searchlist/' )
def ii11iIi1I ( ) :
 o000o0o00o0Oo ( "Browse" , '/searchlist' )
 OoOoOO00 = [ ]
 iI111I11I1I1 = [ {
 "label" : "[B]Search[/B]" ,
 "path" : "%s/search" % ( O0O0OO0O0O0 ) ,
 "thumbnail" : "https://lh3.googleusercontent.com/jH1IxHp7MbOx62G1aboX2kj1vgtt3kercFVPYTxh7Yr0kMoVZARVNZIYjFZQOY1FzK7DisXyfHo=s256-no"
 } ]
 IIIII = OO0o . get_storage ( 'search_history' )
 if 'keywords' in IIIII :
  for OOooO0OOoo in IIIII [ 'keywords' ] :
   iIii1 = [ {
 "label" : OOooO0OOoo ,
 "path" : '%s/yts/none/video/%s/' % ( O0O0OO0O0O0 , urllib . quote_plus ( OOooO0OOoo ) ) ,
 "thumbnail" : "https://lh3.googleusercontent.com/jH1IxHp7MbOx62G1aboX2kj1vgtt3kercFVPYTxh7Yr0kMoVZARVNZIYjFZQOY1FzK7DisXyfHo=s256-no"
 } ]
   OoOoOO00 += iIii1
 OoOoOO00 = iI111I11I1I1 + OoOoOO00
 return OO0o . finish ( OoOoOO00 )
 if 71 - 71: IiI1I1
@ OO0o . route ( '/login' )
def OoO000 ( ) :
 o000o0o00o0Oo ( "Login" , "/login" )
 xbmc . executebuiltin ( 'Dialog.Close(busydialog)' )
 try :
  IIiiIiI1 = requests . get ( "http://echipstore.com/get-code/?nocache=true" ) . json ( )
  iiIiIIi = IIiiIiI1 [ "message" ] % IIiiIiI1 [ "user_code" ] . upper ( )
  ooOoo0O = xbmcgui . DialogProgress ( )
  ooOoo0O . create ( 'Login' , iiIiIIi )
  if 76 - 76: i1II1I11 / i11iIiiIii / ii11i . O0OOo % OOOo0
  OO0oOoo = 0
  while OO0oOoo < 60 :
   O0o0Oo = int ( ( OO0oOoo / 60.0 ) * 100 )
   if ooOoo0O . iscanceled ( ) :
    break
   ooOoo0O . update ( O0o0Oo , "" )
   OO0oOoo = OO0oOoo + 1
   xbmc . sleep ( 5000 )
   i1I11i = requests . get ( "http://echipstore.com/device?device_code=%s&nocache=true" % urllib . quote_plus ( IIiiIiI1 [ "device_code" ] ) )
   if "token" in i1I11i . text :
    Oo0Ooo . setSetting ( "token" , i1I11i . json ( ) [ "token" ] )
    Oo0Ooo . setSetting ( "email" , i1I11i . json ( ) [ "email" ] )
    break
  ooOoo0O . close ( )
  del ooOoo0O
  xbmc . executebuiltin ( 'XBMC.Container.Update(%s)' % O0O0OO0O0O0 )
 except :
  Oo00OOOOO = xbmcgui . Dialog ( )
  Oo00OOOOO . ok ( "Oops!" , "Có lỗi xảy ra. Xin quý vị vui lòng login vào dịp khác" )
  if 85 - 85: i1II1I11 . IiiIII111ii - ooOo % i1II1I11 % Oo
@ OO0o . route ( '/' )
def OO0o00o ( ) :
 o000o0o00o0Oo ( )
 dir ( "0" )
 if 89 - 89: II1Iiii1111i + I1IiI
@ OO0o . route ( '/ytslive/<order>/' , name = "ytslive_firstpage" )
@ OO0o . route ( '/ytslive/<order>/<page>' )
def Ii1I ( order = "viewcount" , page = "" ) :
 o000o0o00o0Oo ( "Browse YT Live News" , "/ytslive/%s/%s" % ( order , page ) )
 OoOoOO00 = o0OOO ( "%s/ytslive/%s/%s" % ( iiiii , order , page ) )
 for iIii1 in OoOoOO00 :
  iIii1 [ "path" ] = O0O0OO0O0O0 + iIii1 [ "path" ]
 if OO0o . get_setting ( 'thumbview' , bool ) :
  if xbmc . getSkinDir ( ) in ( 'skin.confluence' , 'skin.eminence' ) :
   return OO0o . finish ( OoOoOO00 , view_mode = 500 )
  elif xbmc . getSkinDir ( ) == 'skin.xeebo' :
   return OO0o . finish ( OoOoOO00 , view_mode = 52 )
  else :
   return OO0o . finish ( OoOoOO00 )
 else :
  return OO0o . finish ( OoOoOO00 )
  if 89 - 89: i11iIiiIii / iIIi1iI1II111 * Ooo0O % O00OoOoo00 % II1Iiii1111i
@ OO0o . route ( '/yts/<order>/<t>/<q>/' , name = 'yts_firstpage' )
@ OO0o . route ( '/yts/<order>/<t>/<q>/<page>' )
def Ii1 ( order , t , q = "" , page = "" ) :
 o000o0o00o0Oo ( "Browse YT by topics %s" % q , "/yts/%s/%s/%s/%s" % ( order , t , q , page ) )
 OoOoOO00 = [ ]
 if t in [ "channel" , "playlist" ] and order == "date" :
  order = "videocount"
 OoOoOO00 = o0OOO ( "%s/yts/%s/%s?q=%s&page=%s" % ( iiiii , order , t , q , page ) )
 for iIii1 in OoOoOO00 :
  if "plugin://" not in iIii1 [ "path" ] :
   iIii1 [ "path" ] = O0O0OO0O0O0 + iIii1 [ "path" ]
 if t == "video" :
  III1i1i = [ {
 "label" : "[B]Channels[/B]" ,
 "path" : "%s/yts/%s/channel/%s" % ( O0O0OO0O0O0 , order , q ) ,
 "thumbnail" : "http://thong.viettv24.com/kodi4vn/images/yt.png"
 } ]
  iiI1 = [ {
 "label" : "[B]Playlist[/B]" ,
 "path" : "%s/yts/%s/playlist/%s" % ( O0O0OO0O0O0 , order , q ) ,
 "thumbnail" : "https://lh3.googleusercontent.com/184S-U4BBN7f55qcTQFUQSsBjYlJZ246A01J-n_BKa4bwe74nANMPkj58I8DSPzlxYyWocyYYYj89D-1qHXfEkVENdA6O1weJZOVZAMCAIhK8vfZ9bgKpw-eY4pwpaCzfQ0MS4wlwnjZE28jmTZejHIVRflEUcPS-SLJ6xGTAVIHXbIP1uEKugegwL9ULD0vfwD92FWzz9_abZ70VNeBTBRCjE3-gfQ-IKVUmGJlnJeEJcS1fUAo6_qvrBf9NX1n0gLp24lVdTj-ml6VmDtr5bVwQBBes-7zTKthqeLqZoo-Zr0ZDY2hhw871xrXDeUtlwVeK-EnAEgFRAWyRa9HjijEEED81GDYkCc5r0qK3xjqqPvo3aJ-urdVH2TcOkbmTgx2l7jHIMo4WuE9-d8hAMzGXJfLp4NNGty3vYLk-0RG_MjvUp4qeNcmPMHrX8fWih2z-hAXhfvjXZ1SJq_BEnFzSgVCyW44inHkLUallDmcbFyz5EuYgEAVYHMUikabDj2eLrsMbHTM94a_ljcBV9X4jS0Dz5EMjLl5veXQmCA=w175-h107-no"
 } ]
  OoOoOO00 = III1i1i + iiI1 + OoOoOO00
 if OO0o . get_setting ( 'thumbview' , bool ) :
  if xbmc . getSkinDir ( ) in ( 'skin.confluence' , 'skin.eminence' ) :
   return OO0o . finish ( OoOoOO00 , view_mode = 500 )
  elif xbmc . getSkinDir ( ) == 'skin.xeebo' :
   return OO0o . finish ( OoOoOO00 , view_mode = 52 )
  else :
   return OO0o . finish ( OoOoOO00 )
 else :
  return OO0o . finish ( OoOoOO00 )
  if 19 - 19: iiiI11 + i1II1I11
@ OO0o . route ( '/dir/<url>' )
def dir ( url ) :
 o000o0o00o0Oo ( "Browse Kodi4vn Launcher Menu %s" % url , "/dir/%s" % url )
 OoOoOO00 = [ ]
 if "://" in url :
  pass
 else :
  OoOoOO00 = o0OOO ( "%s/dir/%s" % ( iiiii , urllib . quote_plus ( url ) ) )
  for iIii1 in OoOoOO00 :
   if "plugin://" not in iIii1 [ "path" ] :
    iIii1 [ "path" ] = O0O0OO0O0O0 + iIii1 [ "path" ]
  ooo = ( "" if OO0o . get_setting ( "email" ) == "" else ( "Chào %s. " % OO0o . get_setting ( "email" ) ) )
  ii1I1i1I = [ {
 "label" : "[COLOR yellow][B]%sVào đây để Login/Relogin[/B][/COLOR]" % ooo ,
 "path" : O0O0OO0O0O0 + "/login" ,
 "thumbnail" : "https://cdn3.iconfinder.com/data/icons/gray-toolbar-2/512/login_user_profile_account-512.png"
 } ]
  if url == "0" :
   OOoo0O0 = [ {
 "label" : "[B]Search[/B]" ,
 "path" : "%s/searchlist" % ( O0O0OO0O0O0 ) ,
 "thumbnail" : "https://lh4.ggpht.com/tKloV0jZyh-PviiBI8eledqCYt17oiFZdbnDCpgHTLwQmQIjKkvTicbL4M3lV6tmzR8=w300"
 } ]
   OoOoOO00 = OOoo0O0 + OoOoOO00
  OoOoOO00 = ii1I1i1I + OoOoOO00
  if 41 - 41: II1Iiii1111i
  if 6 - 6: O0OOo
  if 31 - 31: oooOOOOO . oooOOOOO - i11Ii11I1Ii1i / ooOo + i1II1I11 * Ooo00oOo00o
  if 63 - 63: IiI1I1 % OOOo0 / oOooOoO0Oo0O - oOooOoO0Oo0O
  if 8 - 8: Ooo0O
  if 60 - 60: iiiI11 / iiiI11
  if 46 - 46: oooOOOOO * O00OoOoo00 - ooOo * II1Iiii1111i - IiI1I1
  if 83 - 83: oOooOoO0Oo0O
  if 31 - 31: Oo - O00OoOoo00 . IiI1I1 % Ooo0O - iIIi1iI1II111
 return OO0o . finish ( OoOoOO00 )
 if 4 - 4: Oo / i1II1I11 . IiiIII111ii
@ OO0o . route ( '/ytp/<pid>' , name = 'ytp_firstpage' )
@ OO0o . route ( '/ytp/<pid>/<page>' )
def O0oo0OO0oOOOo ( pid , page = "" ) :
 o000o0o00o0Oo ( "Browse YT Videos by PlaylistID %s" % pid , "/ytp/%s/%s" % ( pid , page ) )
 OoOoOO00 = o0OOO ( "%s/ytp/%s/%s" % ( iiiii , pid , page ) )
 for iIii1 in OoOoOO00 :
  iIii1 [ "path" ] = O0O0OO0O0O0 + iIii1 [ "path" ]
 if OO0o . get_setting ( 'thumbview' , bool ) :
  if xbmc . getSkinDir ( ) in ( 'skin.confluence' , 'skin.eminence' ) :
   return OO0o . finish ( OoOoOO00 , view_mode = 500 )
  elif xbmc . getSkinDir ( ) == 'skin.xeebo' :
   return OO0o . finish ( OoOoOO00 , view_mode = 52 )
  else :
   return OO0o . finish ( OoOoOO00 )
 else :
  return OO0o . finish ( OoOoOO00 )
  if 35 - 35: i1iIIi1 % Ooo00oOo00o
@ OO0o . route ( '/ytu/<uid>' )
def o0OOoo0OO0OOO ( uid ) :
 iI1iI1I1i1I = requests . get ( "%s/ytu/%s" % ( iiiii , uid ) ) . text
 iIi11Ii1 ( iI1iI1I1i1I , "" )
 if 50 - 50: Oo - i1II1I11 * O0OOo / IiI1I1 + i11Ii11I1Ii1i
@ OO0o . route ( '/ytc/<cid>' , name = 'ytc_firstpage' )
@ OO0o . route ( '/ytc/<cid>/<page>' )
def iIi11Ii1 ( cid , page = "" ) :
 o000o0o00o0Oo ( "Browse YT Videos by ChannelID %s" % cid , "/ytc/%s/%s" % ( cid , page ) )
 OoOoOO00 = [ {
 "label" : "[B]Playlist[/B]" ,
 "path" : "%s/ytcp/%s/%s" % ( O0O0OO0O0O0 , cid . split ( "@" ) [ 0 ] , "" ) ,
 "thumbnail" : "https://lh3.googleusercontent.com/184S-U4BBN7f55qcTQFUQSsBjYlJZ246A01J-n_BKa4bwe74nANMPkj58I8DSPzlxYyWocyYYYj89D-1qHXfEkVENdA6O1weJZOVZAMCAIhK8vfZ9bgKpw-eY4pwpaCzfQ0MS4wlwnjZE28jmTZejHIVRflEUcPS-SLJ6xGTAVIHXbIP1uEKugegwL9ULD0vfwD92FWzz9_abZ70VNeBTBRCjE3-gfQ-IKVUmGJlnJeEJcS1fUAo6_qvrBf9NX1n0gLp24lVdTj-ml6VmDtr5bVwQBBes-7zTKthqeLqZoo-Zr0ZDY2hhw871xrXDeUtlwVeK-EnAEgFRAWyRa9HjijEEED81GDYkCc5r0qK3xjqqPvo3aJ-urdVH2TcOkbmTgx2l7jHIMo4WuE9-d8hAMzGXJfLp4NNGty3vYLk-0RG_MjvUp4qeNcmPMHrX8fWih2z-hAXhfvjXZ1SJq_BEnFzSgVCyW44inHkLUallDmcbFyz5EuYgEAVYHMUikabDj2eLrsMbHTM94a_ljcBV9X4jS0Dz5EMjLl5veXQmCA=w175-h107-no"
 } ]
 if "@" not in cid :
  cid = requests . get ( "%s/ytc/%s" % ( iiiii , cid ) ) . text
 if "@" in cid :
  III1i1i = o0OOO ( "%s/ytp/%s/%s" % ( iiiii , cid . split ( "@" ) [ 1 ] , page ) )
  for iIii1 in III1i1i :
   iIii1 [ "path" ] = O0O0OO0O0O0 + iIii1 [ "path" ]
  OoOoOO00 += III1i1i
 if OO0o . get_setting ( 'thumbview' , bool ) :
  if xbmc . getSkinDir ( ) in ( 'skin.confluence' , 'skin.eminence' ) :
   return OO0o . finish ( OoOoOO00 , view_mode = 500 )
  elif xbmc . getSkinDir ( ) == 'skin.xeebo' :
   return OO0o . finish ( OoOoOO00 , view_mode = 52 )
  else :
   return OO0o . finish ( OoOoOO00 )
 else :
  return OO0o . finish ( OoOoOO00 )
  if 88 - 88: oooOOOOO / IiI1I1 + IiiIII111ii - Oo / i1II1I11 - Ooo0O
@ OO0o . route ( '/ytcp/<cid>' , name = 'ytcp_firstpage' )
@ OO0o . route ( '/ytcp/<cid>/<page>' )
def IIIIii ( cid , page = "" ) :
 o000o0o00o0Oo ( "Browse YT Playlist by ChannelID %s" % cid , "/ytcp/%s/%s" % ( cid , page ) )
 OoOoOO00 = o0OOO ( "%s/ytcp/%s/%s" % ( iiiii , cid , page ) )
 for iIii1 in OoOoOO00 :
  iIii1 [ "path" ] = O0O0OO0O0O0 + iIii1 [ "path" ]
 if OO0o . get_setting ( 'thumbview' , bool ) :
  if xbmc . getSkinDir ( ) in ( 'skin.confluence' , 'skin.eminence' ) :
   return OO0o . finish ( OoOoOO00 , view_mode = 500 )
  elif xbmc . getSkinDir ( ) == 'skin.xeebo' :
   return OO0o . finish ( OoOoOO00 , view_mode = 52 )
  else :
   return OO0o . finish ( OoOoOO00 )
 else :
  return OO0o . finish ( OoOoOO00 )
  if 70 - 70: oooOOOOO / iiiI11 . IiiIII111ii % I1IiI
@ OO0o . route ( '/play/<url>' )
def OOoOO00OOO0OO ( url ) :
 o000o0o00o0Oo ( "Play %s" % url , "/play/%s" % url )
 ooOoo0O = xbmcgui . DialogProgress ( )
 ooOoo0O . create ( 'Kodi4VN Launcher' , 'Loading video. Please wait...' )
 OO0o . set_resolved_url ( iI1I111Ii111i ( url ) )
 ooOoo0O . close ( )
 del ooOoo0O
 if 7 - 7: i1II1I11 * ooOo % II1Iiii1111i . i1iIIi1
def iI1I111Ii111i ( url ) :
 if "youtube" in url :
  Ii1iIiII1ii1 = re . compile ( '(youtu\.be\/|youtube-nocookie\.com\/|youtube\.com\/(watch\?(.*&)?v=|(embed|v|user)\/))([^\?&"\'>]+)' ) . findall ( url )
  ooOooo000oOO = Ii1iIiII1ii1 [ 0 ] [ len ( Ii1iIiII1ii1 [ 0 ] ) - 1 ] . replace ( 'v/' , '' )
  return 'plugin://plugin.video.youtube/?action=play_video&videoid=%s' % ooOooo000oOO
 elif "://" not in url :
  Oo0oOOo = "http://www.viettv24.com/main/getStreamingServer.php"
  Oo0OoO00oOO0o = { 'strname' : '%s-' % url }
  return requests . post ( Oo0oOOo , data = Oo0OoO00oOO0o ) . text . strip ( )
 else :
  return url
  if 80 - 80: II1Iiii1111i + O00OoOoo00 - O00OoOoo00 % IiiIII111ii
@ OO0o . route ( '/showimage/<url>' )
def OoOO0oo0o ( url ) :
 O0oo0OO0 = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
 II11i1I11Ii1i = xbmc . translatePath ( os . path . join ( O0oo0OO0 , "tmp" ) )
 if os . path . exists ( II11i1I11Ii1i ) :
  shutil . rmtree ( II11i1I11Ii1i )
 os . makedirs ( II11i1I11Ii1i )
 if ".zip" in url :
  O000O0oOO0 = xbmc . translatePath ( os . path . join ( II11i1I11Ii1i , "temp.zip" ) )
  urllib . urlretrieve ( url , O000O0oOO0 )
  IiiIII111iI ( O000O0oOO0 , II11i1I11Ii1i )
 else :
  O0ooo0O0oo0 = xbmc . translatePath ( os . path . join ( II11i1I11Ii1i , "temp.jpg" ) )
  urllib . urlretrieve ( url , O0ooo0O0oo0 )
 xbmc . executebuiltin ( "SlideShow(%s,recursive)" % II11i1I11Ii1i )
 if 91 - 91: ii11i + IiI1I1
def o000o0o00o0Oo ( title = "Home" , page = "/" ) :
 i1i = "http://www.google-analytics.com/collect"
 I1I1iIiII1 = open ( i11i1I1 ) . read ( )
 ii1I = {
 'v' : '1' ,
 'tid' : 'UA-52209804-5' ,
 'cid' : I1I1iIiII1 ,
 't' : 'pageview' ,
 'dp' : page ,
 'dt' : title
 }
 requests . post ( i1i , data = urllib . urlencode ( ii1I ) )
 if 67 - 67: i11iIiiIii - OOOo0 % O0OOo . iIIi1iI1II111
o0oo = xbmc . translatePath ( 'special://userdata' )
if os . path . exists ( o0oo ) == False :
 os . mkdir ( o0oo )
i11i1I1 = os . path . join ( o0oo , 'cid' )
oooooOoo0ooo = os . path . join ( o0oo , 'search.p' )
if 6 - 6: iiiI11 - oooOOOOO + ii11i - IiI1I1 - i11iIiiIii
if os . path . exists ( i11i1I1 ) == False :
 with open ( i11i1I1 , "w" ) as OO0oOO0O :
  OO0oOO0O . write ( str ( uuid . uuid1 ( ) ) )
  if 91 - 91: iIIi1iI1II111
if __name__ == '__main__' :
 OO0o . run ( )
 if 61 - 61: Oo
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3

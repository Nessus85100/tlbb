# script by Mikey1234

import xbmc, xbmcgui
import os
import xbmcaddon

cmd = os.path.join(xbmc.translatePath(xbmcaddon.Addon('script.tlbb').getAddonInfo('path')), 'update.py')
cmd += ',0'


dialog = xbmcgui.Dialog()
if dialog.yesno('TLBB UPDATE','', 'Do You Want To Check For Updates'):


  xbmc.executebuiltin("XBMC.RunScript(%s)"%cmd)




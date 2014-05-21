import xbmc
import sys

controlid = sys.argv[1]
 
xbmc.executebuiltin('XBMC.Action(window1111)')
xbmc.executebuiltin('XBMC.SendClick('+controlid+')')


import sys
from xbmcjson import XBMC

languageToSet = sys.argv[1]
xbmc = XBMC("http://localhost:80/jsonrpc")
xbmc.Settings.SetSettingValue({"setting":"locale.language","value":languageToSet})
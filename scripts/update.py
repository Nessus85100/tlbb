import xbmc, xbmcgui
import shutil

class MyClass(xbmcgui.Window):
  def __init__(self):
    dialog = xbmcgui.Dialog()
    if dialog.yesno("", ""):
      
mydisplay = MyClass()
del mydisplay

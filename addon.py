import xbmc
import os, subprocess
winView = "explorer.exe"
subprocess.run(winView, shell=True)
def terminate(ProcessName):
    os.system('taskkill /IM "' + ProcessName + '" /F')

terminate('kodi.exe')

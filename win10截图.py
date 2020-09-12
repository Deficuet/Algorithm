import win32con
import win32api
import win32gui
import win32ui
import keyboard

def CutImage_Win32():
    #corrwin = 0
    corrwin = win32gui.FindWindow('Progman', 'Program Manager')
    corrwin = win32gui.FindWindowEx(corrwin, 0, 'SHELLDLL_DefView', None)
    corrwin = win32gui.FindWindowEx(corrwin, 0, 'SysListView32', 'FolderView')
    
    WinDC = win32gui.GetWindowDC(corrwin)
    mfcDC = win32ui.CreateDCFromHandle(WinDC)
    saveDC = mfcDC.CreateCompatibleDC()
    bitmap = win32ui.CreateBitmap()
    bitmap.CreateCompatibleBitmap(mfcDC, 1920, 1080)
    saveDC.SelectObject(bitmap)
    saveDC.BitBlt((0, 0), (1920, 1080), mfcDC, (0, 0), win32con.SRCCOPY)
    bitmap.SaveBitmapFile(saveDC, 'test.png')

#keyboard.add_hotkey('ctrl+alt+a', CutImage_Win32)
#keyboard.wait('right shift+esc')

CutImage_Win32()
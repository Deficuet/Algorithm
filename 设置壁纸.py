import win32api
import win32gui
import win32con

key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, 'Control Panel\\Desktop', 0, win32con.KEY_SET_VALUE)
win32api.RegSetValueEx(key, 'WallpaperStyle', 0, win32con.REG_SZ, '0')
win32api.RegSetValueEx(key, 'TileWallpaper', 0, win32con.REG_SZ, '0')
win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, r'D:\BackgroundBuffer\lumang_2_bg.png', 1+2)
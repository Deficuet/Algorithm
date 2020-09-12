from ctypes import c_buffer, windll
from sys import getfilesystemencoding
buf = c_buffer(255)
audiodir = 'D:/CloudMusic/MyNight.mp3'
alias = 'Daydream_Cafe_-_piano_ver'
command_open = ('open "' + audiodir + '" alias ' + alias).encode(getfilesystemencoding())
command_play = ('play ' + alias).encode(getfilesystemencoding())
for i in [command_open, command_play]:
    windll.winmm.mciSendStringA(i, buf, 254, 0)
input()
command_close = ('close ' + 'Daydream_Cafe_-_piano_ver').encode(getfilesystemencoding())
windll.winmm.mciSendStringA(command_close, 0, 0, 0)
input()
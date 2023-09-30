from delphifmx import *
from MusicPlayer import MusicPlayerWindow

def main():
    Application.Initialize()
    Application.Title = 'Music Player'
    Application.MainForm = MusicPlayerWindow(Application)
    Application.MainForm.Show()
    Application.Run()
    Application.MainForm.Destroy()

if __name__ == '__main__':
    main()

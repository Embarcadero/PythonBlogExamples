from delphifmx import *
from Bio import BioScreen

def main():
    Application.Initialize()
    Application.Title = 'Chat Application'
    Application.MainForm = BioScreen(Application)
    Application.MainForm.Show()
    Application.Run()
    Application.MainForm.Destroy()

if __name__ == '__main__':
    main()

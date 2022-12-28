from delphifmx import *

Application.Initialize()
Application.Title = "Delphi FMX"

main_window = Form(Application)
Application.MainForm = main_window

main_window.SetProps(Caption = "Python4Delphi")
msg = Label(main_window)
msg.SetProps(Parent = main_window,
    Text = "Delphi FMX For Python GUIs",
    Position = Position(PointF(20, 20)),
    Width = 200)
main_window.SetProps(Width = 315, Height = 400) #Window dimensions
main_window.Show()
Application.Run() #Main loop
main_window.Destroy()
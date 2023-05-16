import os
from delphifmx import *

class StopwatchForm(Form):

    def __init__(self, owner):
        self.Title = None
        self.Time = None
        self.Start = None
        self.Pause = None
        self.Reset = None
        self.Back = None
        self.Timer1 = None
        self.LoadProps(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Stopwatch.pyfmx"))

        # Initially setting time label to zero
        self.Time.Text = '00:00:00'

    def StartClick(self, Sender):
        self.Timer1.Enabled = True
        self.Timer1.Interval = 10

    def PauseClick(self, Sender):
        self.Timer1.Enabled = False

    def ResetClick(self, Sender):
        self.Time.Text = '00:00:00'  # Update the label
        self.Timer1.Tag = 0  # Update the timer tag
        self.Timer1.Enabled = False

    def BackClick(self, Sender):
        Application.MainForm.Show()
        self.Destroy()

    def Timer1Timer(self, Sender):
        # Keep adding the time interval
        ElapsedTime = self.Timer1.Tag + self.Timer1.Interval

        # Calculate the number of minutes, seconds and milliseconds
        Minutes = ElapsedTime // (60 * 1000)
        Seconds = (ElapsedTime // 1000) % 60
        Milliseconds = ElapsedTime % 1000

        # Update time label
        self.Time.Text = f"{Minutes:02d}:{Seconds:02d}.{Milliseconds:02d}"

        # Store the elapsed time in the timer tag
        self.Timer1.Tag = ElapsedTime
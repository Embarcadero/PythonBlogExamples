import os
from delphifmx import *


class TimerForm(Form):

    def __init__(self, owner):
        self.Title = None
        self.Time = None
        self.Start = None
        self.Pause = None
        self.Reset = None
        self.ComboBox1 = None
        self.Back = None
        self.TimeDuration = None
        self.Status = None
        self.Timer1 = None
        self.LoadProps(os.path.join(os.path.dirname(
            os.path.abspath(__file__)), "Timer.pyfmx"))

        # Initially setting time label to zero and status to blank
        self.Time.Text = '00:00:00'
        self.Status.Text = ''

        # Add items to the combo box
        self.ComboBox1.Items.Add('Brush Teeth')
        self.ComboBox1.Items.Add('Boil Eggs')
        self.ComboBox1.Items.Add('Other')

        # You cannot type in the TEdit until Other from combo box is selected
        self.TimeDuration.Enabled = False
        self.Start.Enabled = False
        self.Pause.Enabled = False
        self.Reset.Enabled = False

        # Var to store start time value
        self.CountdownTime = 0

    def StartClick(self, Sender):
        self.Timer1.Enabled = True
        self.Timer1.Interval = 10
        self.Status.Text = ''

    def PauseClick(self, Sender):
        self.Timer1.Enabled = False

    def ResetClick(self, Sender):
        self.Time.Text = '00:00:00'  # Update the label
        self.Timer1.Tag = self.CountdownTime  # Update the timer tag
        self.Timer1.Enabled = False

    def SetOtherTime(self, sender):
        # Check for format of time given
        if self.TimeDuration.Text.count(':') == 2:
            Time = self.TimeDuration.Text.split(':')
            Minutes, Seconds, Milliseconds = int(
                Time[0]), int(Time[1]), int(Time[2])
            TotalMilliseconds = (Minutes * 60 * 1000) + \
                (Seconds * 1000) + Milliseconds

            self.CountdownTime = int(TotalMilliseconds)
            self.Timer1.Tag = self.CountdownTime

            self.Start.Enabled = True
            self.Pause.Enabled = True
            self.Reset.Enabled = True

        else:
            self.Status.Text = 'Give the time duration in minutes:seconds:milliseconds'

    def ComboSelected(self, sender):
        if self.ComboBox1.ItemIndex == 0:
            self.TimeDuration.Text = '2:00:00'
        elif self.ComboBox1.ItemIndex == 1:
            self.TimeDuration.Text = '5:10:00'
        elif self.ComboBox1.ItemIndex == 2:
            self.TimeDuration.Text = ''
            self.TimeDuration.Enabled = True

    def BackClick(self, Sender):
        self.Destroy()
        Application.MainForm.Show()

    def Timer1Timer(self, Sender):
        ElapsedTime = self.Timer1.Tag - self.Timer1.Interval

        if ElapsedTime <= 0:
            self.Status.Text = 'Timer Ended!'
            self.Time.Text = '00:00:00'  # Update the label
            self.Timer1.Tag = self.CountdownTime  # Update the timer tag
            self.Timer1.Enabled = False

        # Calculate the number of minutes, seconds and milliseconds
        Minutes = ElapsedTime // (60 * 1000)
        Seconds = (ElapsedTime // 1000) % 60
        Milliseconds = ElapsedTime % 1000

        self.Time.Text = f"{Minutes:02d}:{Seconds:02d}.{Milliseconds:02d}"

        # Store the elapsed time in the Tag property of the timer
        self.Timer1.Tag = ElapsedTime

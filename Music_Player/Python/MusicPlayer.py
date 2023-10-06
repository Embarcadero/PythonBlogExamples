import os
from delphifmx import *
from tinytag import TinyTag

class MusicPlayerWindow(Form):

    def __init__(self, owner):
        # Initialize all GUI elements
        self.top_rectangle = None
        self.top_heading = None
        self.create_playlist = None
        self.tab_ctrl = None
        self.songs_tab = None
        self.audio_list_box = None
        self.now_playing_tab = None
        self.audio_embedded_image = None
        self.audio_track_bar = None
        self.play_btn = None
        self.pause_btn = None
        self.open_audio_dialog = None
        self.media_player = None
        self.timer = None
        self.stop_btn = None
        self.fwd_btn = None
        self.bwd_btn = None
        self.nxt_btn = None
        self.volume_track_bar = None
        self.vol_label = None
        self.location_label = None
        self.current_time_label = None
        self.song_name_label = None
        self.artist_label = None
        self.duration_label = None
        self.LoadProps(os.path.join(os.path.dirname(os.path.abspath(__file__)), "MusicPlayer.pyfmx"))

        # Set up the style manager and apply a custom style
        self.__sm = StyleManager()
        self.__sm.SetStyleFromFile(os.path.join(os.getcwd(), "Styles\Transparent.style"))

        # Set the initial position of TrackBar to the middle (50%)
        self.volume_track_bar.Value = 100
    
        self.tag = None

    def create_playlistClick(self, Sender):
        # Open a file dialog to select audio files and populate the playlist
        if self.open_audio_dialog.Execute():
            self.audio_list_box.Clear()
            mp3_files_list = self.open_audio_dialog.Files.ToList()
            self.listbox_song_paths = []
            self.listbox_items = []
            for mp3_file_path in mp3_files_list:
                self.listbox_song_paths.append(mp3_file_path)
                mp3_file_name = os.path.splitext(os.path.basename(mp3_file_path))[0]
                lb_item_audio_name = ListBoxItem(self.audio_list_box)
                lb_item_audio_name.SetProps(Parent=self.audio_list_box,
                                            Height=40,
                                            Text=mp3_file_name)
                self.listbox_items.append(lb_item_audio_name)

    def audio_list_boxChange(self, Sender):
        # Handle selection of an audio item in the list box
        selected_lb_item = self.audio_list_box.Selected
        self.tab_ctrl.TabIndex = 1
        mp3_file_path = self.listbox_song_paths[self.listbox_items.index(selected_lb_item)]
        
        # Use TinyTag to retrieve audio file information
        self.tag = TinyTag.get(mp3_file_path, image=True)

        mins = self.tag.duration // 60
        sec = self.tag.duration % 60
        self.duration_label.Text = f"{int(mins)}:{int(sec)}"

        # Set various labels and update the embedded image if available
        self.audio_track_bar.Max = self.tag.duration
        self.artist_label.Text = "Artist: {}".format(self.tag.artist)
        self.location_label.Text = "Location: {}".format(mp3_file_path)
        self.song_name_label.Text = "Song Name: {}".format(selected_lb_item.Text)

        image_data = self.tag.get_image()
        if image_data is not None:
            bs = BytesStream(image_data)
            self.audio_embedded_image.Bitmap.LoadFromStream(bs)
        else:
            self.audio_embedded_image.Bitmap = None

        # Load and play the selected audio file
        self.audio_track_bar.OnChange = self.audio_track_barChange
        self.media_player.FileName = mp3_file_path
        self.media_player.Play()

        # Set up a timer to update the current playback time
        self.timer.Interval = 1000  # Set the interval to 1000 milliseconds (1 second)
        self.timer.Enabled = True

        # Enable playback control buttons
        self.pause_btn.Enabled = True
        self.stop_btn.Enabled = True

    def audio_track_barChange(self, Sender):
        # Handle changes in the audio trackbar
        selected_position_seconds = self.audio_track_bar.Value
        self.media_player.CurrentTime = int(selected_position_seconds * 10000000)

    def update_current_time(self, Sender):
        # Update the current playback time
        current_time_seconds = self.media_player.CurrentTime / 10000000

        self.audio_track_bar.Value = current_time_seconds

        # Format the current time as MM:SS
        minutes = int(current_time_seconds // 60)
        seconds = int(current_time_seconds % 60)
        self.current_time_label.Text = f"{minutes:02}:{seconds:02}"

    def play_btnClick(self, Sender):
        # Handle play button click
        self.play_btn.Enabled = False
        self.pause_btn.Enabled = True
        self.stop_btn.Enabled = True
        self.media_player.Play()

    def pause_btnClick(self, Sender):
        # Handle pause button click
        self.play_btn.Enabled = True
        self.pause_btn.Enabled = False
        self.media_player.Stop()

    def stop_btnClick(self, Sender):
        # Handle stop button click
        self.stop_btn.Enabled = False
        self.pause_btn.Enabled = False
        self.play_btn.Enabled = True
        self.media_player.FileName = self.open_audio_dialog.FileName

    def fwd_btnClick(self, Sender):
        # Handle forward button click
        current_time_seconds = self.media_player.CurrentTime / 10000000
        new_time_seconds = current_time_seconds + 10
    
        if new_time_seconds < self.tag.duration:
            self.media_player.CurrentTime = round(new_time_seconds * 10000000)

    def bwd_btnClick(self, Sender):
        # Handle backward button click
        current_time_seconds = self.media_player.CurrentTime / 10000000
        new_time_seconds = current_time_seconds - 10
    
        if new_time_seconds >= 0:
            self.media_player.CurrentTime = round(new_time_seconds * 10000000)

    def volumeChange(self, Sender):
        # Handle volume control change
        volume = self.volume_track_bar.Value / 100.0
        self.media_player.Volume = volume

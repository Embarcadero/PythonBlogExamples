unit MusicPlayer;

interface

uses
  System.SysUtils, System.Types, System.UITypes, System.Classes, System.Variants,
  FMX.Types, FMX.Controls, FMX.Forms, FMX.Graphics, FMX.Dialogs, FMX.Media,
  FMX.StdCtrls, FMX.Layouts, FMX.ListBox, FMX.TabControl,
  FMX.Controls.Presentation, FMX.Objects;

type
  TMusicPlayerWindow = class(TForm)
    top_rectangle: TRectangle;
    top_heading: TLabel;
    create_playlist: TButton;
    tab_ctrl: TTabControl;
    songs_tab: TTabItem;
    now_playing_tab: TTabItem;
    audio_list_box: TListBox;
    audio_embedded_image: TImageControl;
    audio_track_bar: TTrackBar;
    play_btn: TButton;
    pause_btn: TButton;
    open_audio_dialog: TOpenDialog;
    media_player: TMediaPlayer;
    timer: TTimer;
    stop_btn: TButton;
    fwd_btn: TButton;
    bwd_btn: TButton;
    volume_track_bar: TTrackBar;
    vol_label: TLabel;
    location_label: TLabel;
    current_time_label: TLabel;
    song_name_label: TLabel;
    artist_label: TLabel;
    duration_label: TLabel;
    procedure create_playlistClick(Sender: TObject);
    procedure play_btnClick(Sender: TObject);
    procedure pause_btnClick(Sender: TObject);
    procedure update_current_time(Sender: TObject);
    procedure audio_list_boxChange(Sender: TObject);
    procedure volumeChange(Sender: TObject);
    procedure bwd_btnClick(Sender: TObject);
    procedure fwd_btnClick(Sender: TObject);
    procedure stop_btnClick(Sender: TObject);
    procedure nxt_btnClick(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  MusicPlayerWindow: TMusicPlayerWindow;

implementation

{$R *.fmx}


procedure TMusicPlayerWindow.audio_list_boxChange(Sender: TObject);
begin
//
end;

procedure TMusicPlayerWindow.bwd_btnClick(Sender: TObject);
begin
//
end;

procedure TMusicPlayerWindow.create_playlistClick(Sender: TObject);
begin
//
end;

procedure TMusicPlayerWindow.fwd_btnClick(Sender: TObject);
begin
//
end;

procedure TMusicPlayerWindow.nxt_btnClick(Sender: TObject);
begin
//
end;

procedure TMusicPlayerWindow.pause_btnClick(Sender: TObject);
begin
//
end;

procedure TMusicPlayerWindow.play_btnClick(Sender: TObject);
begin
//
end;

procedure TMusicPlayerWindow.stop_btnClick(Sender: TObject);
begin
//
end;

procedure TMusicPlayerWindow.update_current_time(Sender: TObject);
begin
//
end;

procedure TMusicPlayerWindow.volumeChange(Sender: TObject);
begin
//
end;

end.

program MusicPlayerProject;

uses
  System.StartUpCopy,
  FMX.Forms,
  MusicPlayer in 'MusicPlayer.pas' {MusicPlayerWindow};

{$R *.res}

begin
  Application.Initialize;
  Application.CreateForm(TMusicPlayerWindow, MusicPlayerWindow);
  Application.Run;
end.

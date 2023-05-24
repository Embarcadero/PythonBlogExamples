program HiLoGame;

uses
  System.StartUpCopy,
  FMX.Forms,
  MainMenu in 'MainMenu.pas' {MainForm},
  Game in 'Game.pas' {GameForm};

{$R *.res}

begin
  Application.Initialize;
  Application.CreateForm(TMainForm, MainForm);
  Application.CreateForm(TGameForm, GameForm);
  Application.Run;
end.

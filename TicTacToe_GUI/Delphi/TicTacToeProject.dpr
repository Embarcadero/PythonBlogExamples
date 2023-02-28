program TicTacToeProject;

uses
  System.StartUpCopy,
  FMX.Forms,
  TicTacToe in 'TicTacToe.pas' {TicTacToeGUI};

{$R *.res}

begin
  Application.Initialize;
  Application.CreateForm(TTicTacToeGUI, TicTacToeGUI);
  Application.Run;
end.

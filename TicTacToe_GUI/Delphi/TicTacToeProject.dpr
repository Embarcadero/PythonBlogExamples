program TicTacToeProject;

uses
  System.StartUpCopy,
  FMX.Forms,
  TicTacToe in 'TicTacToe.pas' {Form2};

{$R *.res}

begin
  Application.Initialize;
  Application.CreateForm(TForm2, Form2);
  Application.Run;
end.

program ImageEditor;

uses
  System.StartUpCopy,
  FMX.Forms,
  Main in 'Main.pas' {MainFrom};

{$R *.res}

begin
  Application.Initialize;
  Application.CreateForm(TMainFrom, MainFrom);
  Application.Run;
end.

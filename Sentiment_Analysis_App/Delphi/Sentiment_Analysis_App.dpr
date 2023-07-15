program Sentiment_Analysis_App;

uses
  System.StartUpCopy,
  FMX.Forms,
  Main in 'Main.pas' {MainForm};

{$R *.res}

begin
  Application.Initialize;
  Application.CreateForm(TMainForm, MainForm);
  Application.Run;
end.

program MyTestProject;

uses
  System.StartUpCopy,
  FMX.Forms,
  TestUnit in 'TestUnit.pas' {TestForm};

{$R *.res}

begin
  Application.Initialize;
  Application.CreateForm(TTestForm, TestForm);
  Application.Run;
end.

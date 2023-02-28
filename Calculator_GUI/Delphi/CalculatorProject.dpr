program CalculatorProject;

uses
  System.StartUpCopy,
  FMX.Forms,
  Calculator in 'Calculator.pas' {CalculatorGUI};

{$R *.res}

begin
  Application.Initialize;
  Application.CreateForm(TCalculatorGUI, CalculatorGUI);
  Application.Run;
end.

program UnitConversionApp;

uses
  System.StartUpCopy,
  FMX.Forms,
  TimeForm in 'TimeForm.pas' {Time},
  TemperatueForm in 'TemperatueForm.pas' {Temperature},
  LengthForm in 'LengthForm.pas' {Length},
  WeightForm in 'WeightForm.pas' {Weight},
  MainForm in 'MainForm.pas' {Main};

{$R *.res}

begin
  Application.Initialize;
  Application.CreateForm(TTime, Time);
  Application.CreateForm(TTemperature, Temperature);
  Application.CreateForm(TLength, Length);
  Application.CreateForm(TWeight, Weight);
  Application.CreateForm(TMain, Main);
  Application.Run;
end.

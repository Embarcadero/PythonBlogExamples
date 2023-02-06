program CurrencyConversion;

uses
  System.StartUpCopy,
  FMX.Forms,
  CurrencyConverter in 'CurrencyConverter.pas' {CurrencyConverterApp};

{$R *.res}

begin
  Application.Initialize;
  Application.CreateForm(TCurrencyConverterApp, CurrencyConverterApp);
  Application.Run;
end.

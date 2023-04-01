program StopwatchTimerApp;

uses
  System.StartUpCopy,
  FMX.Forms,
  Stopwatch in 'Stopwatch.pas' {StopwatchForm},
  Timer in 'Timer.pas' {TimerForm},
  MainMenu in 'MainMenu.pas' {MainForm};

{$R *.res}

begin
  Application.Initialize;
  Application.CreateForm(TStopwatchForm, StopwatchForm);
  Application.CreateForm(TTimerForm, TimerForm);
  Application.CreateForm(TMainForm, MainForm);
  Application.Run;
end.

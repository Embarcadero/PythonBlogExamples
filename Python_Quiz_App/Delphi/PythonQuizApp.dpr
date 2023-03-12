program PythonQuizApp;

uses
  System.StartUpCopy,
  FMX.Forms,
  Main in 'Main.pas' {MainForm},
  Quiz in 'Quiz.pas' {QuizForm},
  Results in 'Results.pas' {ResultsForm};

{$R *.res}

begin
  Application.Initialize;
  Application.CreateForm(TMainForm, MainForm);
  Application.CreateForm(TQuizForm, QuizForm);
  Application.CreateForm(TResultsForm, ResultsForm);
  Application.Run;
end.

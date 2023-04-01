unit Stopwatch;

interface

uses
  System.SysUtils, System.Types, System.UITypes, System.Classes, System.Variants,
  FMX.Types, FMX.Controls, FMX.Forms, FMX.Graphics, FMX.Dialogs, FMX.StdCtrls,
  FMX.Controls.Presentation;

type
  TStopwatchForm = class(TForm)
    Title: TLabel;
    Time: TLabel;
    Play: TButton;
    Pause: TButton;
    Reset: TButton;
    Back: TButton;
    Timer1: TTimer;
    procedure PlayClick(Sender: TObject);
    procedure PauseClick(Sender: TObject);
    procedure ResetClick(Sender: TObject);
    procedure BackClick(Sender: TObject);
    procedure Timer1Timer(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  StopwatchForm: TStopwatchForm;

implementation

{$R *.fmx}

procedure TStopwatchForm.BackClick(Sender: TObject);
begin
//
end;

procedure TStopwatchForm.PauseClick(Sender: TObject);
begin
//
end;

procedure TStopwatchForm.PlayClick(Sender: TObject);
begin
//
end;

procedure TStopwatchForm.ResetClick(Sender: TObject);
begin
//
end;

procedure TStopwatchForm.Timer1Timer(Sender: TObject);
begin
//
end;

end.

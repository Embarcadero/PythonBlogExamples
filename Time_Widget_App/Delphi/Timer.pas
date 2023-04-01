unit Timer;

interface

uses
  System.SysUtils, System.Types, System.UITypes, System.Classes, System.Variants,
  FMX.Types, FMX.Controls, FMX.Forms, FMX.Graphics, FMX.Dialogs, FMX.StdCtrls,
  FMX.Controls.Presentation, FMX.ListBox, FMX.Edit;

type
  TTimerForm = class(TForm)
    Title: TLabel;
    Time: TLabel;
    Start: TButton;
    Pause: TButton;
    Reset: TButton;
    ComboBox1: TComboBox;
    Timer1: TTimer;
    Back: TButton;
    TimeDuration: TEdit;
    Status: TLabel;
    procedure StartClick(Sender: TObject);
    procedure PauseClick(Sender: TObject);
    procedure ResetClick(Sender: TObject);
    procedure BackClick(Sender: TObject);
    procedure Timer1Timer(Sender: TObject);
    procedure ComboSelected(Sender: TObject);
    procedure SetOtherTime(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  TimerForm: TTimerForm;

implementation

{$R *.fmx}

procedure TTimerForm.BackClick(Sender: TObject);
begin
//
end;

procedure TTimerForm.ComboSelected(Sender: TObject);
begin
//
end;

procedure TTimerForm.SetOtherTime(Sender: TObject);
begin
//
end;

procedure TTimerForm.PauseClick(Sender: TObject);
begin
//
end;

procedure TTimerForm.StartClick(Sender: TObject);
begin
//
end;

procedure TTimerForm.ResetClick(Sender: TObject);
begin
//
end;

procedure TTimerForm.Timer1Timer(Sender: TObject);
begin
//
end;

end.

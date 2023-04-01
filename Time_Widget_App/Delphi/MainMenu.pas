unit MainMenu;

interface

uses
  System.SysUtils, System.Types, System.UITypes, System.Classes, System.Variants,
  FMX.Types, FMX.Controls, FMX.Forms, FMX.Graphics, FMX.Dialogs,
  FMX.Controls.Presentation, FMX.StdCtrls;

type
  TMainForm = class(TForm)
    Title: TLabel;
    StopwatchFormButton: TButton;
    TimerFormButton: TButton;
    procedure StopwatchFormButtonClick(Sender: TObject);
    procedure TimerFormButtonClick(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  MainForm: TMainForm;

implementation

{$R *.fmx}

procedure TMainForm.StopwatchFormButtonClick(Sender: TObject);
begin
//
end;

procedure TMainForm.TimerFormButtonClick(Sender: TObject);
begin
//
end;

end.

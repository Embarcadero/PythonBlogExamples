unit MainForm;

interface

uses
  System.SysUtils, System.Types, System.UITypes, System.Classes, System.Variants,
  FMX.Types, FMX.Controls, FMX.Forms, FMX.Graphics, FMX.Dialogs, FMX.ListBox,
  FMX.StdCtrls, FMX.Controls.Presentation, FMX.Edit;

type
  TMain = class(TForm)
    Title: TLabel;
    TemperatureFromButton: TButton;
    LengthFormButton: TButton;
    WeightFromButton: TButton;
    TimeFormButton: TButton;
    procedure LengthFormButtonClick(Sender: TObject);
    procedure TemperatureFromButtonClick(Sender: TObject);
    procedure TimeFormButtonClick(Sender: TObject);
    procedure WeightFromButtonClick(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Main: TMain;

implementation

{$R *.fmx}

procedure TMain.LengthFormButtonClick(Sender: TObject);
begin
//
end;

procedure TMain.TemperatureFromButtonClick(Sender: TObject);
begin
//
end;

procedure TMain.TimeFormButtonClick(Sender: TObject);
begin
//
end;

procedure TMain.WeightFromButtonClick(Sender: TObject);
begin
//
end;

end.

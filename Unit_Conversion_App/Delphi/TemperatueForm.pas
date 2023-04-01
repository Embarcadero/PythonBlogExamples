unit TemperatueForm;

interface

uses
  System.SysUtils, System.Types, System.UITypes, System.Classes, System.Variants,
  FMX.Types, FMX.Controls, FMX.Forms, FMX.Graphics, FMX.Dialogs, FMX.ListBox,
  FMX.StdCtrls, FMX.Controls.Presentation, FMX.Edit;

type
  TTemperature = class(TForm)
    FromValue: TEdit;
    UnitFromLabel: TLabel;
    ValueFromLabel: TLabel;
    Title: TLabel;
    FromLabel: TLabel;
    ToLabel: TLabel;
    Convert: TButton;
    FromUnit: TComboBox;
    ToUnit: TComboBox;
    ToValue: TLabel;
    UnitToLabel: TLabel;
    ValueToLabel: TLabel;
    BackButton: TButton;
    Status: TLabel;
    procedure BackButtonClick(Sender: TObject);
    procedure ConvertClick(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Temperature: TTemperature;

implementation

{$R *.fmx}

procedure TTemperature.BackButtonClick(Sender: TObject);
begin
//
end;

procedure TTemperature.ConvertClick(Sender: TObject);
begin
//
end;

end.

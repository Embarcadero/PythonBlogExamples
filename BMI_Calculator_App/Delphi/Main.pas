unit Main;

interface

uses
  System.SysUtils, System.Types, System.UITypes, System.Classes, System.Variants,
  FMX.Types, FMX.Controls, FMX.Forms, FMX.Graphics, FMX.Dialogs, FMX.StdCtrls,
  FMX.Controls.Presentation, FMX.Edit;

type
  TMainForm = class(TForm)
    WeightEdit: TEdit;
    HeightFeetEdit: TEdit;
    ResultsButton: TButton;
    HeightLabel: TLabel;
    WeightLabel: TLabel;
    Title: TLabel;
    PoundsRadio: TRadioButton;
    KgRadio: TRadioButton;
    FeetLabel: TLabel;
    HeightInchEdit: TEdit;
    InchLabel: TLabel;
    Status: TLabel;
    procedure ResultsButtonClick(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  MainForm: TMainForm;

implementation

{$R *.fmx}

procedure TMainForm.ResultsButtonClick(Sender: TObject);
begin
//
end;

end.

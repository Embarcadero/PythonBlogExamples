unit Main;

interface

uses
  System.SysUtils, System.Types, System.UITypes, System.Classes, System.Variants,
  FMX.Types, FMX.Controls, FMX.Forms, FMX.Graphics, FMX.Dialogs,
  FMX.Controls.Presentation, FMX.StdCtrls, FMX.Edit;

type
  TMainForm = class(TForm)
    Title: TLabel;
    SLength: TLabel;
    SWidth: TLabel;
    PWidth: TLabel;
    Result: TLabel;
    PLength: TLabel;
    SLengthEdit: TEdit;
    SWidthEdit: TEdit;
    PLengthEdit: TEdit;
    PWidthEdit: TEdit;
    Predict: TButton;
    StyleBook1: TStyleBook;
    procedure PredictClick(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  MainForm: TMainForm;

implementation

{$R *.fmx}


procedure TMainForm.PredictClick(Sender: TObject);
begin
//
end;


end.

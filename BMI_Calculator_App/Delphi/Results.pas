unit Results;

interface

uses
  System.SysUtils, System.Types, System.UITypes, System.Classes, System.Variants,
  FMX.Types, FMX.Controls, FMX.Forms, FMX.Graphics, FMX.Dialogs, FMX.StdCtrls,
  FMX.Controls.Presentation;

type
  TResultsForm = class(TForm)
    BMIScore: TLabel;
    Label1: TLabel;
    DetailsLabel: TLabel;
    CategoryLabel: TLabel;
    Title: TLabel;
    procedure ResetClick(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  ResultsForm: TResultsForm;

implementation

{$R *.fmx}

procedure TResultsForm.ResetClick(Sender: TObject);
begin
//
end;

end.

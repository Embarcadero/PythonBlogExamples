unit Main;

interface

uses
  System.SysUtils, System.Types, System.UITypes, System.Classes, System.Variants,
  FMX.Types, FMX.Controls, FMX.Forms, FMX.Graphics, FMX.Dialogs, FMX.StdCtrls,
  FMX.Edit, FMX.Controls.Presentation, FMX.Objects;

type
  TMainForm = class(TForm)
    Title: TLabel;
    Result: TLabel;
    FileName: TLabel;
    FilePickButton: TButton;
    ResultButton: TButton;
    OpenDialog1: TOpenDialog;
    SentimentTextEdit: TEdit;
    TextboxRadio: TRadioButton;
    FilePickerRadio: TRadioButton;
    StyleBook1: TStyleBook;
    Image1: TImage;
    procedure ResultButtonClick(Sender: TObject);
    procedure FilePickButtonClick(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  MainForm: TMainForm;

implementation

{$R *.fmx}

procedure TMainForm.FilePickButtonClick(Sender: TObject);
begin
//
end;

procedure TMainForm.ResultButtonClick(Sender: TObject);
begin
//
end;

end.

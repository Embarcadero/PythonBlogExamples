unit Main;

interface

uses
  System.SysUtils, System.Types, System.UITypes, System.Classes, System.Variants,
  FMX.Types, FMX.Controls, FMX.Forms, FMX.Graphics, FMX.Dialogs, FMX.Objects,
  FMX.StdCtrls, FMX.Edit, FMX.Controls.Presentation;

type
  TMainForm = class(TForm)
    Title: TLabel;
    KValue: TEdit;
    KLabel: TLabel;
    ApplyButton: TButton;
    UploadButton: TButton;
    OpenDialog1: TOpenDialog;
    BeforeImage: TImage;
    AfterImage: TImage;
    StyleBook1: TStyleBook;
    procedure UploadButtonClick(Sender: TObject);
    procedure ApplyButtonClick(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  MainForm: TMainForm;

implementation

{$R *.fmx}

procedure TMainForm.ApplyButtonClick(Sender: TObject);
begin
//
end;

procedure TMainForm.UploadButtonClick(Sender: TObject);
begin
//
end;

end.

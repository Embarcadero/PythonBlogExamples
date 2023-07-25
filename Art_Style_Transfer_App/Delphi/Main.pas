unit Main;

interface

uses
  System.SysUtils, System.Types, System.UITypes, System.Classes, System.Variants,
  FMX.Types, FMX.Controls, FMX.Forms, FMX.Graphics, FMX.Dialogs, FMX.Objects,
  FMX.StdCtrls, FMX.Controls.Presentation;

type
  TMainForm = class(TForm)
    Title: TLabel;
    StyleImageLabel: TLabel;
    ContentImageLabel: TLabel;
    UploadContentButton: TButton;
    UploadStyleButton: TButton;
    ApplyButton: TButton;
    StyleImage: TImage;
    ContentImage: TImage;
    FinalImage: TImage;
    OpenDialog1: TOpenDialog;
    OpenDialog2: TOpenDialog;
    StyleBook1: TStyleBook;
    procedure UploadStyleButtonClick(Sender: TObject);
    procedure UploadContentButtonClick(Sender: TObject);
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

procedure TMainForm.UploadContentButtonClick(Sender: TObject);
begin
//
end;

procedure TMainForm.UploadStyleButtonClick(Sender: TObject);
begin
//
end;

end.

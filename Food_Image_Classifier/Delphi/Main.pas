unit Main;

interface

uses
  System.SysUtils, System.Types, System.UITypes, System.Classes, System.Variants,
  FMX.Types, FMX.Controls, FMX.Forms, FMX.Graphics, FMX.Dialogs, FMX.StdCtrls,
  FMX.Controls.Presentation;

type
  TMainForm = class(TForm)
    Title: TLabel;
    FileNameLabel: TLabel;
    ResultLabel: TLabel;
    FileName: TLabel;
    FileSelectButton: TButton;
    ClassifyButton: TButton;
    OpenDialog1: TOpenDialog;
    StyleBook1: TStyleBook;
    procedure FileSelectButtonClick(Sender: TObject);
    procedure ClassifyButtonClick(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  MainForm: TMainForm;

implementation

{$R *.fmx}

procedure TMainForm.ClassifyButtonClick(Sender: TObject);
begin
//
end;

procedure TMainForm.FileSelectButtonClick(Sender: TObject);
begin
//
end;

end.

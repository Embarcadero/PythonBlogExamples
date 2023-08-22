unit Bio;

interface

uses
  System.SysUtils, System.Types, System.UITypes, System.Classes, System.Variants,
  FMX.Types, FMX.Controls, FMX.Forms, FMX.Graphics, FMX.Dialogs, FMX.Objects,
  FMX.Edit, FMX.EditBox, FMX.NumberBox, FMX.Controls.Presentation, FMX.StdCtrls;

type
  TBioScreen = class(TForm)
    TitleLabel: TLabel;
    AgeLabel: TLabel;
    NameLabel: TLabel;
    AgeNumberBox: TNumberBox;
    NameEdit: TEdit;
    Image1: TImage;
    StartButton: TButton;
    StyleBook1: TStyleBook;
    procedure StartButtonClick(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  BioScreen: TBioScreen;

implementation

{$R *.fmx}

procedure TBioScreen.StartButtonClick(Sender: TObject);
begin
//
end;

end.

unit Game;

interface

uses
  System.SysUtils, System.Types, System.UITypes, System.Classes, System.Variants,
  FMX.Types, FMX.Controls, FMX.Forms, FMX.Graphics, FMX.Dialogs,
  FMX.Controls.Presentation, FMX.StdCtrls;

type
  TGameForm = class(TForm)
    ScoreLabel: TLabel;
    Number: TLabel;
    HighButton: TButton;
    LowButton: TButton;
    AgainButton: TButton;
    StatusLabel: TLabel;
    StyleBook1: TStyleBook;
    procedure HighButtonClick(Sender: TObject);
    procedure LowButtonClick(Sender: TObject);
    procedure AgainButtonClick(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  GameForm: TGameForm;

implementation

{$R *.fmx}

procedure TGameForm.AgainButtonClick(Sender: TObject);
begin
//
end;

procedure TGameForm.HighButtonClick(Sender: TObject);
begin
//
end;

procedure TGameForm.LowButtonClick(Sender: TObject);
begin
//
end;

end.

unit TicTacToe;

interface

uses
  System.SysUtils, System.Types, System.UITypes, System.Classes, System.Variants,
  FMX.Types, FMX.Controls, FMX.Forms, FMX.Graphics, FMX.Dialogs,
  FMX.Controls.Presentation, FMX.StdCtrls, FMX.Objects;

type
  TForm2 = class(TForm)
    Title: TLabel;
    Status: TLabel;
    Line1: TLine;
    Line2: TLine;
    Line3: TLine;
    Line4: TLine;
    Pos1: TButton;
    Pos2: TButton;
    Pos3: TButton;
    Pos4: TButton;
    Pos6: TButton;
    Pos5: TButton;
    Pos7: TButton;
    Pos8: TButton;
    Pos9: TButton;
    Reset: TButton;
    procedure FormCreate(Sender: TObject);
    procedure Line4Click(Sender: TObject);
    procedure Pos1Click(Sender: TObject);
    procedure Pos2Click(Sender: TObject);
    procedure Pos3Click(Sender: TObject);
    procedure Pos4Click(Sender: TObject);
    procedure Pos5Click(Sender: TObject);
    procedure Pos6Click(Sender: TObject);
    procedure Pos7Click(Sender: TObject);
    procedure Pos8Click(Sender: TObject);
    procedure Pos9Click(Sender: TObject);
    procedure ResetClick(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form2: TForm2;

implementation

{$R *.fmx}

procedure TForm2.FormCreate(Sender: TObject);
begin
    //
end;

procedure TForm2.Line4Click(Sender: TObject);
begin
    //
end;

procedure TForm2.Pos1Click(Sender: TObject);
begin
    //
end;

procedure TForm2.Pos2Click(Sender: TObject);
begin
    //
end;

procedure TForm2.Pos3Click(Sender: TObject);
begin
    //
end;

procedure TForm2.Pos4Click(Sender: TObject);
begin
    //
end;

procedure TForm2.Pos5Click(Sender: TObject);
begin
    //
end;

procedure TForm2.Pos6Click(Sender: TObject);
begin
    //
end;

procedure TForm2.Pos7Click(Sender: TObject);
begin
    //
end;

procedure TForm2.Pos8Click(Sender: TObject);
begin
    //
end;

procedure TForm2.Pos9Click(Sender: TObject);
begin
    //
end;

procedure TForm2.ResetClick(Sender: TObject);
begin
  //
end;

end.

unit Tic_Tac_Toe;

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
    Z: TLine;
    Pos1: TLabel;
    Pos2: TLabel;
    Pos3: TLabel;
    Pos5: TLabel;
    Pos4: TLabel;
    Pos6: TLabel;
    Pos7: TLabel;
    Pos8: TLabel;
    Pos9: TLabel;
    Button1: TButton;
    procedure Pos1Click(Sender: TObject);
    procedure Pos2Click(Sender: TObject);
    procedure Pos3Click(Sender: TObject);
    procedure Pos4Click(Sender: TObject);
    procedure Pos5Click(Sender: TObject);
    procedure Pos6Click(Sender: TObject);
    procedure Pos7Click(Sender: TObject);
    procedure Pos8Click(Sender: TObject);
    procedure Pos9Click(Sender: TObject);
    procedure Button1Click(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form2: TForm2;

implementation

{$R *.fmx}

procedure TForm2.Button1Click(Sender: TObject);
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

end.

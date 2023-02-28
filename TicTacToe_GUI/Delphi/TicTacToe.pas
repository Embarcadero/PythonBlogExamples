unit TicTacToe;

interface

uses
  System.SysUtils, System.Types, System.UITypes, System.Classes, System.Variants,
  FMX.Types, FMX.Controls, FMX.Forms, FMX.Graphics, FMX.Dialogs, FMX.StdCtrls,
  FMX.Objects, FMX.Controls.Presentation;

type
  TTicTacToeGUI = class(TForm)
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
    Title: TLabel;
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
  TicTacToeGUI: TTicTacToeGUI;

implementation

{$R *.fmx}

procedure TTicTacToeGUI.Pos1Click(Sender: TObject);
begin
//
end;

procedure TTicTacToeGUI.Pos2Click(Sender: TObject);
begin
//
end;

procedure TTicTacToeGUI.Pos3Click(Sender: TObject);
begin
//
end;

procedure TTicTacToeGUI.Pos4Click(Sender: TObject);
begin
//
end;

procedure TTicTacToeGUI.Pos5Click(Sender: TObject);
begin
//
end;

procedure TTicTacToeGUI.Pos6Click(Sender: TObject);
begin
//
end;

procedure TTicTacToeGUI.Pos7Click(Sender: TObject);
begin
//
end;

procedure TTicTacToeGUI.Pos8Click(Sender: TObject);
begin
//
end;

procedure TTicTacToeGUI.Pos9Click(Sender: TObject);
begin
//
end;

procedure TTicTacToeGUI.ResetClick(Sender: TObject);
begin
//
end;

end.

unit Calculator;

interface

uses
  System.SysUtils, System.Types, System.UITypes, System.Classes, System.Variants,
  FMX.Types, FMX.Controls, FMX.Forms, FMX.Graphics, FMX.Dialogs, FMX.StdCtrls,
  FMX.Controls.Presentation;

type
  TCalculatorGUI = class(TForm)
    Del: TButton;
    C: TButton;
    Percent: TButton;
    Plus: TButton;
    Seven: TButton;
    Eight: TButton;
    Nine: TButton;
    Minus: TButton;
    Four: TButton;
    Five: TButton;
    Six: TButton;
    Multiply: TButton;
    One: TButton;
    Two: TButton;
    Three: TButton;
    Zero: TButton;
    Dot: TButton;
    Divide: TButton;
    Equals: TButton;
    Results: TLabel;
    Calc: TLabel;
    procedure DelClick(Sender: TObject);
    procedure ResultsClick(Sender: TObject);
    procedure CClick(Sender: TObject);
    procedure PercentClick(Sender: TObject);
    procedure PlusClick(Sender: TObject);
    procedure SevenClick(Sender: TObject);
    procedure EightClick(Sender: TObject);
    procedure NineClick(Sender: TObject);
    procedure MinusClick(Sender: TObject);
    procedure FourClick(Sender: TObject);
    procedure FiveClick(Sender: TObject);
    procedure SixClick(Sender: TObject);
    procedure MultiplyClick(Sender: TObject);
    procedure OneClick(Sender: TObject);
    procedure TwoClick(Sender: TObject);
    procedure ThreeClick(Sender: TObject);
    procedure DivideClick(Sender: TObject);
    procedure ZeroClick(Sender: TObject);
    procedure DotClick(Sender: TObject);
    procedure EqualsClick(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  CalculatorGUI: TCalculatorGUI;

implementation

{$R *.fmx}

procedure TCalculatorGUI.DelClick(Sender: TObject);
begin
     //
end;procedure TCalculatorGUI.ResultsClick(Sender: TObject);
begin
     //
end;
procedure TCalculatorGUI.CClick(Sender: TObject);
begin
     //
end;

procedure TCalculatorGUI.DivideClick(Sender: TObject);
begin
     //
end;

procedure TCalculatorGUI.DotClick(Sender: TObject);
begin
     //
end;

procedure TCalculatorGUI.EightClick(Sender: TObject);
begin
     //
end;

procedure TCalculatorGUI.EqualsClick(Sender: TObject);
begin
     //
end;

procedure TCalculatorGUI.FiveClick(Sender: TObject);
begin
     //
end;

procedure TCalculatorGUI.FourClick(Sender: TObject);
begin
     //
end;

procedure TCalculatorGUI.MinusClick(Sender: TObject);
begin
     //
end;

procedure TCalculatorGUI.MultiplyClick(Sender: TObject);
begin
     //
end;

procedure TCalculatorGUI.NineClick(Sender: TObject);
begin
     //
end;

procedure TCalculatorGUI.OneClick(Sender: TObject);
begin
     //
end;

procedure TCalculatorGUI.PercentClick(Sender: TObject);
begin
     //
end;

procedure TCalculatorGUI.PlusClick(Sender: TObject);
begin
     //
end;

procedure TCalculatorGUI.SevenClick(Sender: TObject);
begin
     //
end;

procedure TCalculatorGUI.SixClick(Sender: TObject);
begin
     //
end;

procedure TCalculatorGUI.ThreeClick(Sender: TObject);
begin
     //
end;

procedure TCalculatorGUI.TwoClick(Sender: TObject);
begin
     //
end;

procedure TCalculatorGUI.ZeroClick(Sender: TObject);
begin
     //
end;

end.

unit CurrencyConverter;

interface

uses
  System.SysUtils, System.Types, System.UITypes, System.Classes, System.Variants,
  FMX.Types, FMX.Controls, FMX.Forms, FMX.Graphics, FMX.Dialogs, FMX.StdCtrls,
  FMX.Controls.Presentation, FMX.Edit, FMX.ListBox;

type
  TCurrencyConverterApp = class(TForm)
    FromAmount: TEdit;
    Currency1: TLabel;
    Amount1: TLabel;
    Currency2: TLabel;
    Amount2: TLabel;
    Title: TLabel;
    FromLabel: TLabel;
    ToLabel: TLabel;
    Convert: TButton;
    FromCurrency: TComboBox;
    ToCurrency: TComboBox;
    ToAmount: TLabel;
    procedure ConvertClick(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  CurrencyConverterApp: TCurrencyConverterApp;

implementation

{$R *.fmx}

procedure TCurrencyConverterApp.ConvertClick(Sender: TObject);
begin
  //
end;

end.

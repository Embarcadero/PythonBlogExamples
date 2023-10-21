unit Main;

interface

uses
  System.SysUtils, System.Types, System.UITypes, System.Classes, System.Variants,
  FMX.Types, FMX.Controls, FMX.Forms, FMX.Graphics, FMX.Dialogs, FMX.Memo.Types,
  FMX.EditBox, FMX.SpinBox, FMX.Edit, FMX.Objects, FMX.StdCtrls, FMX.ScrollBox,
  FMX.Memo, FMX.Calendar, FMX.Controls.Presentation, FMX.TabControl, FMX.ListBox;

type
  TMainForm = class(TForm)
    TabControl1: TTabControl;
    HistoricalTab: TTabItem;
    HistoryButton: TButton;
    Calendar1: TCalendar;
    HistoricalMemo: TMemo;
    DateLabel: TLabel;
    CurrentTab: TTabItem;
    CurrentButton: TButton;
    Image1: TImage;
    CurrentMemo: TMemo;
    PredictionTab: TTabItem;
    Edit2: TEdit;
    TitleLabel: TLabel;
    CityLabel: TLabel;
    CityCombo: TComboBox;
    TabControl2: TTabControl;
    TabItem1: TTabItem;
    Button1: TButton;
    Calendar2: TCalendar;
    Memo1: TMemo;
    Label1: TLabel;
    TabItem2: TTabItem;
    Button2: TButton;
    Image2: TImage;
    Memo2: TMemo;
    TabItem3: TTabItem;
    Edit1: TEdit;
    PredictButton: TButton;
    SpinBox1: TSpinBox;
    PredictLabel: TLabel;
    PredictLabel2: TLabel;
    PredictMemo: TMemo;
    StyleBook1: TStyleBook;
    procedure HistoryButtonClick(Sender: TObject);
    procedure CurrentButtonClick(Sender: TObject);
    procedure PredictButtonClick(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  MainForm: TMainForm;

implementation

{$R *.fmx}

procedure TMainForm.CurrentButtonClick(Sender: TObject);
begin
//
end;

procedure TMainForm.HistoryButtonClick(Sender: TObject);
begin
//
end;

procedure TMainForm.PredictButtonClick(Sender: TObject);
begin
//
end;

end.

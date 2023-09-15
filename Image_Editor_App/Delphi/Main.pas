unit Main;

interface

uses
  System.SysUtils, System.Types, System.UITypes, System.Classes, System.Variants,
  FMX.Types, FMX.Controls, FMX.Forms, FMX.Graphics, FMX.Dialogs, FMX.TabControl,
  FMX.StdCtrls, FMX.Edit, FMX.EditBox, FMX.SpinBox, FMX.ListBox, FMX.Objects,
  FMX.Controls.Presentation;

type
  TMainFrom = class(TForm)
    TabControl1: TTabControl;
    Edit: TTabItem;
    FilenameLabel: TLabel;
    EffectLabel: TLabel;
    IntensityLabel: TLabel;
    WidthLabel: TLabel;
    HeightLabel: TLabel;
    BackgroundRemoval: TTabItem;
    RemoveBgImage: TImage;
    RemoveButton: TButton;
    TransformButton: TButton;
    FileButton: TButton;
    EffectComboBox: TComboBox;
    SpinBox1: TSpinBox;
    DimensionsCheckBox: TCheckBox;
    EditImage: TImage;
    OpenDialog1: TOpenDialog;
    StyleBook1: TStyleBook;
    WidthEdit: TEdit;
    HeightEdit: TEdit;
    procedure TransformButtonClick(Sender: TObject);
    procedure FileButtonClick(Sender: TObject);
    procedure RemoveButtonClick(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  MainFrom: TMainFrom;

implementation

{$R *.fmx}

procedure TMainFrom.FileButtonClick(Sender: TObject);
begin
//
end;

procedure TMainFrom.RemoveButtonClick(Sender: TObject);
begin
//
end;

procedure TMainFrom.TransformButtonClick(Sender: TObject);
begin
//
end;

end.

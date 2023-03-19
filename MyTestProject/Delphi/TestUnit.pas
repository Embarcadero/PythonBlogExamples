unit TestUnit;

interface

uses
  System.SysUtils, System.Types, System.UITypes, System.Classes, System.Variants,
  FMX.Types, FMX.Controls, FMX.Forms, FMX.Graphics, FMX.Dialogs, FMX.StdCtrls,
  FMX.Layouts, FMX.ListBox, FMX.Edit, FMX.Controls.Presentation;

type
  TTestForm = class(TForm)
    Label1: TLabel;
    taskEdit: TEdit;
    listBox: TListBox;
    btnAdd: TButton;
    bthDelete: TButton;
    procedure btnAddClick(Sender: TObject);
    procedure bthDeleteClick(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  TestForm: TTestForm;

implementation

{$R *.fmx}

procedure TTestForm.bthDeleteClick(Sender: TObject);
begin
//
end;

procedure TTestForm.btnAddClick(Sender: TObject);
begin
//
end;

end.

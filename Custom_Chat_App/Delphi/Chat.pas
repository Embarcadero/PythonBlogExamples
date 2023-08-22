unit Chat;

interface

uses
  System.SysUtils, System.Types, System.UITypes, System.Classes, System.Variants,
  FMX.Types, FMX.Controls, FMX.Forms, FMX.Graphics, FMX.Dialogs, FMX.Memo.Types,
  FMX.ScrollBox, FMX.Memo, FMX.StdCtrls, FMX.Edit, FMX.Controls.Presentation;

type
  TChatScreen = class(TForm)
    SendButton: TButton;
    UserQsEdit: TEdit;
    Header: TToolBar;
    HeaderLabel: TLabel;
    Footer: TToolBar;
    BackButton: TButton;
    ChatMemo: TMemo;
    StyleBook1: TStyleBook;
    procedure BackButtonClick(Sender: TObject);
    procedure SendButtonClick(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  ChatScreen: TChatScreen;

implementation

{$R *.fmx}

procedure TChatScreen.BackButtonClick(Sender: TObject);
begin
    //
end;

procedure TChatScreen.SendButtonClick(Sender: TObject);
begin
        //
end;

end.

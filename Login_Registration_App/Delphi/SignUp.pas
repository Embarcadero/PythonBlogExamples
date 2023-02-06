unit SignUp;

interface

uses
  System.SysUtils, System.Types, System.UITypes, System.Classes, System.Variants,
  FMX.Types, FMX.Controls, FMX.Forms, FMX.Graphics, FMX.Dialogs,
  FMX.Controls.Presentation, FMX.StdCtrls, FMX.Edit;

type
  TSignUpForm = class(TForm)
    Register: TLabel;
    FnameText: TEdit;
    Fname: TLabel;
    LNameText: TEdit;
    LName: TLabel;
    EmailText: TEdit;
    Email: TLabel;
    PasswordText: TEdit;
    Password: TLabel;
    CPasswordText: TEdit;
    CPassword: TLabel;
    Signup: TButton;
    Status: TLabel;
    procedure SignupClick(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  SignUpForm: TSignUpForm;

implementation

{$R *.fmx}



procedure TSignUpForm.SignupClick(Sender: TObject);
begin
  //
end;

end.

unit SignIn;

interface

uses
  System.SysUtils, System.Types, System.UITypes, System.Classes, System.Variants,
  FMX.Types, FMX.Controls, FMX.Forms, FMX.Graphics, FMX.Dialogs, FMX.StdCtrls,
  FMX.Edit, FMX.Controls.Presentation;

type
  TSignInForm = class(TForm)
    Login: TLabel;
    Email: TLabel;
    PasswordText: TEdit;
    Password: TLabel;
    Signin: TButton;
    EmailText: TEdit;
    Status: TLabel;
    Signup: TButton;
    procedure SigninClick(Sender: TObject);
    procedure SignupClick(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  SignInForm: TSignInForm;

implementation

{$R *.fmx}

procedure TSignInForm.SigninClick(Sender: TObject);
begin
  //
end;

procedure TSignInForm.SignupClick(Sender: TObject);
begin
  //
end;

end.

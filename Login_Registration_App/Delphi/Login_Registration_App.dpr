program Login_Registration_App;

uses
  System.StartUpCopy,
  FMX.Forms,
  SignUp in 'SignUp.pas' {SignUpForm},
  SignIn in 'SignIn.pas' {SignInForm};

{$R *.res}

begin
  Application.Initialize;
  Application.CreateForm(TSignUpForm, SignUpForm);
  Application.CreateForm(TSignInForm, SignInForm);
  Application.Run;
end.

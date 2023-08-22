program ChatApplication;

uses
  System.StartUpCopy,
  FMX.Forms,
  Bio in 'Bio.pas' {BioScreen},
  Chat in 'Chat.pas' {ChatScreen};

{$R *.res}

begin
  Application.Initialize;
  Application.CreateForm(TBioScreen, BioScreen);
  Application.CreateForm(TChatScreen, ChatScreen);
  Application.Run;
end.

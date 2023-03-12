unit Quiz;

interface

uses
  System.SysUtils, System.Types, System.UITypes, System.Classes, System.Variants,
  FMX.Types, FMX.Controls, FMX.Forms, FMX.Graphics, FMX.Dialogs, FMX.StdCtrls,
  FMX.Controls.Presentation;

type
  TQuizForm = class(TForm)
    QuestionNumberLabel: TLabel;
    Question: TLabel;
    OptionA: TButton;
    OptionB: TButton;
    OptionC: TButton;
    OptionD: TButton;
    NextQuestion: TButton;
    AnswerStatus: TLabel;
    procedure OptionAClick(Sender: TObject);
    procedure OptionBClick(Sender: TObject);
    procedure OptionCClick(Sender: TObject);
    procedure OptionDClick(Sender: TObject);
    procedure NextQuestionClick(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  QuizForm: TQuizForm;

implementation

{$R *.fmx}

procedure TQuizForm.NextQuestionClick(Sender: TObject);
begin
//
end;

procedure TQuizForm.OptionAClick(Sender: TObject);
begin
//
end;

procedure TQuizForm.OptionBClick(Sender: TObject);
begin
//
end;

procedure TQuizForm.OptionCClick(Sender: TObject);
begin
//
end;

procedure TQuizForm.OptionDClick(Sender: TObject);
begin
//
end;

end.

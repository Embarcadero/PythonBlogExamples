import os
from delphifmx import *
from Results import ResultsForm  # import result form to create window


class QuizForm(Form):

    def __init__(self, owner, QuestionNumber, Score):
        self.QuestionNumberLabel = None
        self.Question = None
        self.OptionA = None
        self.OptionB = None
        self.OptionC = None
        self.OptionD = None
        self.NextQuestion = None
        self.AnswerStatus = None
        self.LoadProps(os.path.join(os.path.dirname(
            os.path.abspath(__file__)), "Quiz.pyfmx"))

        # Store variables from previous form to make them accessible
        self.QuestionNumber = QuestionNumber
        self.Score = Score

        # Dictionary with all of the quiz data
        self.QuizQuestions = {
            1: {"Question": "Which operator has higher precedence:", "Answer": "** (Exponent)", "Options": ["> (Comparison)", "** (Exponent)", "& (BitWise AND)", "% (Modulus)"]},
            2: {"Question": "What is a correct syntax to output 'Hello World' in Python?", "Answer": "print('Hello World')", "Options": ["print('Hello World')", "print 'Hellow World'", "p('Hello World')", "echo 'Hello World'"]},
            3: {"Question": "How do you insert comments in Python code?", "Answer": "#Comment", "Options": ["#Comment", "//Comment", "!Comment", "/*Comment*/"]},
            4: {"Question": "Which of the following is not a legal variable name", "Answer": "python-GUI", "Options": ["_pythonGUI", "python_GUI", "pythonGUI", "python-GUI"]},
            5: {"Question": "What is the correct syntax to output the type of a variable or object in Python?", "Answer": "print(type(x))", "Options": ["print(type x)", "print(typeOf(x))", "print(type(x))", "print(typeof(x))"]},
            6: {"Question": "What is the correct way to create a function in Python?", "Answer": "def myfunc():", "Options": ["create myfunc():", "function myfunc():", "def myfunc():", "func myfunc():"]},
            7: {"Question": "What is a correct syntax to return the first character in a string?", "Answer": "'PythonGUI'[0]", "Options": ["'PythonGUI'[0]", "'PythonGUI'[1]", "'PythonGUI'.sub(0,1)", "sub('PythonGUI',0,1)"]},
            8: {"Question": "Which method can be used to remove any whitespace from both the beginning and the end of a string?", "Answer": "strip()", "Options": ["len()", "strip()", "split()", "ptrim()"]},
            9: {"Question": "Which collection is ordered, changeable, and allows duplicate members?", "Answer": "List", "Options": ["List", "Dictionary", "Set", "Tuple"]},
            10: {"Question": "Which statement is used to stop a loop?", "Answer": "break", "Options": ["break", "exit", "return", "stop"]}
        }

        # Display options of the current question
        self.OptionA.Text = self.QuizQuestions[self.QuestionNumber]["Options"][0]
        self.OptionB.Text = self.QuizQuestions[self.QuestionNumber]["Options"][1]
        self.OptionC.Text = self.QuizQuestions[self.QuestionNumber]["Options"][2]
        self.OptionD.Text = self.QuizQuestions[self.QuestionNumber]["Options"][3]

        # Display question number
        self.QuestionNumberLabel.Text = str(self.QuestionNumber) + " of 10"

        # Display question text
        self.Question.Text = self.QuizQuestions[self.QuestionNumber]["Question"]

        # Resetting Status
        self.AnswerStatus.Text = ""

    def OptionAClick(self, Sender):
        # Ensure some button not already clicked
        if self.AnswerStatus.Text == "Correct" or self.AnswerStatus.Text == "Incorrect":
            pass
        # If correct answer chosen then increase score and print correct
        elif self.OptionA.Text == self.QuizQuestions[self.QuestionNumber]["Answer"]:
            self.Score += 1
            self.AnswerStatus.Text = "Correct"
        # If incorrect answer chosen then print incorrect
        else:
            self.AnswerStatus.Text = "Incorrect"

    def OptionBClick(self, Sender):
        # Ensure some button not already clicked
        if self.AnswerStatus.Text == "Correct" or self.AnswerStatus.Text == "Incorrect":
            pass
        # If correct answer chosen then increase score and print correct
        elif self.OptionB.Text == self.QuizQuestions[self.QuestionNumber]["Answer"]:
            self.Score += 1
            self.AnswerStatus.Text = "Correct"
        # If incorrect answer chosen then print incorrect
        else:
            self.AnswerStatus.Text = "Incorrect"

    def OptionCClick(self, Sender):
        # Ensure some button not already clicked
        if self.AnswerStatus.Text == "Correct" or self.AnswerStatus.Text == "Incorrect":
            pass
        # If correct answer chosen then increase score and print correct
        elif self.OptionC.Text == self.QuizQuestions[self.QuestionNumber]["Answer"]:
            self.Score += 1
            self.AnswerStatus.Text = "Correct"
        # If incorrect answer chosen then print incorrect
        else:
            self.AnswerStatus.Text = "Incorrect"

    def OptionDClick(self, Sender):
        # Ensure some button not already clicked
        if self.AnswerStatus.Text == "Correct" or self.AnswerStatus.Text == "Incorrect":
            pass
        # If correct answer chosen then increase score and print correct
        elif self.OptionD.Text == self.QuizQuestions[self.QuestionNumber]["Answer"]:
            self.Score += 1
            self.AnswerStatus.Text = "Correct"
        # If incorrect answer chosen then print incorrect
        else:
            self.AnswerStatus.Text = "Incorrect"

    def NextQuestionClick(self, Sender):

        # Checking if user has answered a question.
        # User can only proceed to next question if an answer has been selected
        if self.AnswerStatus.Text == "" or self.AnswerStatus.Text == "Select an answer before proceeding!":
            self.AnswerStatus.Text = "Select an answer before proceeding!"

        else:
            self.QuestionNumber += 1  # Update question number to display the next one
            if self.QuestionNumber <= 10:  # If the ten questions have not been asked
                self.NextQuestionWindow = QuizForm(
                    self, QuestionNumber=self.QuestionNumber, Score=self.Score)
                self.NextQuestionWindow.show()
            else:  # It the ten questions have been asked, show the result form
                self.ResultsWindow = ResultsForm(self, Score=self.Score)
                self.ResultsWindow.show()

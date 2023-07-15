import os
from delphifmx import *

# Additional imports
from transformers import AutoTokenizer, AutoModelForSequenceClassification

class MainForm(Form):

    def __init__(self, owner):
        self.Title = None
        self.Result = None
        self.FileName = None
        self.FilePickButton = None
        self.ResultButton = None
        self.OpenDialog1 = None
        self.SentimentTextEdit = None
        self.TextboxRadio = None
        self.FilePickerRadio = None
        self.Image1 = None
        self.StyleBook1 = None
        self.LoadProps(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Main.pyfmx"))

        # Initialize model and tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
        self.model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")

    def FilePickButtonClick(self, Sender):
        self.OpenDialog1.Title = "Select an Image"

        # Filtering only image formats to show
        self.OpenDialog1.Filter = "Text files (*.txt)|*.txt|All files (*.*)|*.*"

        if self.OpenDialog1.Execute():
                    self.FileName.Text = "Filename: " + os.path.basename(self.OpenDialog1.FileName)

    def ResultButtonClick(self, Sender):
        if self.TextboxRadio.IsChecked:
            text = self.SentimentTextEdit.Text
            print(text)
            self.predict(text)
        elif self.FilePickerRadio.IsChecked:
            with open(self.OpenDialog1.FileName, 'r') as file:
                text = file.read()
            print(text)
            self.predict(text)
        else:
            pass

    def predict(self, text):
        tokens = self.tokenizer.encode_plus(text, return_tensors='pt', padding=True, truncation=True)
        output = self.model(**tokens)
        logits = output.logits
        predicted_label = logits.argmax().item()

        self.Result.Text = "Result: " + self.model.config.id2label[predicted_label]

    def RadioChange(self, Sender):
        if self.TextboxRadio.IsChecked:
            self.SentimentTextEdit.Enabled = True
            self.FilePickButton.Enabled = False
        if self.FilePickerRadio.IsChecked:
            self.SentimentTextEdit.Enabled = False
            self.FilePickButton.Enabled = True
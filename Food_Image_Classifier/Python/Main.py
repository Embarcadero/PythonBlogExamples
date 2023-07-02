import os
from delphifmx import *

# Additional imports
from PIL import Image
from transformers import AutoModelForImageClassification, AutoImageProcessor

class MainForm(Form):

    def __init__(self, owner):
        self.Title = None
        self.FileNameLabel = None
        self.ResultLabel = None
        self.FileName = None
        self.FileSelectButton = None
        self.ClassifyButton = None
        self.OpenDialog1 = None
        self.StyleBook1 = None
        self.LoadProps(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Main.pyfmx"))

        self.FileName.Text = ""
        
        # Loading pre-trained transformer model and feature extractor during app initialization
        self.extractor = AutoImageProcessor.from_pretrained("Kaludi/Food-Classification")
        self.model = AutoModelForImageClassification.from_pretrained("Kaludi/Food-Classification")


    def FileSelectButtonClick(self, Sender):
        # Filepicker window title
        self.OpenDialog1.Title = "Select an Image" 

        # Filtering only image formats to show
        self.OpenDialog1.Filter = "Image files (*.jpg;*.jpeg;*.png;*.gif;*.bmp, *.webp)|*.jpg;*.jpeg;*.png;*.gif;*.bmp;*.webp|All files (*.*)|*.*" 
        
        if self.OpenDialog1.Execute():
            self.FileName.Text = os.path.basename(self.OpenDialog1.FileName) # Display selected image

    def ClassifyButtonClick(self, Sender):
        # Load image from local file
        image = Image.open(self.OpenDialog1.FileName)

        # Preprocess image
        inputs = self.extractor(images=image, return_tensors="pt")

        # Make prediction
        outputs = self.model(**inputs)
        predicted_class_idx = outputs.logits.argmax(-1).item()
        predicted_class = self.model.config.id2label[predicted_class_idx]

        self.ResultLabel.Text = "Result: " + predicted_class # Display prediction
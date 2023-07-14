import os
from delphifmx import *
# Additional Imports
from KMeans import KMeansClustering
from PIL import Image
import numpy as np


class MainForm(Form):

    def __init__(self, owner):
        self.Title = None
        self.KValue = None
        self.KLabel = None
        self.ApplyButton = None
        self.UploadButton = None
        self.OpenDialog1 = None
        self.BeforeImage = None
        self.AfterImage = None
        self.StyleBook1 = None
        self.LoadProps(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Main.pyfmx"))

    def ApplyButtonClick(self, Sender):
        # Create an instance of KMeansClustering
        kmeans = KMeansClustering(int(self.KValue.Text))

        # Load the image from the stream in KMeansClustering
        kmeans.load_image(self.OpenDialog1.FileName)

        # Apply K-means clustering
        segmented_image = kmeans.apply()

        # Convert the segmented image array to PIL Image
        pil_image = Image.fromarray(segmented_image.astype(np.uint8))

        # Save the image to the same directory as the before image
        output_path = os.path.join(os.path.dirname(self.OpenDialog1.FileName), "segmented_image.png")
        pil_image.save(output_path)

        # Load the segmented image in the AfterImage
        self.AfterImage.Bitmap.LoadFromFile(output_path)

    def UploadButtonClick(self, Sender):
        self.OpenDialog1.Title = "Select an Image"

        # Filtering only image formats to show for file pick
        self.OpenDialog1.Filter = "Image files (*.jpg;*.jpeg;*.png;*.webp)|*.jpg;*.jpeg;*.png;*.webp|All files (*.*)|*.*"
       
        if self.OpenDialog1.Execute():
            # Load the selected image into BeforeImage
            self.BeforeImage.Bitmap.LoadFromFile(self.OpenDialog1.FileName)
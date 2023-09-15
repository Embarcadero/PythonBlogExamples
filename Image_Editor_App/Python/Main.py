import os
from delphifmx import *

# Additional Imports
import cloudinary
from cloudinary import uploader
from cloudinary import CloudinaryImage
import requests
import time

class MainFrom(Form):
    def __init__(self, owner):
        self.TabControl1 = None
        self.Edit = None
        self.FilenameLabel = None
        self.EffectLabel = None
        self.IntensityLabel = None
        self.WidthLabel = None
        self.HeightLabel = None
        self.TransformButton = None
        self.FileButton = None
        self.EffectComboBox = None
        self.SpinBox1 = None
        self.DimensionsCheckBox = None
        self.EditImage = None
        self.BackgroundRemoval = None
        self.RemoveBgImage = None
        self.RemoveButton = None
        self.OpenDialog1 = None
        self.StyleBook1 = None
        self.WidthEdit = None
        self.HeightEdit = None
        self.LoadProps(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Main.pyfmx"))

        # Defining different effect options
        self.effect_options = {0:"--", 1:"cartoonify", 2:"pixelate", 3:"sepia", 4:"vignette", 5:"grayscale"}

        # Populating ComboBox
        for option in list(self.effect_options.values()):
            self.EffectComboBox.Items.Add(option)

        # Configure Cloudinary with your account details
        cloudinary.config( 
        cloud_name = "dzte1natd", 
        api_key = "558364876947471", 
        api_secret = "Llc8TFU56g17mjPWK_kEgNd--mE" 
        )

    def BoxChecked(self, Sender):
        if self.DimensionsCheckBox.IsChecked:
            # Enable the WidthEdit and HeightEdit controls
            self.WidthEdit.Enabled = True
            self.HeightEdit.Enabled = True
        else:
            # Disable the WidthEdit and HeightEdit controls
            self.WidthEdit.Enabled = False
            self.HeightEdit.Enabled = False

    def TransformButtonClick(self, Sender):
        transformations = []
        # Adding Height and Width Parameters if Checkbox is checked
        if self.DimensionsCheckBox.IsChecked:
            if self.WidthEdit.Text.isdigit() and self.HeightEdit.Text.isdigit():
                transformations.append({"height": int(self.HeightEdit.Text), "width": int(self.WidthEdit.Text), "crop": "fill"})
        
        # Adding Effect Paramets along with Intensity
        if self.EffectComboBox.ItemIndex in list(self.effect_options.keys()) and self.effect_options[self.EffectComboBox.ItemIndex] != "--" and self.SpinBox1.Text.isdigit():
            if 0 < int(self.SpinBox1.Text) <= 100:
                transformations.append({"effect": "{}:{}".format(self.effect_options[self.EffectComboBox.ItemIndex], self.SpinBox1.Text)})

        # Upload the image to Cloudinary with the specified public ID
        result = uploader.upload(self.OpenDialog1.FileName, public_id=self.public_id, transformation=transformations)['secure_url']

        # Define the local file path where you want to save the image
        local_file_path = ".\Images\edited_"+self.FilenameLabel.Text  # Change to your desired local path

        # Download the transformed image and save it locally
        self.Download(result, local_file_path, self.EditImage)

    def FileButtonClick(self, Sender):
        # Filepicker window title
        self.OpenDialog1.Title = "Select an Image"

        # Filtering only image formats to show
        self.OpenDialog1.Filter = "Image files (*.jpg;*.jpeg;*.png;*.bmp,*.webp)|*.jpg;*.jpeg;*.png;*.bmp;*.webp|All files (*.*)|*.*"
       
        if self.OpenDialog1.Execute():
            self.FilenameLabel.Text = os.path.basename(self.OpenDialog1.FileName) # Display selected image name
            self.EditImage.Bitmap.LoadFromFile(self.OpenDialog1.FileName)
            self.RemoveBgImage.Bitmap.LoadFromFile(self.OpenDialog1.FileName)
            self.public_id = self.FilenameLabel.Text.split('.')[0]

    def RemoveButtonClick(self, Sender):
        self.public_id+='_removal'

        # Uploading Image with background removal API
        result = uploader.upload(self.OpenDialog1.FileName, public_id=self.public_id, background_removal = "cloudinary_ai")
        print(result)
        result= result['secure_url']
        image = CloudinaryImage(self.public_id)

        # Retrieving Image URL
        result = image.url + ".png"
        print(result)

        # Defining Local Save Path
        local_file_path = ".\Images\\bg_removed_"+self.public_id+".png" # Change to your desired local path

        # Adding Time for background removal completion
        time.sleep(5)

        # Downloading Image
        self.Download(result, local_file_path, self.RemoveBgImage)

    def Download(self, result, local_file_path, image):
        # Retrieving Image
        response = requests.get(result, stream=True)

        if response.status_code == 200:
            with open(local_file_path, "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"Transformed image saved to: {local_file_path}")

            # Load and display the downloaded image in the DownloadedImage control
            image.Bitmap.LoadFromFile(local_file_path)
        else:
            print("Failed to download the image.")
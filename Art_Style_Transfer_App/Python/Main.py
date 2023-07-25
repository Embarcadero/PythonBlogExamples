import os
from delphifmx import *
# Additional Imports
import tensorflow as tf
import numpy as np
import PIL.Image
import tensorflow_hub as hub

class MainForm(Form):

    def __init__(self, owner):
        self.Title = None
        self.StyleImageLabel = None
        self.ContentImageLabel = None
        self.UploadContentButton = None
        self.UploadStyleButton = None
        self.ApplyButton = None
        self.StyleImage = None
        self.ContentImage = None
        self.FinalImage = None
        self.OpenDialog1 = None
        self.OpenDialog2 = None
        self.StyleBook1 = None
        self.LoadProps(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Main.pyfmx"))

        # Load compressed models from tensorflow_hub
        os.environ['TFHUB_MODEL_LOAD_FORMAT'] = 'COMPRESSED'

    def load_img(self, path_to_img):
        # Function to load and preprocess an image
        max_dim = 512
        img = tf.io.read_file(path_to_img)
        img = tf.image.decode_image(img, channels=3)
        img = tf.image.convert_image_dtype(img, tf.float32)

        shape = tf.cast(tf.shape(img)[:-1], tf.float32)
        long_dim = max(shape)
        scale = max_dim / long_dim

        new_shape = tf.cast(shape * scale, tf.int32)

        img = tf.image.resize(img, new_shape)
        img = img[tf.newaxis, :]
        return img
    
    def tensor_to_image(self, tensor):
        # Function to convert a tensor to a PIL Image
        tensor = tensor*255
        tensor = np.array(tensor, dtype=np.uint8)
        if np.ndim(tensor) > 3:
            assert tensor.shape[0] == 1
            tensor = tensor[0]
        return PIL.Image.fromarray(tensor)

    def UploadContentButtonClick(self, Sender):
        self.OpenDialog1.Title = "Select your Content Image"

        # Filtering only image formats to show for file pick
        self.OpenDialog1.Filter = "Image files (*.jpg;*.jpeg;*.png)|*.jpg;*.jpeg;*.png|All files (*.*)|*.*"
       
        if self.OpenDialog1.Execute():
            # Load the selected image into ContentImage component
            self.ContentImage.Bitmap.LoadFromFile(self.OpenDialog1.FileName)

    def UploadStyleButtonClick(self, Sender):
        self.OpenDialog2.Title = "Select your Style Image"

        # Filtering only image formats to show for file pick
        self.OpenDialog2.Filter = "Image files (*.jpg;*.jpeg;*.png)|*.jpg;*.jpeg;*.png|All files (*.*)|*.*"
       
        if self.OpenDialog2.Execute():
            # Load the selected image into StyleImage component
            self.StyleImage.Bitmap.LoadFromFile(self.OpenDialog2.FileName)

    def ApplyButtonClick(self, Sender):
        content_image = self.load_img(self.OpenDialog1.FileName)
        style_image = self.load_img(self.OpenDialog2.FileName)

        # Load the Hub model for image stylization
        hub_model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')
        stylized_image = hub_model(tf.constant(content_image), tf.constant(style_image))[0]
        stylized_image = self.tensor_to_image(stylized_image)

        # Save the stylized image locally with a specific filename
        fname = "{}_{}_result.jpg".format(os.path.splitext(os.path.basename(self.OpenDialog1.FileName))[0], os.path.splitext(os.path.basename(self.OpenDialog2.FileName))[0])
        output_path = os.path.join(os.path.dirname(self.OpenDialog1.FileName), fname)
        stylized_image.save(output_path)
        
        # Load the stylized image into the FinalImage component
        self.FinalImage.Bitmap.LoadFromFile(output_path)
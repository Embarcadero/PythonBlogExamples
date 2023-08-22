import os
from delphifmx import *
# Additional imports
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

class MainForm(Form):

    def __init__(self, owner):
        self.Title = None
        self.SLength = None
        self.SWidth = None
        self.PLength = None
        self.PWidth = None
        self.Result = None
        self.SLengthEdit = None
        self.SWidthEdit = None
        self.PLengthEdit = None
        self.PWidthEdit = None
        self.Predict = None
        self.StyleBook1 = None
        self.LoadProps(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Main.pyfmx"))
        
        # Load the Iris dataset
        self.iris = load_iris()
        X, y = self.iris.data, self.iris.target

        # Split the data into training and testing sets
        X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train the SVC model
        self.knn = SVC()
        self.knn.fit(X_train, y_train)

    def PredictClick(self, Sender):
        # User input for flower measurements
        try:
            sepal_length = float(self.SLengthEdit.Text)
            sepal_width = float(self.SWidthEdit.Text)
            petal_length = float(self.PLengthEdit.Text)
            petal_width = float(self.PWidthEdit.Text)
            new_flower = [[sepal_length, sepal_width, petal_length, petal_width]]
            predicted_species = self.knn.predict(new_flower)

            # Map the predicted label to the corresponding species name
            species_names = self.iris.target_names
            predicted_species_name = species_names[predicted_species[0]]
            self.Result.Text = "Species Name: {}".format(predicted_species_name.capitalize())
        except:
            self.Result.Text = "Error! Incomplete or invalid input fields."
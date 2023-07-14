import cv2
from sklearn.cluster import KMeans

class KMeansClustering:
    def __init__(self, K: int):
        self.K = K  # Number of clusters for K-means algorithm
        self.image = None  # Placeholder for the image array
    
    def load_image(self, filename: str):
        self.image = cv2.imread(filename)  # Load the image array using OpenCV
    
    def apply(self):
        # Convert the image from BGR color space to RGB color space
        image_rgb = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)

        # Reshape the image to a 2D array of pixels
        pixels = image_rgb.reshape(-1, 3)

        # Apply K-means clustering algorithm
        kmeans = KMeans(n_clusters=self.K, random_state=42)
        kmeans.fit(pixels)
        labels = kmeans.labels_
        centers = kmeans.cluster_centers_

        # Assign cluster labels to each pixel in the image to create a segmented image
        segmented_image = centers[labels].reshape(image_rgb.shape)

        return segmented_image
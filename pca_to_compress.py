# -*- coding: utf-8 -*-
"""pca_to_compress.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14R5Fj7DEBHpJa5ideNoBeaPE_mgFuMTO
"""

import numpy as np
from sklearn.decomposition import PCA
from skimage import io
from google.colab.patches import cv2_imshow

# Load the image
image = io.imread('/content/Saint-Basils-Cathedral.jpg')

cv2_imshow(image)

# Reshape the image into a 2D array of pixels
rows,cols,colors = image.shape
image_array = np.reshape(image,(rows*cols,colors))

# Apply PCA with a smaller number of components
pca = PCA(n_components=3) #whiten=True
image_pca = pca.fit_transform(image_array)

# Inverse transform the image back to RGB
image_pca_inv = pca.inverse_transform(image_pca)

# Reshape the result into a 3D array of 8-bit integers
image_pca_inv = np.clip(image_pca_inv.astype('uint8'), 0, 255)
image_pca_inv = np.reshape(image_pca_inv, (rows, cols, colors))

cv2_imshow(image_pca_inv)

# Save the result
io.imsave('compressed_image.jpg', image_pca_inv)
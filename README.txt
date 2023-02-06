README
Image compression using ml techniques

#Using Kmeans
1. Load the image
2. Reshape the image into 2D array of pizels
3. Fit the Kmean algorithm using 512 clusters
4. Predict the closest cluster for each pixel
5. Reshape the result into a 3D array of 8-bit integers
6. Show/Save Image

#Using PCA
1. Load the image
2. Reshape the image into 2D array of pizels
3. Fit the PCA algorithm using 3 components
4. Inverse transform the image back to RGB
5. Reshape the result into a 3D array of 8-bit integers
6. Show/Save Image
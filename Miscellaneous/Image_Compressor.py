import os
import sys

from PIL import Image
import numpy as np


# A function that creates initial points for the centroids.
def initialize_K_centroids(X, K):
    m = len(X)
    return X[np.random.choice(m, K, replace=False), :]


# A function to find the closest centroid for each training example
def find_closest_centroids(X, centroids):
    m = len(X)
    c = np.zeros(m)
    for i in range(m):
        distances = np.linalg.norm(X[i] - centroids, axis=1)
        c[i] = np.argmin(distances)
    return c


# Compute the distance of each example to its centroid and take the average of distance for every centroid
def compute_means(X, idx, K):
    _, n = X.shape
    centroids = np.zeros((K, n))
    for k in range(K):
        examples = X[np.where(idx == k)]
        mean = [np.mean(column) for column in examples.T]
        centroids[k] = mean
    return centroids


# Find K-means
def find_k_means(X, K, max_iters=10):
    centroids = initialize_K_centroids(X, K)
    previous_centroids = centroids
    for _ in range(max_iters):
        idx = find_closest_centroids(X, centroids)
        centroids = compute_means(X, idx, K)
        if (centroids == previous_centroids).all():
            # The centroids aren't moving anymore.
            return centroids
        else:
            previous_centroids = centroids

    return centroids, idx


# Get input Image
image_path = './test_goku.png'


# Load Image from the path and return as a Numpy array
def load_image(path):
    image = Image.open(path)
    return np.asarray(image) / 255


image = load_image(image_path)
w, h, d = image.shape
print(F'Image found with width: {w}, height: {h}, depth: {d}')

X = image.reshape((w * h, d))
K = 12  # The desired number of colors in the compressed image

# Get new colors with K-means
colors, _ = find_k_means(X, K, max_iters=20)
idx = find_closest_centroids(X, colors)

# Image Reconstruction
idx = np.array(idx, dtype=np.uint8)
X_reconstructed = np.array(colors[idx, :] * 255, dtype=np.uint8).reshape((w, h, d))
compressed_image = Image.fromarray(X_reconstructed)

compressed_image.save('out.png')


# Getting file stats
def convert_bytes(num):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def file_size(file_path):
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return convert_bytes(file_info.st_size)


print(F"Original Image size is {file_size(image_path)}")
print(F"After Compression, the size is {file_size(r'out.png')}")

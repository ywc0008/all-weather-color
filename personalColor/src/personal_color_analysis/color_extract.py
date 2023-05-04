import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from skimage import io
from itertools import compress

class DominantColors:

    CLUSTERS = None
    IMAGE = None
    COLORS = None
    LABELS = None

    def __init__(self, image, clusters=3):
        self.CLUSTERS = clusters
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        self.IMAGE = img.reshape((img.shape[0] * img.shape[1], 3))
        kmeans = KMeans(n_clusters = self.CLUSTERS)
        kmeans.fit(self.IMAGE)
        self.COLORS = kmeans.cluster_centers_
        self.LABELS = kmeans.labels_

    def rgb_to_hex(self, rgb):
        return '#%02x%02x%02x' % (int(rgb[0]), int(rgb[1]), int(rgb[2]))
    def getHistogram(self):
        numLabels = np.arange(0, self.CLUSTERS+1)
        #create frequency count tables
        (hist, _) = np.histogram(self.LABELS, bins = numLabels)
        hist = hist.astype("float")
        hist /= hist.sum()

        colors = self.COLORS
        colors = colors[(-hist).argsort()]
        hist = hist[(-hist).argsort()]
        for i in range(self.CLUSTERS):
            colors[i] = colors[i].astype(int)
        fil = [colors[i][2] < 250 and colors[i][0] > 10 for i in range(self.CLUSTERS)]
        colors = list(compress(colors, fil))
        return colors, hist

    def plotHistogram(self):
        colors, hist = self.getHistogram()
        chart = np.zeros((50, 500, 3), np.uint8)
        start = 0
        for i in range(len(colors)):
            end = start + hist[i] * 500
            r,g,b = colors[i]
            cv2.rectangle(chart, (int(start), 0), (int(end), 50), (r,g,b), -1)
            start = end
        plt.figure()
        plt.axis("off")
        plt.imshow(chart)
        plt.show()

        return colors

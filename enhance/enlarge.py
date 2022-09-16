# -*- coding: utf-8 -*-
from . import imgprocess
import numpy as np


class Upsample(object):
    def __init__(self, img, out_width: int, out_height: int):
        self.img = imgprocess.ImageProcess(img).openImage()
        # self.height, self.width, self.channel = self.img.shape
        self.width = self.img.size[0]  # The width of the original image
        self.height = self.img.size[1]  # The height of the original image
        self.out_width = out_width
        self.out_height = out_height

    def nearestInterpolation(self):
        """Nearest Neighbour interpolation"""
        out_img = np.zeros((self.out_height, self.out_width, 3), dtype=int)
        img_array = np.array(self.img)

        for i in range(self.out_height - 1):
            for j in range(self.out_width - 1):
                h = round(i * (self.height / self.out_height))
                w = round(j * (self.width / self.out_width))
                out_img[i, j] = img_array[h, w]

        return imgprocess.ImageProcess.saveImage(out_img)

    def bilinearInterpolation(self):
        """Bilinear Interpolation"""
        pass

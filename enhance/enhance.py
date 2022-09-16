# -*- coding: utf-8 -*-
from . import imgprocess
import numpy as np


class Sample(object):
    def __init__(self, img, out_width: int, out_height: int):
        self.img = imgprocess.ImageProcess(img).openImage()
        self.img_array = np.array(self.img)
        self.width = self.img.size[0]  # The width of the original image
        self.height = self.img.size[1]  # The height of the original image
        self.out_width = out_width
        self.out_height = out_height

    def nearestInterpolation(self):
        """Nearest Neighbour interpolation:"""
        out_img = np.zeros((self.out_height, self.out_width, 3), dtype=int)
        for i in range(self.out_height - 1):
            for j in range(self.out_width - 1):
                h = round(i * ((self.height - 1) / self.out_height))
                w = round(j * ((self.width - 1) / self.out_width))
                out_img[i, j, :] = self.img_array[h, w, :]

        return imgprocess.ImageProcess.saveImage(out_img)

    def bilinearInterpolation(self):
        """Bilinear Interpolation"""
        out_img = np.zeros((self.out_height, self.out_width, 3), dtype=int)
        for i in range(self.out_height):
            for j in range(self.out_width):
                h = i * float(self.height / self.out_height)
                w = j * float(self.width / self.out_width)
                h_int = i * self.height // self.out_height
                w_int = j * self.width // self.out_width
                a = w - w_int
                b = h - h_int
                if h_int + 1 == self.height or w_int + 1 == self.width:
                    out_img[i, j, :] = self.img_array[h_int, w_int, :]
                    continue
                out_img[i, j, :] = \
                    (1. - a) * (1. - b) * self.img_array[h_int + 1, w_int + 1, :] \
                    + (1. - a) * b * self.img_array[h_int, w_int + 1, :] \
                    + a * (1. - b) * self.img_array[h_int + 1, w_int, :] \
                    + a * b * self.img_array[h_int, w_int, :]

        return imgprocess.ImageProcess.saveImage(out_img)

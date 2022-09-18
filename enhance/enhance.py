# -*- coding: utf-8 -*-
from . import imgprocess
import numpy as np


class Sample(object):
    def __init__(self, img, out_width: int, out_height: int):
        self.img = imgprocess.ImageProcess(img).openImage()
        self.img_array = np.array(self.img)
        self.width = self.img.size[0]
        self.height = self.img.size[1]
        self.out_width = out_width
        self.out_height = out_height

    def nearestInterpolation(self):
        print("Start Nearest Neighbour Interpolation".center(50, "-"))
        """Nearest neighbour interpolation:"""
        out_img = np.zeros((self.out_height, self.out_width, 3), dtype=int)
        for i in range(self.out_height - 1):
            for j in range(self.out_width - 1):
                h = round(i * ((self.height - 1) / self.out_height))
                w = round(j * ((self.width - 1) / self.out_width))
                out_img[i, j, :] = self.img_array[h, w, :]
        print("End Nearest Neighbour Interpolation".center(50, "-"))
        return imgprocess.ImageProcess.saveImage(out_img)

    def bilinearInterpolation(self):
        """Bilinear interpolation"""
        print("Start Bilinear Interpolation".center(50, "-"))
        # Projection
        width = \
            np.array([(i + 0.5) / self.out_width * self.width - 0.5 for i in range(self.out_width)], dtype=float)
        height = \
            np.array([(i + 0.5) / self.out_height * self.height - 0.5 for i in range(self.out_height)], dtype=float)
        width = np.clip(width, 0, self.width - 1)  # repair a bug
        height = np.clip(height, 0, self.height - 1)  # repair a bug
        width = np.repeat(width.reshape(1, self.out_width), self.out_height, axis=0)
        height = np.repeat(height.reshape(self.out_height, 1), self.out_width, axis=1)

        width0 = np.clip(np.floor(width), 0, self.width - 2).astype(int)
        height0 = np.clip(np.floor(height), 0, self.height - 2).astype(int)
        width1 = width0 + 1
        height1 = height0 + 1

        # Get the surrounding pixels
        pixel_00 = self.img_array[height0, width0, :].T
        pixel_01 = self.img_array[height0, width1, :].T
        pixel_10 = self.img_array[height1, width0, :].T
        pixel_11 = self.img_array[height1, width1, :].T

        # Calculate the weight
        weight_00 = ((height1 - height) * (width1 - width)).T
        weight_01 = ((height1 - height) * (width - width0)).T
        weight_10 = ((height - height0) * (width1 - width)).T
        weight_11 = ((height - height0) * (width - width0)).T

        out_img = \
            (pixel_00 * weight_00).T + (pixel_01 * weight_01).T + (pixel_10 * weight_10).T + (pixel_11 * weight_11).T

        print("End Bilinear Interpolation".center(50, "-"))
        return imgprocess.ImageProcess.saveImage(out_img)

# def bilinearInterpolation(self):
#     """Bilinear Interpolation"""
#     out_img = np.zeros((self.out_height, self.out_width, 3), dtype=int)
#     rate_height = self.height / self.out_height
#     rate_width = self.width / self.out_width
#     for i in range(self.out_height):
#         for j in range(self.out_width):
#             h = i * float(rate_height)
#             w = j * float(rate_width)
#             h_int = i * self.height // self.out_height
#             w_int = j * self.width // self.out_width
#             a = w - w_int
#             b = h - h_int
#             if h_int + 1 == self.height or w_int + 1 == self.width:
#                 out_img[i, j, :] = self.img_array[h_int, w_int, :]
#                 continue
#             out_img[i, j, :] = \
#                 (1. - a) * (1. - b) * self.img_array[h_int + 1, w_int + 1, :] \
#                 + (1. - a) * b * self.img_array[h_int, w_int + 1, :] \
#                 + a * (1. - b) * self.img_array[h_int + 1, w_int, :] \
#                 + a * b * self.img_array[h_int, w_int, :]
#
#     return imgprocess.ImageProcess.saveImage(out_img)

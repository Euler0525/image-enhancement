# -*- coding: utf-8 -*-
import numpy as np
from . import imgprocess


class Sample(object):
    def __init__(self, img, out_width: int, out_height: int):
        self.img = imgprocess.ImageProcess(img).openImage()
        self.img_array = np.array(self.img)
        self.width = self.img.size[0]
        self.height = self.img.size[1]
        self.out_width = out_width
        self.out_height = out_height

    def nearestInterpolation(self):
        """Nearest neighbour interpolation"""
        out_img = np.zeros([self.out_height, self.out_width, 3], dtype=int)

        scale_h = self.out_height / self.height
        scale_w = self.out_width / self.width

        # Generates an initial matrix based on the size of the target image
        height = np.arange(self.out_height)
        width = np.arange(self.out_width)
        height = np.floor(height / scale_h).astype(int)
        width = np.floor(width / scale_w).astype(int)

        # Generate projection matrix
        height = height.reshape(height.shape[0], 1)
        height = np.tile(height, (1, self.out_width))
        width = np.tile(width, (self.out_height, 1))

        # Project the original image to the target image
        out_img[:, :] = self.img_array[height[:, :], width[:, :]]

        return imgprocess.ImageProcess.saveImage(out_img)

    def bilinearInterpolation(self):
        """Bilinear interpolation"""
        # Projection
        width = \
            np.array([(i + 0.5) / self.out_width * self.width - 0.5 for i in range(self.out_width)], dtype=float)
        height = \
            np.array([(i + 0.5) / self.out_height * self.height - 0.5 for i in range(self.out_height)], dtype=float)
        width = np.clip(width, 0, self.width - 1)  # repair a bug
        height = np.clip(height, 0, self.height - 1)  # repair a bug

        height = np.repeat(height.reshape(self.out_height, 1), self.out_width, axis=1)
        width = np.repeat(width.reshape(1, self.out_width), self.out_height, axis=0)

        height0 = np.clip(np.floor(height), 0, self.height - 2).astype(int)
        height1 = height0 + 1
        width0 = np.clip(np.floor(width), 0, self.width - 2).astype(int)
        width1 = width0 + 1

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

        return imgprocess.ImageProcess.saveImage(out_img)

# -*- coding: utf-8 -*-
from PIL import Image
import numpy as np


class ImageProcess(object):
    def __init__(self, in_img: str):
        self.img = in_img

    def openImage(self):
        """Open an image and return <class 'numpy.ndarray'>"""
        # return np.array(Image.open(self.img))
        return Image.open(self.img)

    @staticmethod
    def saveImage(array):
        """convert array to image and return  <class 'PIL.PngImagePlugin.PngImageFile'>"""
        out_img = Image.fromarray(array.astype("uint8")).convert("RGB")

        return out_img


if __name__ == "__main__":
    pass
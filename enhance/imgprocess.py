# -*- coding: utf-8 -*-
from PIL import Image
import numpy as np


class ImageProcess(object):
    def __init__(self, in_img: str):
        self.img = in_img
        self.support = ["RGB"]

    def openImage(self):
        """Open an image and return PIL.PngImagePlugin.PngImageFile"""
        img = Image.open(self.img)
        try:
            if img.mode not in self.support:
                raise ModeError(img.mode)
        except Exception as result:
            print(result)
            return img.convert("RGB")
        else:
            return img

    @staticmethod
    def saveImage(array: np.ndarray):
        """convert array to image and return PIL.PngImagePlugin.PngImageFile"""
        out_img = Image.fromarray(array.astype("uint8")).convert("RGB")
        return out_img


class ModeError(Exception):
    """img.mode exception"""

    def __init__(self, mode):
        self.support = ["RGB"]
        self.mode = mode

    def __str__(self):
        return f"Mode \"{self.mode}\" is not supported and it has been convert to \"RGB\""

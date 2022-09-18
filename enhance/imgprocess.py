# -*- coding: utf-8 -*-
from PIL import Image


class ImageProcess(object):
    def __init__(self, in_img: str):
        self.img = in_img

    def openImage(self):
        """Open an image and return PIL.PngImagePlugin.PngImageFile"""
        return Image.open(self.img)

    @staticmethod
    def saveImage(array):
        """convert array to image and return PIL.PngImagePlugin.PngImageFile"""
        out_img = Image.fromarray(array.astype("uint8")).convert("RGB")

        return out_img

# -*- coding: utf-8 -*-
from enhance import *
import fire


def main(img: str, choice: str, w: int, h: int):
    test_img = img
    obj = enhance.Sample(test_img, w, h)
    if choice == "n":
        obj.nearestInterpolation().save("./test/nearest.png")
    elif choice == "b":
        obj.bilinearInterpolation().save("./test/bilinear.png")
    else:
        exit()


if __name__ == "__main__":
    fire.Fire(main)

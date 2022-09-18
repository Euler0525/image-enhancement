# -*- coding: utf-8 -*-
from enhance import *
import fire


def main(img: str, out_img: str, choice: str, w: int, h: int):
    test_img = img
    obj = enhance.Sample(test_img, w, h)
    if choice == "n":
        obj.nearestInterpolation().save(out_img)
    elif choice == "b":
        obj.bilinearInterpolation().save(out_img)
    else:
        exit()


if __name__ == "__main__":
    fire.Fire(main)

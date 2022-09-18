# -*- coding: utf-8 -*-
from enhance import *
import fire


def main(in_img: str, out_img: str, choice: str, w: int, h: int):
    obj = enhance.Sample(in_img, w, h)
    if choice == "n":
        obj.nearestInterpolation().save(out_img)
    elif choice == "b":
        obj.bilinearInterpolation().save(out_img)
    else:
        exit()


if __name__ == "__main__":
    try:
        fire.Fire(main)
    except Exception as result:
        print(result)

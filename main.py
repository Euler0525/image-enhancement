# -*- coding: utf-8 -*-

from enhance import *


def main():
    test_img = "./test/test.png"
    obj = enhance.Sample(test_img, 200, 200)
    obj.nearestInterpolation().save("./test/1.png")
    obj.bilinearInterpolation().save("./test/2.png")


if __name__ == "__main__":
    main()

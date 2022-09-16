# -*- coding: utf-8 -*-

from enhance import *


def main():
    test_img = "./test/test.png"
    obj = enlarge.Upsample(test_img, 256, 256)
    obj.nearestInterpolation().show()


if __name__ == "__main__":
    main()



# from PIL import Image
# import matplotlib.pyplot as plt
# import numpy as np
# import math
#
#
# def NN_interpolation(img, dstH, dstW):
#     scrH, scrW, t = img.shape  # src原图的长宽
#     retimg = np.zeros((dstH, dstW, 3), dtype=np.uint8)
#     for i in range(dstH - 1):
#         for j in range(dstW - 1):
#             scrx = round(i * (scrH / dstH))
#             scry = round(j * (scrW / dstW))
#             retimg[i, j] = img[scrx, scry]
#     return retimg
#
#
# im_path = "./test/test.png"
# image = np.array(Image.open(im_path))
#
# plt.figure(figsize=(16, 8))
#
# plt.subplot(1, 2, 1)
# plt.imshow(image)
#
# image1 = NN_interpolation(image, image.shape[0] * 2, image.shape[1] * 2)
# # 从array转换成image
# image1 = Image.fromarray(image1.astype('uint8')).convert('RGB')
# image1.save("./test/out.png")
# plt.subplot(1, 2, 2)
# plt.imshow(image1)

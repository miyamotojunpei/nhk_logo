import cv2
import numpy as np


def main():
    # 画像の読み込み
    images = read_images()


    return


def read_images():
    background_image = cv2.imread("../image/nhk_logo_background.png", cv2.IMREAD_COLOR)
    n_image = cv2.imread("../image/nhk_logo_n.png", cv2.IMREAD_UNCHANGED)
    h_image = cv2.imread("../image/nhk_logo_h.png", cv2.IMREAD_UNCHANGED)
    k_image = cv2.imread("../image/nhk_logo_k.png", cv2.IMREAD_UNCHANGED)
    return background_image, n_image, h_image, k_image









if __name__ == "__main__":
    main()
import cv2
from egg import Egg
import numpy as np


def main():
    # 画像の読み込み
    images = read_images()

    # ゲームスタート
    start_game(images)

    return


def read_images():
    bg_image = cv2.imread("../image/nhk_logo_background.png", cv2.IMREAD_COLOR)
    n_image = Egg("nhk_logo_n.png")
    h_image = Egg("nhk_logo_h.png")
    k_image = Egg("nhk_logo_k.png")

    return bg_image, n_image, h_image, k_image


def start_game(images):
    stop_count = 0
    while stop_count < 3:
        rotate(images)

    print_score()

def rotate(images):
    while








if __name__ == "__main__":
    main()
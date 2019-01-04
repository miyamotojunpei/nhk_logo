import cv2
from egg import Egg
import mouseevent
import numpy as np


def main():
    # 画像の読み込み
    images = read_images()

    # ゲームスタート
    start_game(images)

    #スコア表示
    print_score()
    return


def read_images():
    bg_image = cv2.imread("../image/nhk_logo_background_rgba.png", cv2.IMREAD_UNCHANGED)
    bg_image = np.zeros(bg_image.shape, dtype=np.uint8)
    n_image = Egg("nhk_logo_n.png", 372, 242, 0)
    h_image = Egg("nhk_logo_h.png", 372, 242, 290)
    k_image = Egg("nhk_logo_k.png", 372, 242, 579)

    return bg_image, n_image, h_image, k_image


def start_game(images):
    stop_count = 0
    win_name = "NHK"
    cv2.namedWindow(win_name, cv2.WINDOW_AUTOSIZE)
    cv2.setMouseCallback(win_name, mouseevent.mouse_event)

    while stop_count < 3:
        current_image = rotate(images)
        cv2.imshow(win_name, current_image)
        cv2.waitKey(1)
    return


def rotate(images):
    bg_image = images[0]
    n_rotated = images[1].rotate()
    h_rotated = images[2].rotate()
    k_rotated = images[3].rotate()

    current_image = overlay(bg_image.copy(), n_rotated)
    current_image = overlay(current_image, h_rotated)
    current_image = overlay(current_image, k_rotated)

    current_image[np.where((current_image == [0, 0, 0, 0]).all(axis=2))] = [255, 255, 255, 255]
    return current_image


def overlay(bg_image, rotated):
    bg_image[rotated.y_offset:rotated.y_offset + rotated.size, rotated.x_offset:rotated.x_offset + rotated.size] += rotated.image
    return bg_image


if __name__ == "__main__":
    main()
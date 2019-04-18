import cv2
from egg import Egg
import mouseevent
import numpy as np


def main():
    while True:
        # 画像の読み込み
        images = read_images()

        # ゲームスタート
        key = start_game(images)
        # rキーを押すとループ
        if key != ord('r'):
            break
    return


def read_images():
    n_image = Egg("nhk_logo_n.png", 372, 242, 0)
    h_image = Egg("nhk_logo_h.png", 372, 242, 290)
    k_image = Egg("nhk_logo_k.png", 372, 242, 579)

    return n_image, h_image, k_image


def start_game(images):
    stop_count = 0
    win_name = "NHK"
    cv2.namedWindow(win_name, cv2.WINDOW_AUTOSIZE)
    mouse = mouseevent.MouseParam(win_name)

    while stop_count < 3:
        if mouse.get_event() == cv2.EVENT_LBUTTONUP:
            mouse_pos = mouse.get_pos()
        else:
            mouse_pos = (0, 0)
        current_image, stop_count = rotate(images, mouse_pos)
        cv2.imshow(win_name, current_image)
        cv2.waitKey(1)

    final_image = print_score(current_image, images)
    cv2.imshow(win_name, final_image)
    key = cv2.waitKey(0)
    return key


def rotate(images, mouse_pos):
    bg_image = np.zeros((960, 960, 4), dtype=np.uint8)
    n_rotated = images[0].stop(mouse_pos).rotate()
    h_rotated = images[1].stop(mouse_pos).rotate()
    k_rotated = images[2].stop(mouse_pos).rotate()

    current_image = overlay(bg_image, n_rotated)
    current_image = overlay(current_image, h_rotated)
    current_image = overlay(current_image, k_rotated)

    current_image[np.where((current_image == [0, 0, 0, 0]).all(axis=2))] = [255, 255, 255, 255]
    return current_image, sum(x.stopped for x in images)


def overlay(bg_image, rotated):
    bg_image[rotated.y_offset:rotated.y_offset + rotated.size, rotated.x_offset:rotated.x_offset + rotated.size] += rotated.image
    return bg_image


def print_score(current_image, images):
    score = sum(abs(x.error-180) for x in images) * 100 // 540
    cv2.putText(current_image, "Shichoritsu:" + str(score) + "%", (50, 200), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 0), 5, cv2.LINE_AA)
    return current_image


if __name__ == "__main__":
    main()
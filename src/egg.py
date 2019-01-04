import cv2
import copy
import time


class Egg:
    def __init__(self, image, size, y_offset, x_offset):
        self.image = cv2.imread("../image/"+image, cv2.IMREAD_UNCHANGED)
        self.size = size
        self.y_offset = y_offset
        self.x_offset = x_offset

    def rotate(self):
        copied_object = copy.deepcopy(self)
        # 画像の中心位置(x, y)
        center = tuple([self.size // 2, self.size // 2])

        # 回転させたい角度（正の値は反時計回り）
        angle = time.time()

        # 拡大比率
        scale = 1.0

        # 回転変換行列の算出
        rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)

        # アフィン変換
        img_rot = cv2.warpAffine(copied_object.image, rotation_matrix, (self.size, self.size), flags=cv2.INTER_CUBIC)
        copied_object.image = img_rot
        return copied_object
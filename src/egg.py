import cv2
import copy
import time


class Egg:
    def __init__(self, image, size, y_offset, x_offset):
        self.image = cv2.imread("../image/"+image, cv2.IMREAD_UNCHANGED)
        self.size = size
        self.y_offset = y_offset
        self.x_offset = x_offset
        self.stopped = False
        self.error = 0

    def rotate(self):

        copied_object = copy.deepcopy(self)

        # 画像の中心位置(x, y)
        center = tuple([self.size // 2, self.size // 2])

        # 回転させたい角度（正の値は反時計回り）
        if self.stopped:
            angle = self.error
        else:
            angle = time.time() * 360

        # 拡大比率
        scale = 1.0

        # 回転変換行列の算出
        rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)

        # アフィン変換
        img_rot = cv2.warpAffine(copied_object.image, rotation_matrix, (self.size, self.size), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_TRANSPARENT)
        img_rot[0:10, :, :] = 0
        copied_object.image = img_rot
        return copied_object

    def stop(self, mouse_pos):
        if not self.stopped \
                and (self.x_offset+self.size//4, self.y_offset+self.size//4,)\
                < mouse_pos < (self.x_offset+self.size*3//4, self.x_offset+self.size*3//4,):
            self.stopped = True
            self.error = time.time() * 360
        return self
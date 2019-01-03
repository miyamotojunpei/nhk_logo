import cv2


class Egg:
    def __init__(self, image):
        self.image = cv2.imread("../image/"+image, cv2.IMREAD_UNCHANGED)
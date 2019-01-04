import cv2


def mouse_event(event, x, y, flags, param):
    # 左クリックで赤い円形を生成
    if event == cv2.EVENT_LBUTTONUP:
        return x, y
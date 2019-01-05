import cv2


class MouseParam:
    def __init__(self, input_img_name):
        # マウス入力用のパラメータ
        self.mouseEvent = {"x": None, "y": None, "event": None, "flags": None}
        # マウス入力の設定
        cv2.setMouseCallback(input_img_name, self.__callback_func, None)

    # コールバック関数
    def __callback_func(self, event_type, x, y, flags, user_data):
        self.mouseEvent["x"] = x
        self.mouseEvent["y"] = y
        self.mouseEvent["event"] = event_type
        self.mouseEvent["flags"] = flags

        # マウス入力用のパラメータを返すための関数

    def get_data(self):
        return self.mouseEvent

    # マウスイベントを返す関数
    def get_event(self):
        return self.mouseEvent["event"]

        # マウスフラグを返す関数

    def get_flags(self):
        return self.mouseEvent["flags"]

        # xの座標を返す関数

    def get_x(self):
        return self.mouseEvent["x"]

        # yの座標を返す関数

    def get_y(self):
        return self.mouseEvent["y"]

        # xとyの座標を返す関数

    def get_pos(self):
        return self.mouseEvent["x"], self.mouseEvent["y"]


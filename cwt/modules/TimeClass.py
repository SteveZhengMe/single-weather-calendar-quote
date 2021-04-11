import random
import time

from PIL import Image, ImageDraw

from cwt.utils.DrawUtils import Text, Font


class EPaperTime:
    def __init__(self):
        pass

    def draw(self, target_canvas, font_color="#000000"):
        img_draw = ImageDraw.Draw(target_canvas)
        current_time = time.localtime(time.time())
        time_hour = time.strftime('%H',current_time)
        time_minute = time.strftime('%M',current_time)

        minute_offset = random.choice([0,1,2,3,4])
        time_minute_int = int(time_minute) + minute_offset

        if time_minute_int < 10:
            time_string = "%s:%s" % (time_hour, "0" + str(time_minute_int))
        else:
            time_string = "%s:%d" % (time_hour, time_minute_int)

        text = Text(time_string, Font("simkai.ttf", 126, font_color),"center")

        text.draw(img_draw, (0, 0), (target_canvas.width, target_canvas.height))

    def test(self):
        im = Image.new("RGB", (340, 124), "#FFFFFF")
        self.draw(im)
        im.show()

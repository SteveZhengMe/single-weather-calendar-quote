from datetime import datetime
import re

from PIL import Image, ImageDraw
import calendar

from cwt.utils.DrawUtils import Text, Font

class EPaperCalendar:
    def __init__(self):
        pass

    def draw(self, target_canvas, font_color="#000000"):
        current_date = datetime.today().strftime('%m月%d日') + self.to_Chinese(datetime.today().weekday())

        img_draw = ImageDraw.Draw(target_canvas)

        text_current_date = Text(current_date, Font("simkai.ttf",36, font_color),"center")
        cal_string = self.generate_month_calendar()
        text_calendar = Text(cal_string, Font("simhei.ttf",28, font_color),"center")

        text_current_date.draw(img_draw,(0,30), (target_canvas.width,target_canvas.height*0.2))
        text_calendar.draw(img_draw,(0,target_canvas.height*0.2), (target_canvas.width,target_canvas.height))

    def generate_month_calendar(self):
        current_year = datetime.today().strftime('%Y')
        current_month = datetime.today().strftime('%m')
        calendar.setfirstweekday(calendar.SUNDAY)
        res_list = re.split("\n",calendar.month(int(current_year), int(current_month)))
        return "\n".join(res_list[1:])

    def to_Chinese(self, source_str):
        map = {
            0: "星期一",
            1: "星期二",
            2: "星期三",
            3: "星期四",
            4: "星期五",
            5: "星期六",
            6: "星期日"
        }
        return map[source_str]

    def test(self):
        im = Image.new("RGB", (300, 284), "#000000")
        self.draw(im, "#FFFFFF")
        im.show()

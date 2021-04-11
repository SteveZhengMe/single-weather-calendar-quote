from PIL import Image, ImageDraw
import datetime
import json
import os
import time
import traceback
from urllib.error import HTTPError

from cwt.conf import WEATHER_API_KEY, CITY
import cwt.utils.RequestUtils as request
from cwt.utils.DrawUtils import Text, Font

CELSIUS = "℃"
weather_content_file_fullpath = "weather_content.json"
weather_mapping = {
    "01": "C",
    "02": "b",
    "03": "d",
    "04": "e",
    "09": "h",
    "10": "g",
    "11": "i",
    "13": "k",
    "50": "v",
}


class EPaperWeather:
    def __init__(self):
        pass

    def check_reload(self):
        current_time = time.localtime(time.time())
        minute_string = time.strftime('%M', current_time)
        hour_string = time.strftime('%H', current_time)
        return int(minute_string) == 0 and int(hour_string) > 6

    def get_weather_content(self):
        if not self.check_reload():
            return self.read_weather_cache()

        return self.reload_weather()

    def draw(self, target_canvas, font_color="#000000"):
        try:
            weather_json = json.loads(self.get_weather_content())

            weather_icon = weather_mapping.get(weather_json["weather"][0]["icon"][0:2])
            desc = weather_json["weather"][0]["main"]
            temp_min = weather_json["main"]["temp_min"]
            temp = weather_json["main"]["temp"]
            temp_max = weather_json["main"]["temp_max"]
            humidity = weather_json["main"]["humidity"]
            city_name = weather_json["name"]
            dt = weather_json["dt"]
            # dt_utc = datetime.datetime.fromtimestamp(int(dt)).replace(tzinfo=timezone('UTC'))
            dt_desc = datetime.datetime.fromtimestamp(int(dt)).strftime('%Y-%m-%d %H:%M')

            text_weather = Text(weather_icon, Font("weather.ttf", 146, font_color), "center")
            text_current = Text("%s/%d%s/(%d%%)" % (desc, temp, CELSIUS, humidity), Font("simkai.ttf", 36, font_color), "center")
            text_minmax = Text("%d%s ～ %d%s" % (temp_min, CELSIUS, temp_max, CELSIUS), Font("simkai.ttf", 36, font_color), "center")
            text_city = Text("%s (Update at %s)" % (city_name, dt_desc), Font("simkai.ttf", 14, font_color), "right")

            img_draw = ImageDraw.Draw(target_canvas)
            text_weather.draw(img_draw, (0, 30), (target_canvas.width, target_canvas.height * 0.5))
            # print(target_canvas.height*0.4)
            text_current.draw(img_draw, (0, target_canvas.height * 0.5), (target_canvas.width, target_canvas.height * 0.7))
            text_minmax.draw(img_draw, (0, target_canvas.height * 0.7), (target_canvas.width, target_canvas.height * 0.9))
            text_city.draw(img_draw, (0, target_canvas.height * 0.9), (target_canvas.width, target_canvas.height))

        except HTTPError:
            os.remove(weather_content_file_fullpath)
        except IOError:
            msg = traceback.format_exc()
            print(msg)

    def reload_weather(self):
        weather_content = request.get_html_content("https://api.openweathermap.org/data/2.5/weather?q=%s,ca&APPID=%s&units=metric" % (CITY, WEATHER_API_KEY))

        if weather_content is not None:
            if os.access(weather_content_file_fullpath, os.F_OK):
                os.remove(weather_content_file_fullpath)

            with open(weather_content_file_fullpath, 'wt', encoding='utf-8') as f:
                f.write(weather_content.decode("utf-8"))

            return weather_content.decode("utf-8")
        else:
            return self.read_weather_cache()

    def read_weather_cache(self):
        if os.access(weather_content_file_fullpath, os.R_OK):
            with open(weather_content_file_fullpath, 'r') as f:
                return "\n".join(f.readlines())
        return None

    def test(self):
        im = Image.new("RGB", (340, 260), "#FFFFFF")
        self.draw(im)
        im.show()
